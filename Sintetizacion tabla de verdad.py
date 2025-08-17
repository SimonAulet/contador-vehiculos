# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# | SC | B2 | B1 | SR | S | B2 | B1 |
# |----|----|----|----|---|----|----|
# | IN | IN | IN |OUT |OUT|OUT | OUT|
# | 0  | 0  | 0  | X  | 0 | 0  | 0  |
# | 0  | 0  | 1  | 1  | 1 | 0  | 1  |
# | 0  | 1  | 0  | 0  | 1 | 1  | 0  |
# | 0  | 1  | 1  | X  | 0 | 1  | 1  |
# | 1  | 0  | 0  | X  | 0 | 0  | 0  |
# | 1  | 0  | 1  | X  | 0 | 0  | 0  |
# | 1  | 1  | 0  | 0  | 1 | 1  | 0  |
# | 1  | 1  | 1  | X  | 0 | 1  | 1  |

# %%
from sympy.logic import SOPform
from sympy import symbols

# %%
SC, B2, B1 = symbols('SC B2 B1')
minterms_SR = [[0, 0, 1]]
dontcare_SR = [[0, 0, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]]
minterms_S  = [[0, 0, 1], [0, 1, 0], [1, 1, 0]]
minterms_B2 = [[0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]
minterms_B1 = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
SR = SOPform([SC, B2, B1], minterms_SR, dontcare_SR)
S  = SOPform([SC, B2, B1], minterms_S)
B2 = SOPform([SC, B2, B1], minterms_B2)
B1 = SOPform([SC, B2, B1], minterms_B1)

# %%

A, B = symbols('A B')
minterms_Y1 = [[0, 1], [1, 0]]  # Filas donde Y1=1
minterms_Y2 = [[0, 0], [1, 0]]  # Filas donde Y2=1

# Obtener expresiones SOP
Y1 = SOPform([A, B], minterms_Y1)
Y2 = SOPform([A, B], minterms_Y2)

print("Y1 =", Y1)  # Y1 = (A & ~B) | (~A & B)
print("Y2 =", Y2)  # Y2 = ~B

# %%
from sympy.logic import SOPform
from sympy import symbols

# Variables:
A, B, C = symbols('A B C')

# Minterminos (donde la salida es 1):
minterms = [[0, 0, 1], [1, 0, 0]]  # Ej: Y=1 en A=0,B=0,C=1 y A=1,B=0,C=0

# Don't cares (donde la salida puede ser 0 o 1):
dontcares = [[1, 1, 0], [0, 1, 1]]  # Ej: Y es indiferente en estas combinaciones

# Minimización considerando don't cares:
expr_minimizada = SOPform([A, B, C], minterms, dontcares)
print(expr_minimizada)

# %%
from sympy.logic import SOPform
from sympy import symbols

# %%
A, B = symbols('A B')
minterms_Y1 = [[0, 1], [1, 0]]
minterms_Y2 = [[0, 0], [1, 0]]

# %%
SOPform([A, B], minterms_Y1)
