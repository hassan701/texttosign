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
        Scounter = 0
        while self.currentChar != None:
            if self.currentChar in WHITESPACE:
                Lcounter=0 
                self.advance()
            elif self.checkChar():
                Scounter=0
                yield self.genWord()
            elif self.currentChar in SYMBOL:
                Scounter+=1
                if Scounter>=2:
                    raise Exception(f"Two consencative Symbols:") 
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
            elif len(word) == 1:
                if word == "i" or  word == "a":
                    return Token(TokenType.Word, word)
                else:
                    raise Exception(f"Single charchter world inputed!")  
            else:
                return Token(TokenType.Word, word)
        else:
             raise Exception(f"Not a word: '{word}'")   
            
            
            
            
            
    def checkChar(self):
        if self.currentChar != None and self.currentChar in LETTER:
            return True
        else:
            return False
                



