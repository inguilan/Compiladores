from MiGramaticaListener import MiGramaticaListener
from MiGramaticaParser import MiGramaticaParser

class MyListener(MiGramaticaListener):

    def exitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        # Se ha encontrado un ciclo for
        print(f"Detectado un ciclo 'for' con las siguientes partes:")
        print(f"Inicialización: {ctx.inicializacion().getText()}")
        print(f"Condición: {ctx.condicion().getText()}")
        print(f"Actualización: {ctx.actualizacion().getText()}")
        print("Sentencias dentro del ciclo:")
        for stmt in ctx.sentencia():
            print(f"  - {stmt.getText()}")
        
    def exitInicializacion(self, ctx):
        print(f"Inicialización: {ctx.getText()}")

    def exitCondicion(self, ctx):
        print(f"Condición: {ctx.getText()}")

    def exitActualizacion(self, ctx):
        print(f"Actualización: {ctx.getText()}")

    def exitAssign(self, ctx):
        print(f"Asiganción detectada: {ctx.getText()}")