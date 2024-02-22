# Código criado por Arthur Speziali (https://www.githun.com/ArthurSpeziali)

from modules.Exceptions import Exceptions

with open('script.bstm') as script_file:
    script = script_file.read().replace('\n', '').replace(' ', '')

Exceptions.script = script
array_bit = [0]
home = 0
item = 0
while item < len(script):
    char = script[item]
    
    if char == '>':
        if len(array_bit) == 4096:
            raise(Exceptions(item, 4096).OutofRange)
        
        if home == len(array_bit) -1:
            array_bit.append(0)
            
        home += 1
        
        
    elif char == '<':
        if home == 0:
            raise(Exceptions(item, -1).OutofRange)
        
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
        
        
    elif char == ',':
        char_bit = input()
        
        if len(char_bit) > 1:
            raise(Exceptions(item, len(char_bit)).MultipleCharByte)
        
    
        if ord(char_bit) > 126:
            raise(Exceptions(item, ord(char_bit)).NoAsciiChar)
            
        array_bit[home] = ord(char_bit)

    
    elif char == '[':
        
        if not ']' in script[item:]:
            raise(Exceptions(item, 0).NotOpenorCloseBrackets)
        
        if '[' in script[item + 1: script.find(']')]:
            raise(Exceptions(item).DoubleLoop)
        
        
        last = array_bit[home]
        if array_bit[home] == 0:
            item = script.find(']', item)            
        
        
    elif char == ']':
        if not '[' in script[: item]:
            raise(Exceptions(item, 1).NotOpenorCloseBrackets)
            
        if array_bit[home] >= last:
            raise(Exceptions(item).InfinityLoop)
            
        if array_bit[home] > 0:
            item = script[:item].rfind('[')
        
        
    item += 1
    
print()     