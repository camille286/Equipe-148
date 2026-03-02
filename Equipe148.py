import math
from Bissection import Bissection
from pointfixe import pointfixe


def F(Q):
    return math.exp(Q) + Q/2 - 5

# BISSECTION

n = 18  # nombre d’itérations déterminé à la question b)

X = Bissection(F, 1, 2, tol=1e-6, nmax=100)

Qn  = X[n-1]
Qn1 = X[n]

print("\nRésultats de la méthode de la bissection")
print("------------------------------------------")
print(f"Q{n} = {Qn:.16f}")
print(f"|Q{n+1} - Q{n}| = {abs(Qn1 - Qn):.16e}")
print(f"Q{n} (5 chiffres significatifs) = {format(Qn, '.5g')}")

# POINTS FIXES

def g1(Q):
    return math.log(5 - Q/2)

def g2(Q):
    return 10 - 2*math.exp(Q)

#  NEWTON

def dF(Q):
    return math.exp(Q) + 0.5

def gN(Q):
    return Q - F(Q)/dF(Q)

# TABLEAUX

def print_table(iterations, title, max_rows=None):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))
    print("n\tQn\t\t\t|en|\t\t\t|en+1/en|\t\t|en+1/e_n^2|\t\t|en+1/e_n^3|")

    N = len(iterations) - 1
    if max_rows is None:
        max_rows = N

    for n in range(0, min(max_rows, N) + 1):
        Qn = iterations[n]

        if n == 0:
            print(f"{n}\t{Qn:.16f}\t-\t\t\t-\t\t\t-\t\t\t-")
            continue

        en = abs(iterations[n] - iterations[n-1])

        if n < N:
            en1 = abs(iterations[n+1] - iterations[n])
            r1 = en1/en if en != 0 else float("inf")
            r2 = en1/(en**2) if en != 0 else float("inf")
            r3 = en1/(en**3) if en != 0 else float("inf")

            print(f"{n}\t{Qn:.16f}\t{en:.9e}\t{r1:.6g}\t\t{r2:.6g}\t\t{r3:.6g}")
        else:
            print(f"{n}\t{Qn:.16f}\t{en:.9e}\t-\t\t\t-\t\t\t-")


Q0 = 1
tolr = 1e-8
nmax = 150

it_g1 = pointfixe(g1, Q0, tolr, nmax)
print_table(
    it_g1,
    "TABLEAU 1 — Convergence de la méthode de points fixes appliquée à g1(Q) = ln(5 - Q/2)"
)

it_g2 = pointfixe(g2, Q0, tolr, nmax)
print_table(
    it_g2,
    "TABLEAU 2 — Divergence de la méthode de points fixes appliquée à g2(Q) = 10 - 2 e^Q (5 premières itérations)",
    5
)

it_gN = pointfixe(gN, Q0, tolr, nmax)
print_table(
    it_gN,
    "TABLEAU 3 — Convergence de la méthode de Newton via point fixe gN(Q)"
)

#STEFFENSEN

def steffensen_transform(g):
    def gSteff(Q):
        y = g(Q)
        z = g(y)
        denom = z - 2*y + Q
        if denom == 0:
            return y
        return Q - (y - Q)**2 / denom
    return gSteff

gSteff1 = steffensen_transform(g1)
gSteff2 = steffensen_transform(g2)
gSteffN = steffensen_transform(gN)

it_steff_g1 = pointfixe(gSteff1, Q0, tolr, nmax)
print_table(
    it_steff_g1,
    "TABLEAU 4 — Application de la méthode de Steffensen à g1(Q)"
)

it_steff_g2 = pointfixe(gSteff2, Q0, tolr, nmax)
print_table(
    it_steff_g2,
    "TABLEAU 5 — Application de la méthode de Steffensen à g2(Q)"
)

it_steff_gN = pointfixe(gSteffN, Q0, tolr, nmax)
print_table(
    it_steff_gN,
    "TABLEAU 6 — Application de la méthode de Steffensen à gN(Q)"
)
