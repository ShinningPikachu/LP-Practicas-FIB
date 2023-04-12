if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.funcDicParametre={}
        self.funcDicOperacio={}
        self.funcVarDic = [{}]

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    def visitMulDivMod(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '/':
            return self.visit(l[0]) // self.visit(l[2])
        elif l[1].getText() == '*' :
            return self.visit(l[0]) * self.visit(l[2])
        else :
            return self.visit(l[0]) % self.visit(l[2])

    def visitSumaResta(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '+':
            return self.visit(l[0]) + self.visit(l[2])
        else:
            return self.visit(l[0]) - self.visit(l[2])

    def visitCompar(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '=':
            return self.visit(l[0]) == self.visit(l[2])
        elif l[1].getText() == '!=':
            return self.visit(l[0]) != self.visit(l[2])
        elif l[1].getText() == '>=':
            return self.visit(l[0]) >= self.visit(l[2])
        elif l[1].getText() == '<=':
            return self.visit(l[0]) <= self.visit(l[2])
        elif l[1].getText() == '>':
            return self.visit(l[0]) > self.visit(l[2])
        elif l[1].getText() == '<':
            return self.visit(l[0]) < self.visit(l[2])

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        self.funcVarDic[-1][l[0].getText()]=self.visit(l[2])


    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        return self.funcVarDic[-1][l[0].getText()]

    def visitIfcondition(self, ctx):
        l = list(ctx.getChildren())
        IsTrue = self.visit(l[1])
        if IsTrue :
            return self.visit(l[2])
        if len(l) > 3 and not IsTrue :
            return self.visit(l[4])

    def visitWhileoperation(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            self.visit(l[2])

    def visitFunction(self, ctx):
        l = list(ctx.getChildren())
        counter = 1
        llista = []
        while counter < len(l)-1:
            llista.insert(0,l[counter].getText())
            counter = counter + 1
        self.funcDicParametre[l[0].getText()] = llista
        self.funcDicOperacio[l[0].getText()] = l[-1]

    def visitCallFunc(self, ctx):
        l = list(ctx.getChildren())
        listOfVars = {}
        counter = 1
        for i in self.funcDicParametre[l[0].getText()]:
            listOfVars[i] = int(l[counter].getText())
            print(counter)
            counter = counter + 1
        self.funcVarDic.append(listOfVars)
        return self.visit(self.funcDicOperacio[l[0].getText()])

    def visitBloc(self, ctx):
        l = list(ctx.getChildren())
        counter = 1
        while counter < len(l)-1:
            return self.visit(l[counter]);
            counter = counter + 1
