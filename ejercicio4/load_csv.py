import sys
import json
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener
from collections import defaultdict

class Loader(CSVListener):
    EMPTY = ""
    
    def __init__(self):
        self.rows = []  # Lista para almacenar todas las filas procesadas
        self.header = []  # Encabezado del CSV
        self.currentRowFieldValues = []  # Para almacenar los valores de la fila actual
        self.emptyFieldCount = 0  # Contador de campos vacíos
        self.months_count = defaultdict(int)  # Diccionario para contar cuántas veces aparece cada mes
        self.seen_rows = set()  # Para almacenar las filas procesadas y detectar duplicados
        self.month_totals = defaultdict(float)  # Diccionario para sumar valores por mes

    def enterRow(self, ctx: CSVParser.RowContext):
        """Se ejecuta al empezar a procesar una fila."""
        self.currentRowFieldValues = []  # Limpiar los valores de la fila

    def exitText(self, ctx: CSVParser.TextContext):
        """Procesa los valores normales de texto de la fila."""
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx: CSVParser.StringContext):
        """Procesa los valores de cadenas con comillas."""
        self.currentRowFieldValues.append(ctx.getText())

    def exitEmpty(self, ctx: CSVParser.EmptyContext):
        """Procesa los campos vacíos."""
        self.currentRowFieldValues.append(self.EMPTY)
        self.emptyFieldCount += 1

    def exitHeader(self, ctx: CSVParser.HeaderContext):
        """Cuando se termina de procesar el encabezado."""
        self.header = list(self.currentRowFieldValues)

    def exitRow(self, ctx: CSVParser.RowContext):
        """Cuando se termina de procesar una fila."""
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return  # Si es una fila de encabezado, se ignora

        # Verificar que la cantidad de campos sea correcta
        if len(self.currentRowFieldValues) != len(self.header):
            print(f"Fila inválida: {self.currentRowFieldValues}")
            return

        # Convertir la fila en un diccionario
        row_dict = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i] if i < len(self.header) else f"col_{i}"
            row_dict[key] = val

        # Detectar filas repetidas
        row_tuple = tuple(row_dict.items())  # Convertir la fila en una tupla para comprobar si ya fue procesada
        if row_tuple in self.seen_rows:
            print(f"Fila repetida: {row_dict}")
        else:
            self.seen_rows.add(row_tuple)

        # Contar las ocurrencias de meses (suponiendo que la columna "Mes" existe)
        if "Mes" in row_dict:
            try:
                mes = row_dict["Mes"]
                self.months_count[mes] += 1
            except IndexError:
                print(f"Mes mal formateado en la fila: {row_dict}")

        # Procesar la columna de "Cantidad" (suponiendo que está en la columna 'Cantidad')
        if "Cantidad" in row_dict:
            try:
                # Limpiar y convertir el valor de "Cantidad" a un número
                cantidad = row_dict["Cantidad"].replace('"', '').replace('$', '').replace(',', '')

                # Si la cantidad es "N/A" o vacía, no la procesamos como número
                if cantidad in ["N/A", ""]:
                    cantidad_float = 0  # Asignamos 0 para los valores no válidos
                else:
                    cantidad_float = float(cantidad)  # Convertimos a float si es válido

                # Si la cantidad es válida, sumamos por mes
                if cantidad_float > 0:
                    if "Mes" in row_dict:
                        mes = row_dict["Mes"]
                        self.month_totals[mes] += cantidad_float
            except ValueError:
                print(f"Campo 'Cantidad' mal formateado: {row_dict['Cantidad']} en la fila: {row_dict}")

        # Almacenar la fila procesada
        self.rows.append(row_dict)

    def print_column_stats(self, column_name="Cantidad"):
        """Imprime estadísticas de la columna 'Cantidad'."""
        valores = [fila[column_name] for fila in self.rows if column_name in fila]
        print(f"\nEstadísticas para columna '{column_name}':")
        for valor in valores:
            print(f"• {valor}")

    def limpiar_montos(self):
        """Limpiar los montos de la columna 'Cantidad' eliminando símbolos."""
        for fila in self.rows:
            if "Cantidad" in fila:
                fila["Cantidad"] = fila["Cantidad"].replace('"', '').replace('$','').replace(',', '')

    def exportar_a_json(self, filename="output.json"):
        """Exporta las filas procesadas a un archivo JSON."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)

    def print_month_stats(self):
        """Imprime estadísticas sobre los meses procesados y los totales por mes."""
        print("\nEstadísticas por mes:")
        for mes, total in self.month_totals.items():
            print(f"• {mes}: {total}")

        print("\nConteo de meses:")
        for mes, count in self.months_count.items():
            print(f"• {mes}: {count}")


def main(argv):
    """Función principal para cargar y procesar el archivo CSV."""
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # Imprimir estadísticas de los meses y el conteo de filas
    loader.print_month_stats()

    # Imprimir todas las filas procesadas
    for row in loader.rows:
        print(row)

    # Limpiar montos y exportar a JSON
    loader.limpiar_montos()
    loader.exportar_a_json("output.json")


if __name__ == '__main__':
    main(sys.argv)
