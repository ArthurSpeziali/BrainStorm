#Código criado por Arthur Speziali (https://www.githun.com/ArthurSpeziali)

from modules.Exceptions import Exceptions



with open('script.bstm') as script_file:
    script = script_file.read().replace('\n', '').replace(' ', '')

Exceptions.script = script
array_bit = [0]
home = 0
for enum, char in enumerate(script):
    if char == '>':
        if home == len(array_bit) -1:
            array_bit.append(0)
            
        home += 1
        
    if char == '<':
        if home == 0:
            raise(Exceptions(enum, -1).OutofRange)
        
        home -= 1
    