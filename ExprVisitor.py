# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stat.
    def visitStat(self, ctx:ExprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDivMod.
    def visitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Valor.
    def visitValor(self, ctx:ExprParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SumaResta.
    def visitSumaResta(self, ctx:ExprParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Compar.
    def visitCompar(self, ctx:ExprParser.ComparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assig.
    def visitAssig(self, ctx:ExprParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Function.
    def visitFunction(self, ctx:ExprParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#CallFunc.
    def visitCallFunc(self, ctx:ExprParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Ifcondition.
    def visitIfcondition(self, ctx:ExprParser.IfconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Whileoperation.
    def visitWhileoperation(self, ctx:ExprParser.WhileoperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Bloc.
    def visitBloc(self, ctx:ExprParser.BlocContext):
        return self.visitChildren(ctx)



del ExprParser