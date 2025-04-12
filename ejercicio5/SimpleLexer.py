# Generated from Simple.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\61\n\n\r\n\16\n\62\3\13")
        buf.write("\6\13\66\n\13\r\13\16\13\67\3\f\6\f;\n\f\r\f\16\f<\3\f")
        buf.write("\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2B\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\37\3\2\2")
        buf.write("\2\7!\3\2\2\2\t#\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17+\3")
        buf.write("\2\2\2\21-\3\2\2\2\23\60\3\2\2\2\25\65\3\2\2\2\27:\3\2")
        buf.write("\2\2\31\32\7e\2\2\32\33\7n\2\2\33\34\7c\2\2\34\35\7u\2")
        buf.write("\2\35\36\7u\2\2\36\4\3\2\2\2\37 \7}\2\2 \6\3\2\2\2!\"")
        buf.write("\7\177\2\2\"\b\3\2\2\2#$\7k\2\2$%\7p\2\2%&\7v\2\2&\n\3")
        buf.write("\2\2\2\'(\7=\2\2(\f\3\2\2\2)*\7*\2\2*\16\3\2\2\2+,\7+")
        buf.write("\2\2,\20\3\2\2\2-.\7?\2\2.\22\3\2\2\2/\61\t\2\2\2\60/")
        buf.write("\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\24\3\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67\65\3\2\2\2\678\3\2\2\28\26\3\2\2\29;\t\4\2\2:9\3\2")
        buf.write("\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\b\f\2\2")
        buf.write("?\30\3\2\2\2\6\2\62\67<\3\b\2\2")
        return buf.getvalue()


class SimpleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INT = 9
    ID = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'}'", "'int'", "';'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INT", "ID", "WS" ]

    grammarFileName = "Simple.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


