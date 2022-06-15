from tokens import Token, TokenType
import string
import enchant

WHITESPACE = " \n\t"
LETTER = string.ascii_lowercase + "_-'"
CONJUNCTION = ["and","or", 'so']
SYMBOL = ".,?!"
NUMBERS = ""

class Lexer:
    def __init__(self,text):
        self.text = iter(text)
        self.advance()
        self.dic =  enchant.Dict("en_us")

    def advance(self):
        try:
            self.currentChar = next(self.text)
        except StopIteration:
            self.currentChar = None
    
    
    
    def genTokens(self):
        while self.currentChar != None:
            if self.currentChar in WHITESPACE:
                self.advance()
            elif self.checkChar():
                yield self.genWord()
            elif self.currentChar in SYMBOL:
                yield Token(TokenType.EOS)
                self.advance()
            else:
                raise Exception(f"Illigal Char: '{self.currentChar}'")
                
                
    def genWord(self):
        word = self.currentChar
        self.advance()
        while self.checkChar():
            if self.currentChar in SYMBOL:
                break
            word += self.currentChar
            self.advance()
            
        
        if self.dic.check(word):
            if word in CONJUNCTION:
                return Token(TokenType.EOS, word)
            else:
                return Token(TokenType.Word, word)
        else:
             raise Exception(f"Not a word: '{word}'")   
            
            
            
            
            
    def checkChar(self):
        if self.currentChar != None and self.currentChar in LETTER:
            return True
        else:
            return False
                



