from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoopWithBody(self, ctx):
        # Detecta el ciclo for con cuerpo
        print(f"Detectado un ciclo 'for' con cuerpo:")
        print(f"Inicialización: {ctx.inicializacion().getText()}")
        print(f"Condición: {ctx.condicion().getText()}")
        print(f"Actualización: {ctx.actualizacion().getText()}")
        print("Sentencias dentro del ciclo:")
        for stmt in ctx.sentencia():
            print(f"  - {stmt.getText()}")

    def exitForLoopEmpty(self, ctx):
        # Detecta el ciclo for vacío
        print(f"Detectado un ciclo 'for' vacío:")
        print(f"Inicialización: {ctx.inicializacion().getText()}")
        print(f"Condición: {ctx.condicion().getText()}")
        print(f"Actualización: {ctx.actualizacion().getText()}")

    def exitAssign(self, ctx):
        # Detecta las asignaciones
        print(f"Asiganción detectada: {ctx.getText()}")

def main():
    input_code = input("Ingresa código: ")
    input_stream = InputStream(input_code)
    lexer = MiGramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(token_stream)

    # Generamos el árbol de sintaxis
    tree = parser.programa()
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()