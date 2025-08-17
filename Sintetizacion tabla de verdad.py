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
# # Logica secuencuial a partir de la tabla de verdad

# %% [markdown]
# A partir de la tabla de verdad que pongo a continuación uso `sympy.symbols` para sacar las expresiones booleanas de las 4 salidas

# %% [markdown]
# - SC: Señal de contador (lleno 1, caso contrario 0)
# - b1: Botón de accionado para ENTRADA de vehículos
# - b2: Botón de accionado para SALIDA de vehículos
# - B1: Barra mecánica de ENTRADA
# - B2: Barra mecánica de SALIDA
# - SR: Señal de suma o resta del contador (S(Suma) = 1, S(Resta) = 0)
# - S: Señal si se hace una acción en el contador o no (Se hace acción 1, CC 0)
#
#
# | SC | b2 | b1 | SR | S | B2 | B1 |
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
from sympy import init_printing
init_printing()

# %%
SC, b2, b1 = symbols('SC b2 b1') #Entradas

minterms_SR = [[0, 0, 1]]
dontcare_SR = [[0, 0, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]]#Especifico el dontcare, sympy lo soporta
minterms_S  = [[0, 0, 1], [0, 1, 0], [1, 1, 0]]
minterms_B2 = [[0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]
minterms_B1 = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]

#Salidas en forma SOP
SR = SOPform([SC, b2, b1], minterms_SR, dontcare_SR)
S  = SOPform([SC, b2, b1], minterms_S)
B2 = SOPform([SC, b2, b1], minterms_B2)
B1 = SOPform([SC, b2, b1], minterms_B1)

# %%
SR

# %%
S

# %%
B2

# %%
B1

# %% [markdown]
# Bien, entonces queda:
#
# - $\displaystyle SR = \overline{b_2}$
#
# - $\displaystyle S = \left(b_2 \cdot \overline{b_1}\right) + \left(b_1 \cdot \overline{SC} \cdot \overline{b_2}\right)$
#
# - $\displaystyle B_2 = b_2$
#
# - $\displaystyle B_1 = \left( b_1 \cdot b_2 \right) + \left(b_1 \cdot \overline{SC}\right)$
