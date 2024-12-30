class Tolerancia:
    def __init__(self, x, tol_minima=3, tol_maxima=6):
        self.x = x
        self.tol_minima = tol_minima
        self.tol_maxima = tol_maxima
    def __eq__(self, outro):
        return abs(self.x - outro.x) <= self.tol_minima
    def __ne__(self, outro):
        return abs(self.x - outro.x) >= self.tol_maxima
a = Tolerancia(x=10)
b = Tolerancia(x=15)
print(a==b, a!=b)