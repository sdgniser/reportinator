import numpy as np

# Functions for fitting
def lin(x, a, b):
    return a * x + b


def quad(x, a, b, c):
    return a * x**2 + b * x + c


def exp(x, a, b, c):
    return a * np.exp(b * x) + c


def log(x, a, b, c):
    return a * np.log(b * x) + c


def gauss(x, sigma, mu):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * (np.exp(-0.5 * ((x - mu) / sigma) ** 2))


def boltz(x, a, b, c):
    return ((a - b) / (1 + np.exp((x - a) / b))) + c


def txt(func, p, p_sigma):
    """
    Produces verbose latex output, after fit

    """
    text = "the equation we get after fitting is: "

    if func == "lin":
        text += f"$({p[0]:.3g} \\pm {p_sigma[0]:.3g})x + ({p[1]:.3g} \\pm {p_sigma[1]:.3g})$"

    elif func == "quad":
        text += f"$({p[0]:.3g} \\pm {p_sigma[0]:.3g})x^2 + ({p[1]:.3g} \\pm {p_sigma[1]:.3g})x + ({p[2]:.3g} \\pm {p_sigma[2]:.3g})$"

    elif func == "exp":
        text += f"$({p[0]:.3g} \\pm {p_sigma[0]:.3g})\\exp(({p[1]:.3g} \\pm {p_sigma[1]:.3g})x) + ({p[2]:.3g} \\pm {p_sigma[2]:.3g})$"
    
    elif func == "log":
        text += f"$({p[0]:.3g} \\pm {p_sigma[0]:.3g})\\ln(({p[1]:.3g} \\pm {p_sigma[1]:.3g})x) + ({p[2]:.3g} \\pm {p_sigma[2]:.3g})$"

    elif func == "gauss":
        text += f"$ (1 / (({p[0]:.3g} \\pm {p_sigma[0]:.3g}) * \\sqrt(2\\pi))) * (\\exp(-0.5((x - ({p[1]:.3g} \\pm {p_sigma[1]:.3g})) / ({p[0]:.3g} \\pm {p_sigma[0]:.3g}))^2 )) $"
    
    elif func == "boltz":
        text += f"$((({p[0]:.3g} \\pm {p_sigma[0]:.3g}) - ({p[1]:.3g} \\pm {p_sigma[1]:.3g})) / (1 + \\exp((x - ({p[0]:.3g} \\pm {p_sigma[0]:.3g})) / ({p[1]:.3g} \\pm {p_sigma[1]:.3g})))) + ({p[2]:.3g} \\pm {p_sigma[2]:.3g})$"

    return text
