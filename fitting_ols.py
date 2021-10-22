
"""
Name: Iris Shakya
Email: iris.shakya27@myhunter.cuny.edu
Resources: python scipy docs, inferentialthinking.com/chapters/15/2/Regression_Line.html
"""

import numpy as np
from scipy.stats import pearsonr

def compute_r_line(xes, yes):
    sd_x = np.std(xes)
    sd_y = np.std(yes)
    
    # correlation r
    r = np.mean(standard_units(xes)*standard_units(yes))
    
    # slope
    m = r*sd_x/sd_y
    
    # y-intercept
    b = yes[0]-m*xes[0]
    
    return m, b

