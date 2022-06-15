from lexer import Lexer
from Parser import Parser
from interpetor import Interpetor

while True:
    text = input("Sentence >  ")
    lexer = Lexer(text.lower())
    tokens = lexer.genTokens()
    parser = Parser(tokens)
    tree = parser.parse()
    Interpetor(tree).output()