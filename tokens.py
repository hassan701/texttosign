 
from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    Word = 0
    EOS = 1
    


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self) -> str:
        return self.type.name + (f": {self.value}" if self.value != None else "")
