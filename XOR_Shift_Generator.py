class XOR_Shift_Generator_64Bit:

    def __init__(self, seed = 1, a = 21, b = 15, c = 29):
        self.A = a
        self.B = b
        self.C = c
        self.mask = (1 << 64)-1
        
        self.Seed = seed & self.mask
        self.S = seed & self.mask
    
    def shift(self):
        self.S = (self.S ^ (self.S << self.A)) & self.mask
        self.S = (self.S^(self.S >> self.B)) & self.mask
        self.S = (self.S^(self.S<<self.C)) & self.mask
    
    def random_uint64(self):
        self.shift()
        return self.S

    
    def random(self):
        return self.random_uint64() / float(1 << 64)
    

class XOR_Shift_Generator_32Bit:

    def __init__(self, seed = 1, a = 13, b = 17, c = 5):
        self.A = a
        self.B = b
        self.C = c
        self.mask = (1 << 32) - 1
        
        self.Seed = seed & self.mask
        self.S = seed & self.mask
    
    def shift(self):
        self.S = (self.S ^ (self.S << self.A)) & self.mask
        self.S = (self.S ^ (self.S >> self.B)) & self.mask
        self.S = (self.S ^ (self.S << self.C)) & self.mask
    
    def random_uint32(self):
        self.shift()
        return self.S
    
    def random(self):
        return self.random_uint32() / float((1 << 32) - 1)

if __name__ == "__main__":
    x = 5
    seed = 123
    xor = XOR_Shift_Generator_64Bit(seed)
    print("--- 64 Bit ---")
    print(f"Erste {x} Zufallszahlen:")
    for i in range(x):
        print(f"{i+1}: {xor.random()}")
    xor = XOR_Shift_Generator_32Bit(seed)
    print("--- 32 Bit ---")
    print(f"Erste {x} Zufallszahlen:")
    for i in range(x):
        print(f"{i+1}: {xor.random()}")