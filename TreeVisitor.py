if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor
class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0

    def visitMulDivMod(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '/':
            print('  ' *  self.nivell + 'DIV(/)')
        elif l[1].getText() == '*' :
            print('  ' *  self.nivell + 'MUL(*)')
        else :
            print('  ' *  self.nivell + 'Mod(%)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitSumaResta(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '+':
            print('  ' *  self.nivell + 'MES(+)')
        else :
            print('  ' *  self.nivell + 'RES(-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              ExprParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')
