import sys
input = sys.stdin.readline

def vow(word):
    # dp 선언
    dp = [False]*(len(word)+1)
    dp[0] = True

    # 원소 주기율표
    elements = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
        "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
        "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"
    ]
    # 모든 원소 소문자로 변경
    elements = [elem.lower() for elem in elements]
    
    for i in range(1, len(word)+1):
        if i>=1 and word[i-1:i] in elements and dp[i-1]:
            dp[i] = True
        if i>=2 and word[i-2:i] in elements and dp[i-2]:
            dp[i] = True

    return "YES" if dp[-1] else "NO"
    
N = int(input())
words = [input().rstrip() for _ in range(N)]

for word in words:
    print(vow(word))