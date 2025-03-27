# Task: Caesar Cipher Helper

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift % 26
    
    def shift_s(self, s, is_encode):
        if ord(s) > 90 or ord(s) < 65:
            return s
        if is_encode:
            return chr(ord(s) + self.shift - 26) if ord(s) + self.shift > 90 else chr(ord(s) + self.shift)
        else:
            return chr(ord(s) - self.shift + 26) if ord(s) - self.shift < 65 else chr(ord(s) - self.shift)
        
    def encode(self, st):
        return ''.join([ self.shift_s(s, True) for s in st.upper() ])   
        
    def decode(self, st):
        return ''.join([ self.shift_s(s, False) for s in st.upper() ])
    

'''
# Best Solution in codewars

# 1
class CaesarCipher(object):
    def __init__(self, shift):
       self.shift = shift

    def encode(self, s):
        return self.cypher(s, self.shift)
        
    def decode(self, s):
        return self.cypher(s, -self.shift)
        
    def cypher(self, s, d):
        return "".join([chr(65 + (ord(c) - 65 + d) % 26) if c.isalpha() else c for c in s.upper()])

# 2
class CaesarCipher(object):
    def __init__(self, shift):
        self.s=shift
        pass;

    def encode(self, str):
        return ''.join(chr((ord(i)+self.s-ord('A'))%26+ord('A')) if i.isalpha() else i for i in str.upper())
        
    def decode(self, str):
        return ''.join(chr((ord(i)-self.s+ord('A'))%26+ord('A')) if i.isalpha() else i for i in str.upper())

# 3
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class CaesarCipher(object):
    def __init__(self, shift):
        self.s = shift

    def encode(self, st):
        return ''.join(alp[(alp.index(i)+self.s)%26] if i in alp else i for i in st.upper())
        
    def decode(self, st):
        return ''.join(alp[(alp.index(i)-self.s)%26] if i in alp else i for i in st.upper())        
'''