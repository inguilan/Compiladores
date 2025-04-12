from SimpleListener import SimpleListener

class CustomListener(SimpleListener):
    def enterClassDef(self, ctx):
        print(f"📦 Clase encontrada: {ctx.ID().getText()}")

    def enterMember(self, ctx):
        if ctx.ID() and ctx.getChildCount() == 3:  # int ID ;
            print(f"🔸 Variable declarada: {ctx.ID().getText()}")
        elif ctx.getChildCount() > 3:  # int ID (ID) { stat }
            print(f"🔹 Método encontrado: {ctx.ID(0).getText()}")

    def enterStat(self, ctx):
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '=':
            var = ctx.ID().getText()
            print(f"📝 Asignación encontrada: {var} = ...")
