# fitting_OLS
 
Write a function, compute_r_line(), that takes two iterables of numeric values representing the independent variable (xes) and the dependent variable (yes) and computes the slope and y-intercept of the linear regression line using ordinary least squares. See DS 8: Chapter 15 The pseudocode for this:

Compute the standard deviation of the xes and yes. Call these sd_x and sd_y.
Compute the correlation, r, of the xes and yes.
Compute the slope, m, as m = r*sd_y/sd_x.
Compute the y-intercept, b, as b = yes[0] - m * xes[0]
Return m and b.
