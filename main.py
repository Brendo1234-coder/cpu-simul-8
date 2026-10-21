"""Executa a demonstração principal da CPU simulada."""

from cpu import CPU
from programas import PROGRAMA_DEMO


def main():
    cpu = CPU()
    cpu.carregar_programa(PROGRAMA_DEMO)

    print("=" * 38)
    print("       CPU SIMULADA - 8 BITS")
    print("=" * 38)

    cpu.executar()

    print("\nResultado final:")
    print("MEM[15] =", cpu.memoria[15], "(resultado de 5 + 8)")
    print("MEM[14] =", cpu.memoria[14], "(resultado de 13 XOR 3)")
    print("R0 =", cpu.registradores["R0"], "(resultado final após SUB)")
    print("Total de ciclos:", cpu.ciclos)


if __name__ == "__main__":
    main()
