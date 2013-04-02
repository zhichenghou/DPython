class AbstractExpression(object):
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        print "terminal interpret"

class NonterminalExpression(AbstractExpression):
    def interpret(self, context):
        print "nonterminal interpret"

class Context(object):
    def __init__(self, arg_string):
        self.arg_string = arg_string

def main():
    c = Context("context text")
    sentence = []
    sentence.append(NonterminalExpression())
    sentence.append(TerminalExpression())
    sentence.append(NonterminalExpression())   

    for expression in sentence:
        expression.interpret(c)

if __name__ == '__main__':
    main()