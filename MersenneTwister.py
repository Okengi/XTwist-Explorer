class MersenneTwister():
    def __init__(self, seed:int=0):
        # MT19937
        (self.w, self.n, self.m, self.r) = (32, 624, 397, 31)
        self.a = 0x9908B0DF
        (self.u, self.d) = (11, 0xFFFFFFFF)
        (self.s, self.b) = (7, 0x9D2C5680)
        (self.t, self.c) = (15, 0xEFC60000)
        self.l = 18
        self.f = 1812433253

        self.MT = [0 for i in range(self.n)]
        self.pos_index = self.n+1
        self.lower_mask = 0x7FFFFFFF
        self.upper_mask = 0x80000000

        self.seed = seed
        self.grow_input_seed()
        self.sow_seeds()
        
     
    def grow_input_seed(self):
        self.g0 = self.seed
        for i in range(51):
            self.g0 = 69069 * self.g0 + 1 
        
    def sow_seeds(self):
        for i in range(623):
            self.g0 = 69069 * self.g0 + 1
            self.MT[i] = self.g0&0xffffffff

    def twist(self):
        # 
        for i in range(263):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1) % self.n] & self.lower_mask)
            xa = x>>1
            if(x % 2) != 0:
                xa = xa ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xa
        self.pos_index = 0
    
    def temper(self):
        if self.pos_index > self.n:
            self.twist()
        y1 = self.MT[self.pos_index]
        y2 = y1 ^ ((y1 >> self.u) & self.d)
        y3 = y2 ^ ((y2 << self.s) & self.b)
        y4 = y3 ^ ((y3 << self.t) & self.c)
        y5 = y4 ^ (y4 >> 1)
        y6 = y5 & self.d

        self.pos_index += 1
        return y6
    
    def get_item(self):
        return self.temper()

    def get_items(self, amount):
        return [self.temper() for _ in range(amount)]
    
    def random(self):
        return self.temper() / 2**self.w
    
    def randint(self, a, b):
        return int(self.random()*(b-a)+a)
    


mt = MersenneTwister(1958)
for _ in range(10):
    print(mt.randint(0, 100))