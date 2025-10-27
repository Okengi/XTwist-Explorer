from scipy.stats import pearsonr
import numpy as np

def autocorl(variabel: list, lags=50):
        rs = np.zeros(lags)
        for lag in range(1, lags):
            x = variabel[:-lag]  # alle bis zum vorletzten
            y = variabel[lag:]   # alle ab dem zweiten
            r, p_value = pearsonr(x, y)
            rs[lag-1] = r
        return rs