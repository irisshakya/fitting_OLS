"""
Name: Iris Shakya
Email: iris.shakya27@myhunter.cuny.edu
Resources: python scipy docs, machine learning mastery
"""

import numpy as np
from scipy.stats import pearsonr


def compute_r_line(xes, yes):
    sd_x = np.std(xes)
    sd_y = np.std(yes)
    
    # correlation r
    r,_ = pearsonr(xes, yes)
    
    # slope
    m = r*sd_y/sd_x
    
    # y-intercept
    b = yes[0]-m*xes[0]
    
    return m, b
