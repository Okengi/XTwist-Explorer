from Linear_Congruential_Generator import LCG
from MersenneTwister import MersenneTwister
from XOR_Shift_Generator import XOR_Shift_Generator_64Bit
from scipy.stats import pearsonr
import numpy as np

generator = MersenneTwister(0)
n = 10
generated_values = [generator.random() for _ in range(n)]
rs = np.zeros(3)
for lag in range(1, 4):
    x = generated_values[:-lag]  # alle bis zum vorletzten
    y = generated_values[lag:]   # alle ab dem zweiten
    print(len(x))
    print("\n")
    r, p_value = pearsonr(x, y)
    rs[lag-1] = r

print("Korrelationskoeffizienten:", rs)