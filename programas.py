"""Programas de demonstração para a CPU simulada."""

# Programa próprio com 10 instruções.
# Calcula (5 + 8) XOR 3, guarda 13 em MEM[15] e 14 em MEM[14].
PROGRAMA_DEMO = [
    "LOAD R0, 5",       # 0: R0 = 5
    "LOAD R1, 8",       # 1: R1 = 8
    "ADD R0, R1",       # 2: R0 = 13
    "STORE R0, 15",     # 3: MEM[15] = 13
    "LOAD R2, 3",       # 4: R2 = 3
    "XOR R0, R2",       # 5: R0 = 13 XOR 3 = 14
    "STORE R0, 14",     # 6: MEM[14] = 14
    "LOAD R3, 2",       # 7: R3 = 2
    "SUB R0, R3",       # 8: R0 = 14 - 2 = 12
    "HALT",             # 9: encerra a execução
]

# Exemplo mínimo exigido no enunciado: 5 + 8 = 13.
PROGRAMA_SOMA = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT",
]
