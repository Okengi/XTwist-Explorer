# Implementiert mit: 
# https://github.com/yinengy/Mersenne-Twister-in-Python/blob/master/MT19937.py
# dem C code aus: https://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/ARTICLES/mt.pdf
# und Chat GPT für Erläuterungen und Verständinis fragen vorallem für den C code

class MersenneTwister():
    def __init__(self, seed:int):
        # MT19937 Definiert Parameter
        (self.w, self.n, self.m, self.r) = (32, 624, 397, 31)
        self.a = 0x9908B0DF
        (self.u, self.d) = (11, 0xFFFFFFFF)
        (self.s, self.b) = (7, 0x9D2C5680)
        (self.t, self.c) = (15, 0xEFC60000)
        self.l = 18
        self.f = 1812433253

        self.MT = [0 for i in range(self.n)]
        self.MT_Seeds = [0 for i in range(self.n)]
        self.pos_index = self.n+1
        self.lower_mask = 0x7FFFFFFF #### wegen r 01111..
        self.upper_mask = 0x80000000 #### wegen r 10000..

        self.seed = seed

        self.sow_seeds()
        
    def reset(self):
        self.MT=self.MT_Seeds
        self.pos_index = self.n+1
     
    def sow_seeds(self): # inizialiseren des Zustand arrays
        self.MT[0] = self.seed & 0xffffffff 
        for i in range(1, self.n):
            self.MT[i] = (self.f * (self.MT[i-1] ^ (self.MT[i-1] >> (self.w - 2))) + i) & 0xffffffff
        
        for i in range(len(self.MT)): # Um in der Visualiserung den Seed Array zeugen zu können
            self.MT_Seeds[i] = self.MT[i]

    def twist(self): # Twist um den neuen Zustandsarray zu generieren
        for i in range(624):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1) % self.n] & self.lower_mask)
            xa = x>>1
            if(x % 2) != 0:
                xa = xa ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xa
        self.pos_index = 0
    
    def temper(self):
        if self.pos_index > self.n - 1: # Twist falls Index bei 624
            self.twist()

        y1 = self.MT[self.pos_index]
        y2 = y1 ^ ((y1 >> self.u) & self.d)
        y3 = y2 ^ ((y2 << self.s) & self.b)
        y4 = y3 ^ ((y3 << self.t) & self.c)
        y5 = y4 ^ (y4 >> 1)
        y6 = y5 & self.d

        self.pos_index += 1
        return y6
    
    def random(self):
        return self.temper() / 2**self.w # Zahl zwischen 0 und 1 generieren
    
    def randint(self, a, b):
        return a+ int(self.random()*(b-a)+1) # Ganze Zahl zwischen a und b
    

if __name__ == "__main__":
    mt = MersenneTwister(1958)
    for _ in range(10):
        print(mt.randint(0, 100))