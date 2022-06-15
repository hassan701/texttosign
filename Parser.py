from tokens import TokenType
Dic = {"please","all done","good night","be careful","good morning","i love you","thank you", "you are welcome", "hello"}

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
        
    def raise_error(self):
        raise Exception("Invalid Syntax")
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
        
    def parse(self):
        expresstion = []
        if self.current_token == None:
            return None
        
        while self.current_token != None:
            result = self.sen()
            expresstion.append(result)
        
        
        expresstion = [i for i in expresstion if i]
        
        if not expresstion:
            self.raise_error()
        
        for i in expresstion:
            if i not in Dic:
                raise Exception (f"Pharse currnet not in database: '{i}'") 
        return expresstion
    
    def sen(self):
        sentence = ""
        while self.current_token != None:
            if(self.current_token.type == TokenType.EOS):
                self.advance()
                break
            else:
                sentence+= f" {self.current_token.value}"
                self.advance()
        return sentence.lstrip()
        
        
    
    
        
