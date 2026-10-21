"""Unidade Lógica e Aritmética (ULA) da CPU simulada."""


def limitar_8bits(valor):
    """Mantém apenas os 8 bits menos significativos (intervalo 0..255)."""
    return valor & 0xFF


def ula(operacao, a, b):
    """Executa uma operação da ULA e devolve um resultado de 8 bits."""
    if operacao == "ADD":
        resultado = a + b
    elif operacao == "SUB":
        resultado = a - b
    elif operacao == "AND":
        resultado = a & b
    elif operacao == "OR":
        resultado = a | b
    elif operacao == "XOR":
        resultado = a ^ b
    else:
        raise ValueError(f"Operação da ULA inválida: {operacao}")

    return limitar_8bits(resultado)
