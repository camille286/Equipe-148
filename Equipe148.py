import math
from Bissection import Bissection
from pointfixe import pointfixe

# =========================
# Bissection
# =========================

def F(Q):
    return math.exp(Q) + Q**2 - 5

n = 18  # réponse de la question b)

X = Bissection(F, 1, 2, tol=1e-6, nmax=100)

Qn  = X[n-1]  # Q18
Qn1 = X[n]    # Q19

print(f"Q{n} =", Qn)
print(f"|Q{n+1} - Q{n}| =", abs(Qn1 - Qn))
print(f"Q{n} (5 chiffres signif) =", format(Qn, ".5g"))

# =========================
# (d) Propagation d’erreur
# =========================

def O(Q):
    return math.exp(Q)

def D(Q):
    return -Q**2 + 5

errQ = abs(Qn1 - Qn)

DeltaO = abs(math.exp(Qn)) * errQ      # O'(Q)=e^Q
DeltaD = abs(-2*Qn) * errQ             # D'(Q)=-2Q

print("\nΔO <=", DeltaO)
print("ΔD <=", DeltaD)


# =========================
# (e) Valeurs arrondies
# =========================

OQn = O(Qn)
DQn = D(Qn)

print("\nO(Qn) =", format(OQn, ".5g"))
print("D(Qn) =", format(DQn, ".5g"))

# =========================
# POINT FIXE
# =========================

def g1(Q):
    return math.log(-Q**2 + 5)

def g2(Q):
    return 10 - 2*math.exp(Q)

def dF(Q):
    return math.exp(Q) + 2*Q

def gN(Q):
    return Q - F(Q)/dF(Q)


def print_table(iterations, title, max_rows=None):
    print("\n" + title)
    print("n\tQn\t\t\t|en|")

    N = len(iterations) - 1
    if max_rows is None:
        max_rows = N

    for n in range(0, min(max_rows, N) + 1):
        Qn = iterations[n]

        if n == 0:
            print(f"{n}\t{Qn:.16f}\t-")
        else:
            en = abs(iterations[n] - iterations[n-1])
            print(f"{n}\t{Qn:.16f}\t{en:.9e}")


Q0 = 1
tolr = 1e-8
nmax = 150

it_g1 = pointfixe(g1, Q0, tolr, nmax)
print_table(it_g1, "Point fixe g1")

it_g2 = pointfixe(g2, Q0, tolr, nmax)
print_table(it_g2, "Point fixe g2 (5 premières)", 5)

it_gN = pointfixe(gN, Q0, tolr, nmax)
print_table(it_gN, "Newton (gN)")
