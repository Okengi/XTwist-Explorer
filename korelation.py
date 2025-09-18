from Linear_Congruential_Generator import LCG
from MersenneTwister import MersenneTwister
from scipy.stats import pearsonr

lcg = MersenneTwister()
n = 100
lcg_werte = [lcg.random() for _ in range(n)]
x = lcg_werte[:-1]  # alle bis zum vorletzten
y = lcg_werte[1:]   # alle ab dem zweiten


r, p_value = pearsonr(x, y)
print("Korrelationskoeffizient:", r)