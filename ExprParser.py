# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\5\4\'\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\7\7>\n\7\f\7\16\7A")
        buf.write("\13\7\3\7\3\7\3\b\3\b\7\bG\n\b\f\b\16\bJ\13\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\tQ\n\t\3\n\3\n\3\n\3\n\3\13\3\13\6\13Y")
        buf.write("\n\13\r\13\16\13Z\3\13\3\13\3\13\2\3\6\f\2\4\6\b\n\f\16")
        buf.write("\20\22\24\2\5\3\2\3\5\3\2\6\7\3\2\b\r\2b\2\26\3\2\2\2")
        buf.write("\4!\3\2\2\2\6&\3\2\2\2\b\63\3\2\2\2\n\67\3\2\2\2\f;\3")
        buf.write("\2\2\2\16D\3\2\2\2\20K\3\2\2\2\22R\3\2\2\2\24V\3\2\2\2")
        buf.write("\26\27\5\4\3\2\27\30\7\2\2\3\30\3\3\2\2\2\31\"\5\n\6\2")
        buf.write("\32\"\5\b\5\2\33\"\5\6\4\2\34\"\5\20\t\2\35\"\5\22\n\2")
        buf.write("\36\"\5\f\7\2\37\"\5\16\b\2 \"\5\24\13\2!\31\3\2\2\2!")
        buf.write("\32\3\2\2\2!\33\3\2\2\2!\34\3\2\2\2!\35\3\2\2\2!\36\3")
        buf.write("\2\2\2!\37\3\2\2\2! \3\2\2\2\"\5\3\2\2\2#$\b\4\1\2$\'")
        buf.write("\7\24\2\2%\'\7\26\2\2&#\3\2\2\2&%\3\2\2\2\'\60\3\2\2\2")
        buf.write("()\f\6\2\2)*\t\2\2\2*/\5\6\4\7+,\f\5\2\2,-\t\3\2\2-/\5")
        buf.write("\6\4\6.(\3\2\2\2.+\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63\64\5\6\4\2\64")
        buf.write("\65\t\4\2\2\65\66\5\6\4\2\66\t\3\2\2\2\678\7\26\2\289")
        buf.write("\7\16\2\29:\5\6\4\2:\13\3\2\2\2;?\7\25\2\2<>\7\26\2\2")
        buf.write("=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3")
        buf.write("\2\2\2BC\5\24\13\2C\r\3\2\2\2DH\7\25\2\2EG\5\6\4\2FE\3")
        buf.write("\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\17\3\2\2\2JH\3\2")
        buf.write("\2\2KL\7\17\2\2LM\5\b\5\2MP\5\24\13\2NO\7\20\2\2OQ\5\24")
        buf.write("\13\2PN\3\2\2\2PQ\3\2\2\2Q\21\3\2\2\2RS\7\21\2\2ST\5\b")
        buf.write("\5\2TU\5\24\13\2U\23\3\2\2\2VX\7\22\2\2WY\5\4\3\2XW\3")
        buf.write("\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7\23")
        buf.write("\2\2]\25\3\2\2\2\n!&.\60?HPZ")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'>'", 
                     "'<'", "'>='", "'<='", "'='", "'!='", "'<-'", "'if'", 
                     "'else'", "'while'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "FUNCNAME", "VAR", 
                      "WS" ]

    RULE_root = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_comp = 3
    RULE_asign = 4
    RULE_func = 5
    RULE_callfunc = 6
    RULE_condicional = 7
    RULE_whileCondition = 8
    RULE_blocop = 9

    ruleNames =  [ "root", "stat", "expr", "comp", "asign", "func", "callfunc", 
                   "condicional", "whileCondition", "blocop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    NUM=18
    FUNCNAME=19
    VAR=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(ExprParser.StatContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.stat()
            self.state = 21
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asign(self):
            return self.getTypedRuleContext(ExprParser.AsignContext,0)


        def comp(self):
            return self.getTypedRuleContext(ExprParser.CompContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def condicional(self):
            return self.getTypedRuleContext(ExprParser.CondicionalContext,0)


        def whileCondition(self):
            return self.getTypedRuleContext(ExprParser.WhileConditionContext,0)


        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def callfunc(self):
            return self.getTypedRuleContext(ExprParser.CallfuncContext,0)


        def blocop(self):
            return self.getTypedRuleContext(ExprParser.BlocopContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.asign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.comp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.whileCondition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.func()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 29
                self.callfunc()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 30
                self.blocop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ValorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.NUM]:
                localctx = ExprParser.ValorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 34
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.VAR]:
                localctx = ExprParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(ExprParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulDivModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 39
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__1) | (1 << ExprParser.T__2))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.SumaRestaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.T__3 or _la==ExprParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(4)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_comp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompar" ):
                return visitor.visitCompar(self)
            else:
                return visitor.visitChildren(self)



    def comp(self):

        localctx = ExprParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comp)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.ComparContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.expr(0)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__5) | (1 << ExprParser.T__6) | (1 << ExprParser.T__7) | (1 << ExprParser.T__8) | (1 << ExprParser.T__9) | (1 << ExprParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 51
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_asign

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssigContext(AsignContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AsignContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)



    def asign(self):

        localctx = ExprParser.AsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asign)
        try:
            localctx = ExprParser.AssigContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.VAR)
            self.state = 54
            self.match(ExprParser.T__11)
            self.state = 55
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNCNAME(self):
            return self.getToken(ExprParser.FUNCNAME, 0)
        def blocop(self):
            return self.getTypedRuleContext(ExprParser.BlocopContext,0)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAR)
            else:
                return self.getToken(ExprParser.VAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.FunctionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.FUNCNAME)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.VAR:
                self.state = 58
                self.match(ExprParser.VAR)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.blocop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_callfunc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CallFuncContext(CallfuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CallfuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNCNAME(self):
            return self.getToken(ExprParser.FUNCNAME, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunc" ):
                return visitor.visitCallFunc(self)
            else:
                return visitor.visitChildren(self)



    def callfunc(self):

        localctx = ExprParser.CallfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_callfunc)
        try:
            localctx = ExprParser.CallFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ExprParser.FUNCNAME)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.expr(0) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_condicional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfconditionContext(CondicionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondicionalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comp(self):
            return self.getTypedRuleContext(ExprParser.CompContext,0)

        def blocop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlocopContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlocopContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfcondition" ):
                return visitor.visitIfcondition(self)
            else:
                return visitor.visitChildren(self)



    def condicional(self):

        localctx = ExprParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.IfconditionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ExprParser.T__12)
            self.state = 74
            self.comp()
            self.state = 75
            self.blocop()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.T__13:
                self.state = 76
                self.match(ExprParser.T__13)
                self.state = 77
                self.blocop()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_whileCondition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileoperationContext(WhileConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.WhileConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comp(self):
            return self.getTypedRuleContext(ExprParser.CompContext,0)

        def blocop(self):
            return self.getTypedRuleContext(ExprParser.BlocopContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileoperation" ):
                return visitor.visitWhileoperation(self)
            else:
                return visitor.visitChildren(self)



    def whileCondition(self):

        localctx = ExprParser.WhileConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileCondition)
        try:
            localctx = ExprParser.WhileoperationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ExprParser.T__14)
            self.state = 81
            self.comp()
            self.state = 82
            self.blocop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlocopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_blocop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlocContext(BlocopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BlocopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloc" ):
                return visitor.visitBloc(self)
            else:
                return visitor.visitChildren(self)



    def blocop(self):

        localctx = ExprParser.BlocopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blocop)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.BlocContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ExprParser.T__15)
            self.state = 86 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self.stat()
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__12) | (1 << ExprParser.T__14) | (1 << ExprParser.T__15) | (1 << ExprParser.NUM) | (1 << ExprParser.FUNCNAME) | (1 << ExprParser.VAR))) != 0)):
                    break

            self.state = 90
            self.match(ExprParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




