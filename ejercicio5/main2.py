import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from SimpleListener import SimpleListener

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")
        print(f"    Causa: {self.identify_cause(msg)}")
        print(f"    Corrección sugerida: {self.suggest_correction(msg)}")
    
    def identify_cause(self, msg):
        if "mismatched input" in msg:
            return "Sintaxis inesperada, posiblemente falta un símbolo o palabra clave."
        elif "extraneous input" in msg:
            return "Símbolos adicionales que no se esperaban en ese lugar."
        elif "no viable alternative" in msg:
            return "Estructura no válida según la gramática."
        else:
            return "Error de sintaxis desconocido."
    
    def suggest_correction(self, msg):
        if "mismatched input" in msg:
            return "Revisar si faltan símbolos o cerrar llaves correctamente."
        elif "extraneous input" in msg:
            return "Eliminar los símbolos extra que no son necesarios en ese contexto."
        elif "no viable alternative" in msg:
            return "Verificar si la estructura del código sigue la gramática esperada."
        else:
            return "Revisar el código en busca de errores de sintaxis."

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    try:
        tree = parser.prog()
        print("✅ Entrada válida o parcialmente válida.")
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    entradas = [
        ("=== Entrada 1 ===", "class A { int x }"),

        ("=== Entrada 2 ===", "class { int x; }"),

        ("=== Entrada 3 ===", "class B { int f() { x = 3; } }"),

        ("=== Entrada 4 ===", "class C { int f(a) { x 3; } }"),

        ("=== Entrada 5 ===", "class D { int f(a) { f(3; } }"),

        ("=== Entrada 6 ===", "class E { int f(a) { x = 3 4 5; } }"),

        ("=== Entrada 7 ===", "class F { int f(a) { x = 1; }"),

        ("=== Entrada 8 ===", "class G { x int; }"),

        ("=== Entrada 9 ===", "class H { }"),
        
        ("=== Entrada 10 ===", "class I { int f(x) { } }"),
    ]

    for titulo, texto in entradas:
        print(f"\n{titulo}")
        parse_input(texto)
