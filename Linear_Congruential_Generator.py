# Quelle: https://en.wikipedia.org/wiki/Linear_congruential_generator

class LCG:
    """Linear congruential generator(LCG)\n m : int, > 0, Modulus\n a : int, 0 < a < m, Multiplier\n c : int, 0 <= c < m, Increment\n X_0 : int, 0 <= X_0 < m, Seed"""
    
    def __init__(self, m:int = 9,a:int = 4, c:int = 1, X_0:int = 0 ):
        self.m = m
        self.a = a
        self.c = c
        self.X = X_0
        self.P = -1
        self.X_0 = X_0
    
    def next(self):
        self.X = (self.a*self.X+ self.c) % self.m
        return self.X

    def reset(self):
        self.X = self.X_0
        self.P = -1
    
    def periodLength(self):
        if self.P >= 0:
            return self.P
        
        i = 1
        P = (self.a*self.X+ self.c) % self.m
        while self.X != P:
            P = (self.a*P+ self.c) % self.m
            i+=1
        self.P = i
        return i

if __name__ == "__main__":
    lcg = LCG()
    print(lcg.periodLength())
    print("----")
    for _ in range(lcg.periodLength()+1):
        print(lcg.next())