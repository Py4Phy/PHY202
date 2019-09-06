# PHY194 physics module

pi = 3.14159
h = 6.62606957e-34

def Heaviside(x):
    """Heaviside function Theta(x)"""
    if x < 0:
        return 0
    elif x > 0:
        return 1
    return 0.5