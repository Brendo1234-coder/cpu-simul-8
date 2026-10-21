"""CPU didática de 8 bits com 4 registradores e 16 posições de memória."""

from ula import ula, limitar_8bits


class CPU:
    def __init__(self):
        # Quatro registradores gerais, todos iniciados em zero.
        self.registradores = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}

        # Memória com 16 posições, numeradas de 0 a 15.
        self.memoria = [None] * 16

        # Program Counter: endereço da próxima instrução.
        self.pc = 0
        self.halted = False
        self.ciclos = 0

    def carregar_programa(self, programa, inicio=0):
        """Copia uma lista de instruções para a memória a partir de 'inicio'."""
        if inicio < 0 or inicio + len(programa) > len(self.memoria):
            raise ValueError("O programa não cabe nas 16 posições de memória.")
        for deslocamento, instrucao in enumerate(programa):
            self.memoria[inicio + deslocamento] = instrucao
        self.pc = inicio
        self.halted = False
        self.ciclos = 0

    def validar_registrador(self, nome):
        if nome not in self.registradores:
            raise ValueError(f"Registrador inválido: {nome}")

    def executar_instrucao(self, instrucao):
        """DECODE + EXECUTE: interpreta e executa uma instrução."""
        if instrucao is None:
            raise RuntimeError(
                f"Não há instrução na posição de memória {self.pc}."
            )

        # Aceita, por exemplo, 'LOAD R0, 5' e 'ADD R0, R1'.
        partes = instrucao.replace(",", "").split()
        if not partes:
            raise ValueError("Instrução vazia.")
        operacao = partes[0].upper()

        if operacao == "LOAD":
            if len(partes) != 3:
                raise ValueError("Formato esperado: LOAD R0, valor")
            registrador = partes[1].upper()
            self.validar_registrador(registrador)
            valor = int(partes[2])
            self.registradores[registrador] = limitar_8bits(valor)
            self.pc += 1

        elif operacao == "STORE":
            if len(partes) != 3:
                raise ValueError("Formato esperado: STORE R0, endereço")
            registrador = partes[1].upper()
            self.validar_registrador(registrador)
            endereco = int(partes[2])
            self.validar_endereco(endereco)
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        elif operacao in ("ADD", "SUB", "AND", "OR", "XOR"):
            if len(partes) != 3:
                raise ValueError(f"Formato esperado: {operacao} R0, R1")
            destino = partes[1].upper()
            origem = partes[2].upper()
            self.validar_registrador(destino)
            self.validar_registrador(origem)
            a = self.registradores[destino]
            b = self.registradores[origem]
            self.registradores[destino] = ula(operacao, a, b)
            self.pc += 1

        elif operacao == "JMP":
            if len(partes) != 2:
                raise ValueError("Formato esperado: JMP endereço")
            endereco = int(partes[1])
            self.validar_endereco(endereco)
            self.pc = endereco

        elif operacao == "HALT":
            self.halted = True
            # O PC fica na posição da instrução HALT.
        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    def validar_endereco(self, endereco):
        if not 0 <= endereco < len(self.memoria):
            raise ValueError(
                f"Endereço inválido: {endereco}. Use um valor de 0 a 15."
            )

    def mostrar_estado(self, instrucao=None):
        print(f"PC: {self.pc:02d}")
        if instrucao is not None:
            print(f"Instrução: {instrucao}")
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:03d} (0x{valor:02X})")

    def ciclo(self):
        """FETCH → DECODE → EXECUTE para uma instrução."""
        if self.halted:
            return

        self.validar_endereco(self.pc)

        # FETCH: obter a instrução apontada pelo PC.
        endereco_instrucao = self.pc
        instrucao = self.memoria[endereco_instrucao]

        print("\n" + "-" * 38)
        print(f"FETCH: endereço {endereco_instrucao:02d}")
        print(f"PC: {endereco_instrucao:02d}")
        print(f"Instrução: {instrucao}")

        # DECODE + EXECUTE.
        self.executar_instrucao(instrucao)
        self.ciclos += 1

        print("Estado após a execução:")
        print(f"PC seguinte: {self.pc:02d}")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:03d} (0x{valor:02X})")
        print(f"CPU encerrada: {'Sim' if self.halted else 'Não'}")

    def executar(self, limite_ciclos=100):
        """Executa até HALT ou até atingir o limite de segurança."""
        while not self.halted:
            if self.ciclos >= limite_ciclos:
                raise RuntimeError(
                    "Limite de ciclos atingido; verifique se há um loop infinito."
                )
            self.ciclo()

    def mostrar_memoria(self):
        print("\nMemória:")
        for endereco, valor in enumerate(self.memoria):
            print(f"  MEM[{endereco:02d}] = {valor}")
