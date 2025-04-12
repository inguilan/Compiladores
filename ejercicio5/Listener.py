from SimpleListener import SimpleListener

class ClaseMetodoAsignacionListener(SimpleListener):
    def enterClassDef(self, ctx):
        # Accedemos al primer identificador (el nombre de la clase)
        class_name = ctx.ID().getText() if ctx.ID() else "<sin nombre>"
        print(f"Clase: {class_name}")

    def enterMember(self, ctx):
        # Verificamos si el miembro tiene más de un identificador, indicando un método
        if ctx.getChildCount() > 2 and ctx.getChild(2).getText() == '(':
            # Si hay múltiples IDs, tomamos el primer identificador
            method_name = ctx.ID()[0].getText() if ctx.ID() else "<sin nombre>"
            print(f"Método: {method_name}")

    def enterStat(self, ctx):
        # Verificamos si se trata de una asignación (ID = expr)
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '=':
            var_name = ctx.getChild(0).getText()  # El primer hijo es la variable
            print(f"Asignación: {var_name} = ...")
