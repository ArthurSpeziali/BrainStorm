class Exceptions:
    def __init__(self, index, code=0):
        line = self.ExceptionMaker(index)
        
        self.OutofRange = Exception(f'Array Out of Range[{code}]{line}')
        
    def ExceptionMaker(self, index):
        line = '\n\n'
        
        line += self.script[index - 5: index]
        line += f'\033[31m{self.script[index]}\033[m'
        line += self.script[index + 1: index + 6]
        
        line += '\n'
        line += 5 * ' ' + '↑'
                
        return line