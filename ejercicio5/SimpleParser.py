# Generated from Simple.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\6\3\26\n\3\r\3\16\3\27")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4(\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\62\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\69\n\6\3\6\2\2\7\2\4\6\b\n\2\2")
        buf.write("\2:\2\r\3\2\2\2\4\21\3\2\2\2\6\'\3\2\2\2\b\61\3\2\2\2")
        buf.write("\n8\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17")
        buf.write("\r\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\22\7\3\2\2\22")
        buf.write("\23\7\f\2\2\23\25\7\4\2\2\24\26\5\6\4\2\25\24\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2")
        buf.write("\2\31\32\7\5\2\2\32\5\3\2\2\2\33\34\7\6\2\2\34\35\7\f")
        buf.write("\2\2\35(\7\7\2\2\36\37\7\6\2\2\37 \7\f\2\2 !\7\b\2\2!")
        buf.write("\"\7\f\2\2\"#\7\t\2\2#$\7\4\2\2$%\5\b\5\2%&\7\5\2\2&(")
        buf.write("\3\2\2\2\'\33\3\2\2\2\'\36\3\2\2\2(\7\3\2\2\2)*\5\n\6")
        buf.write("\2*+\7\7\2\2+\62\3\2\2\2,-\7\f\2\2-.\7\n\2\2./\5\n\6\2")
        buf.write("/\60\7\7\2\2\60\62\3\2\2\2\61)\3\2\2\2\61,\3\2\2\2\62")
        buf.write("\t\3\2\2\2\639\7\13\2\2\64\65\7\f\2\2\65\66\7\b\2\2\66")
        buf.write("\67\7\13\2\2\679\7\t\2\28\63\3\2\2\28\64\3\2\2\29\13\3")
        buf.write("\2\2\2\7\17\27\'\618")
        return buf.getvalue()


class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'int'", "';'", 
                     "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "ID", "WS" ]

    RULE_prog = 0
    RULE_classDef = 1
    RULE_member = 2
    RULE_stat = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "classDef", "member", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT=9
    ID=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ClassDefContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SimpleParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.classDef()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.MemberContext)
            else:
                return self.getTypedRuleContext(SimpleParser.MemberContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)




    def classDef(self):

        localctx = SimpleParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(SimpleParser.T__0)
            self.state = 16
            self.match(SimpleParser.ID)
            self.state = 17
            self.match(SimpleParser.T__1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.member()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleParser.T__3):
                    break

            self.state = 23
            self.match(SimpleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.ID)
            else:
                return self.getToken(SimpleParser.ID, i)

        def stat(self):
            return self.getTypedRuleContext(SimpleParser.StatContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = SimpleParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(SimpleParser.T__3)
                self.state = 26
                self.match(SimpleParser.ID)
                self.state = 27
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(SimpleParser.T__3)
                self.state = 29
                self.match(SimpleParser.ID)
                self.state = 30
                self.match(SimpleParser.T__5)
                self.state = 31
                self.match(SimpleParser.ID)
                self.state = 32
                self.match(SimpleParser.T__6)
                self.state = 33
                self.match(SimpleParser.T__1)
                self.state = 34
                self.stat()
                self.state = 35
                self.match(SimpleParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)


        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SimpleParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.expr()
                self.state = 40
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(SimpleParser.ID)
                self.state = 43
                self.match(SimpleParser.T__7)
                self.state = 44
                self.expr()
                self.state = 45
                self.match(SimpleParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimpleParser.INT, 0)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = SimpleParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(SimpleParser.INT)
                pass
            elif token in [SimpleParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(SimpleParser.ID)
                self.state = 51
                self.match(SimpleParser.T__5)
                self.state = 52
                self.match(SimpleParser.INT)
                self.state = 53
                self.match(SimpleParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





