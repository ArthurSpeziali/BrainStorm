class Exceptions:
    def __init__(self, index, code=0):
        line = self.ExceptionMaker(index)
        
        self.OutofRange = Exception(f'Byte out of range[{code}]{line}')
        self.MultipleCharByte = Exception(f'Multiple characters in one byte[{code}]{line}')
        self.NoAsciiChar = Exception(f'Character is not in ascii-utf8(256b) table[{code}]{line}')
        self.NotOpenorCloseBrackets = Exception(f"Bracket's were never opened or closed[{code}]{line}")
        self.DoubleLoop = Exception(f'Loop within another loop[{code}]{line}')
        self.InfinityLoop = Exception(f'Loop that never ends[{code}]{line}')
        self.CharNull = Exception(f'Character null is not allowed[{code}]{line}')
        self.CharOutofRange = Exception(f'Character array exceeded limit[{code}]{line}')
        self.CharExceededArray = Exception(f'Character array exceeded main array[{code}]{line}')
        
    def ExceptionMaker(self, index):
        line = '\n\n'
        line += f'Character: \033[33;1m{index + 1}\033[m'
        line += '\n'
        
        if index < 5:
            start = index
            
        else:
            start = 5
        
        line += '\033[32m' + self.script[index - start: index] + '\033[m'
        line += f'\033[31m{self.script[index]}\033[m'
        line += '\033[32m' + self.script[start + 1: index + 6] + '\033[m'
        
        line += '\n'
        line += 5 * ' ' + '↑'
                
        return line