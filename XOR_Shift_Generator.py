import numpy as np

class XOR_Shift_Generator_64Bit:

    def __init__(self, seed = 0):
        self.A = 21
        self.B = 15
        self.C = 29
        self.mask = (1 << 64)-1
        if seed == None or seed == 0:
            self.Seed = 1
            self.S = 1 & self.mask
        else:
            self.Seed = seed
            self.S = seed & self.mask
        

    def test(self):
        print(self.S)
        print(format(self.S, "064b"))
        self.S = (self.S ^ (self.S << self.A)) & self.mask
        print(self.S)
        print(format(self.S, "064b"))
        self.S = (self.S^(self.S >> self.B)) & self.mask
        print(f"B: {self.S}")
        print(format(self.S, "064b"))
        self.S = (self.S^(self.S<<self.C)) & self.mask
        print(self.S)
        print(format(self.S, "064b"))
    
    def shift(self):
        self.S = (self.S ^ (self.S << self.A)) & self.mask
        self.S = (self.S^(self.S >> self.B)) & self.mask
        self.S = (self.S^(self.S<<self.C)) & self.mask
    
    def random_uint64(self):
        self.shift()
        return self.S

    
    def random(self):
        return self.random_uint64() / float(1 << 64)

if __name__ == "__main__":
    xor = XOR_Shift_Generator_64Bit(0)
    for i in range(10):
        print(xor.random())