"""Testes automáticos básicos da CPU e da ULA."""

import unittest
from cpu import CPU
from ula import ula, limitar_8bits
from programas import PROGRAMA_SOMA


class TestULA(unittest.TestCase):
    def test_add(self):
        self.assertEqual(ula("ADD", 5, 8), 13)

    def test_sub(self):
        self.assertEqual(ula("SUB", 5, 8), 253)  # -3 representado em 8 bits

    def test_logicas(self):
        self.assertEqual(ula("AND", 0b1100, 0b1010), 0b1000)
        self.assertEqual(ula("OR", 0b1100, 0b1010), 0b1110)
        self.assertEqual(ula("XOR", 0b1100, 0b1010), 0b0110)

    def test_limite_8bits(self):
        self.assertEqual(limitar_8bits(256), 0)
        self.assertEqual(limitar_8bits(-1), 255)


class TestCPU(unittest.TestCase):
    def test_programa_soma(self):
        cpu = CPU()
        cpu.carregar_programa(PROGRAMA_SOMA)
        cpu.executar()
        self.assertEqual(cpu.memoria[15], 13)

    def test_store(self):
        cpu = CPU()
        cpu.carregar_programa(["LOAD R2, 42", "STORE R2, 4", "HALT"])
        cpu.executar()
        self.assertEqual(cpu.memoria[4], 42)

    def test_jmp(self):
        cpu = CPU()
        cpu.carregar_programa([
            "JMP 2",
            "LOAD R0, 99",
            "LOAD R0, 7",
            "HALT",
        ])
        cpu.executar()
        self.assertEqual(cpu.registradores["R0"], 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
