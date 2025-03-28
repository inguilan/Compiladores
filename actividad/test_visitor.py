from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx: MiGramaticaParser.ProgramaContext):
        for stmt in ctx.sentencia():
            self.visit(stmt)

    def visitAssign(self, ctx: MiGramaticaParser.AssignContext):
        # Realizamos la asignación
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        return value

    def visitForLoopWithBody(self, ctx: MiGramaticaParser.ForLoopWithBodyContext):
        print("Ejecutando ciclo for con cuerpo...")  # Depuración
        # Ejecutamos la inicialización
        self.visit(ctx.inicializacion())

        # Simulamos el ciclo for con cuerpo
        iteration_count = 0
        while self.visit(ctx.condicion()):
            iteration_count += 1
            print(f"Iteración {iteration_count}: i={self.variables.get('i', 0)}")  # Depuración
            # Ejecutamos las sentencias dentro del ciclo
            for stmt in ctx.sentencia():
                self.visit(stmt)

            # Realizamos la actualización del for
            self.visit(ctx.actualizacion())

            if iteration_count > 10:  # Limitar el número de iteraciones para evitar bucles infinitos
                print("Demasiadas iteraciones. Deteniendo el ciclo.")
                break

    def visitForLoopEmpty(self, ctx: MiGramaticaParser.ForLoopEmptyContext):
        print("Ejecutando ciclo for vacío...")  # Depuración
        # Ejecutamos la inicialización
        self.visit(ctx.inicializacion())

        # Simulamos el ciclo for vacío
        iteration_count = 0
        while self.visit(ctx.condicion()):
            iteration_count += 1
            print(f"Iteración {iteration_count}: i={self.variables.get('i', 0)}")  # Depuración
            # Realizamos la actualización del for
            self.visit(ctx.actualizacion())

            if iteration_count > 10:  # Limitar el número de iteraciones para evitar bucles infinitos
                print("Demasiadas iteraciones. Deteniendo el ciclo.")
                break

    def visitCondicion(self, ctx: MiGramaticaParser.CondicionContext):
        left = self.variables.get(ctx.ID().getText(), 0)
        right = int(ctx.INT().getText())
        op = ctx.op.text
        print(f"Evaluando condición: {left} {op} {right}")  # Depuración
        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitAddSub(self, ctx: MiGramaticaParser.AddSubContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitMulDiv(self, ctx: MiGramaticaParser.MulDivContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            return left / right

    def visitInt(self, ctx: MiGramaticaParser.IntContext):
        return int(ctx.getText())

    def visitVariable(self, ctx: MiGramaticaParser.VariableContext):
        return self.variables.get(ctx.getText(), 0)

def main():
    input_code = input("Ingresa código: ")
    input_stream = InputStream(input_code)
    lexer = MiGramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(token_stream)

    # Generamos el árbol de sintaxis
    tree = parser.programa()
    visitor = EvalVisitor()
    visitor.visit(tree)
    print(f"Estado final de las variables: {visitor.variables}")

if __name__ == "__main__":
    main()