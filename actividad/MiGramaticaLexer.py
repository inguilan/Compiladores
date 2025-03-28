# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\7\21")
        buf.write("L\n\21\f\21\16\21O\13\21\3\22\6\22R\n\22\r\22\16\22S\3")
        buf.write("\23\6\23W\n\23\r\23\16\23X\3\23\3\23\2\2\24\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\3\2\6\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\3\2\62;\5\2\13\f\17\17\"\"\2^\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2")
        buf.write("\5+\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\63\3")
        buf.write("\2\2\2\17\65\3\2\2\2\21\67\3\2\2\2\239\3\2\2\2\25;\3\2")
        buf.write("\2\2\27>\3\2\2\2\31A\3\2\2\2\33C\3\2\2\2\35E\3\2\2\2\37")
        buf.write("G\3\2\2\2!I\3\2\2\2#Q\3\2\2\2%V\3\2\2\2\'(\7h\2\2()\7")
        buf.write("q\2\2)*\7t\2\2*\4\3\2\2\2+,\7*\2\2,\6\3\2\2\2-.\7=\2\2")
        buf.write(".\b\3\2\2\2/\60\7+\2\2\60\n\3\2\2\2\61\62\7}\2\2\62\f")
        buf.write("\3\2\2\2\63\64\7\177\2\2\64\16\3\2\2\2\65\66\7?\2\2\66")
        buf.write("\20\3\2\2\2\678\7@\2\28\22\3\2\2\29:\7>\2\2:\24\3\2\2")
        buf.write("\2;<\7?\2\2<=\7?\2\2=\26\3\2\2\2>?\7#\2\2?@\7?\2\2@\30")
        buf.write("\3\2\2\2AB\7,\2\2B\32\3\2\2\2CD\7\61\2\2D\34\3\2\2\2E")
        buf.write("F\7-\2\2F\36\3\2\2\2GH\7/\2\2H \3\2\2\2IM\t\2\2\2JL\t")
        buf.write("\3\2\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\"\3\2")
        buf.write("\2\2OM\3\2\2\2PR\t\4\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2")
        buf.write("ST\3\2\2\2T$\3\2\2\2UW\t\5\2\2VU\3\2\2\2WX\3\2\2\2XV\3")
        buf.write("\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\23\2\2[&\3\2\2\2\6\2MS")
        buf.write("X\3\b\2\2")
        return buf.getvalue()


class MiGramaticaLexer(Lexer):

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
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    ID = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'for'", "'('", "';'", "')'", "'{'", "'}'", "'='", "'>'", "'<'", 
            "'=='", "'!='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "ID", "INT", "WS" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


