# Generated from Simple.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#prog.
    def enterProg(self, ctx:SimpleParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleParser#prog.
    def exitProg(self, ctx:SimpleParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleParser#classDef.
    def enterClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass

    # Exit a parse tree produced by SimpleParser#classDef.
    def exitClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass


    # Enter a parse tree produced by SimpleParser#member.
    def enterMember(self, ctx:SimpleParser.MemberContext):
        pass

    # Exit a parse tree produced by SimpleParser#member.
    def exitMember(self, ctx:SimpleParser.MemberContext):
        pass


    # Enter a parse tree produced by SimpleParser#stat.
    def enterStat(self, ctx:SimpleParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleParser#stat.
    def exitStat(self, ctx:SimpleParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleParser#expr.
    def enterExpr(self, ctx:SimpleParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleParser#expr.
    def exitExpr(self, ctx:SimpleParser.ExprContext):
        pass



del SimpleParser