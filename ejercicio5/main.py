from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from ejercicio5.Listener import CustomListener  

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

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
        
        # 🎧 Listener para imprimir clases, métodos y asignaciones
        listener = CustomListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("class A { int x; }")

    print("\n=== Entrada con error 1 ===")
    parse_input("class B { int f(x) { a = 3 4 5; } }")

    print("\n=== Entrada con error 2 ===")
    parse_input("class C { int f(x) { a = 3 + 5; } }")

    print("\n=== Entrada con error 3 ===")
    parse_input("class G { int f(x) { a =5; } }")

    print("\n=== Entrada válida 4 ===")
    parse_input("class H { int z; int calc(int a, int b) { z = a + b * 3 - 4; } }")

    print("\n=== Entrada válida 5 ===")
    parse_input("class I { int x; int foo(int y) { x = foo(10); } }")

    print("\n=== Entrada con error 4 ===")
    parse_input("class J { int x; int calc(int a, b { x = a + b; } }")

    print("\n=== Entrada con error 5 ===")
    parse_input("class K { int y; int wrong(int a) { y = 3 + * 5; } }")
