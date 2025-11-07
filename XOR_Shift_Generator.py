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
    
    def random_uint32(self):# die ganze generierte Zahl zurück geben
        self.shift()
        return self.S
    
    def random(self):
        return self.random_uint32() / float((1 << 32) - 1) # flaot zwischen 0 und 1 zurück geben
    
    def randint(self, a, b): # Ganze zahl zwischen a und b
        return a + int(self.random() * (b - a + 1)) # Falls sie das lesen probieren sie doch gerne einmal im xor_tab die Zahlen mit dieser function zu generienen sieht witzig aus

if __name__ == "__main__":
    x = 5
    seed = 123
    xor = XOR_Shift_Generator_32Bit(seed)
    
    for i in range(10):
        print(xor.randint(5, 10))
    