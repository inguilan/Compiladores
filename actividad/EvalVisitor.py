from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

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
    
    def visitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        # Ejecutamos la inicialización
        self.visit(ctx.inicializacion())
        
        # Simulamos el ciclo for
        while self.visit(ctx.condicion()):
            # Ejecutamos las sentencias dentro del ciclo
            for stmt in ctx.sentencia():
                self.visit(stmt)
            
            # Realizamos la actualización del for
            self.visit(ctx.actualizacion())

    def visitCondicion(self, ctx: MiGramaticaParser.CondicionContext):
        left = self.variables.get(ctx.ID().getText(), 0)
        right = int(ctx.INT().getText())
        op = ctx.op.text
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