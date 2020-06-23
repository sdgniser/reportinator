import numpy
## linear
def lin(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g}) + ({:.3g} \\pm {:.3g})x$".format(p[1], p_sigma[1], p[0], p_sigma[0])
## polynomial
def pol2(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g}) + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})x^2$".format(p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol3(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g}) + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x^3$".format(p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol4(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g}) + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x^3 + ({:.3g} \\pm {:.3g})x^4$".format(p[4], p_sigma[4], p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol5(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g}) + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x^3 + ({:.3g} \\pm {:.3g})x^4 + ({:.3g} \\pm {:.3g})x^5$".format(p[5], p_sigma[5], p[4], p_sigma[4], p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])

## logarithm
# def log(x,a,b,c):
#     return a*(np.log(b*x)) + c

## exponential
# def expo(x,a,b,c):
#     return a*(np.exp(b*x))+ c