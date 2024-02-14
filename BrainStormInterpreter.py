#Código criado por Arthur Speziali (https://www.githun.com/ArthurSpeziali)

from modules.Exceptions import Exceptions


with open('script.bstm') as script_file:
    script = script_file.read().replace('\n', '').replace(' ', '')

Exceptions.script = script
array_bit = [0]
home = 0
lenarray = 4096
for enum, char in enumerate(script):
    if char == '>':
        if lenarray == 4096:
            raise(Exceptions(enum, 4096).OutofRange)
        
        if home == len(array_bit) -1:
            array_bit.append(0)
            
        home += 1
        
        
    elif char == '<':
        if home == 0:
            raise(Exceptions(enum, -1).OutofRange)
        
        home -= 1
        
        
    elif char == '+':
        if array_bit[home] > 127:
            array_bit[home] = 0
            
        else:
            array_bit[home] += 1
            
            
    elif char == '-':
        if array_bit[home] == 0:
            array_bit[home] = 127
            
        else:
            array_bit[home] -= 1
            
    
    elif char == '.':
        print(chr(array_bit[home]), end='')
        


print()     