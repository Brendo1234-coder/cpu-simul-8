# CPU Simulada de 8 bits

Projeto didático para a disciplina de Arquitetura de Computadores.

## Arquitetura

- Dados de 8 bits: resultados mantidos entre 0 e 255.
- Quatro registradores: R0, R1, R2 e R3.
- Memória com 16 posições, de 0 a 15.
- PC (Program Counter), que indica a próxima instrução.
- ULA: ADD, SUB, AND, OR e XOR.
- Ciclo de execução: Fetch, Decode e Execute.

## Instruções

| Instrução | Exemplo | Função |
|---|---|---|
| LOAD | `LOAD R0, 5` | Coloca um valor no registrador |
| STORE | `STORE R0, 15` | Grava o registrador na posição de memória |
| ADD | `ADD R0, R1` | Soma R1 a R0 e guarda em R0 |
| SUB | `SUB R0, R1` | Subtrai R1 de R0 e guarda em R0 |
| AND | `AND R0, R1` | AND bit a bit |
| OR | `OR R0, R1` | OR bit a bit |
| XOR | `XOR R0, R1` | XOR bit a bit |
| JMP | `JMP 8` | Altera o PC para o endereço 8 |
| HALT | `HALT` | Encerra a execução |

## Como executar

Requer Python 3. Abra um terminal na pasta do projeto.

Executar a demonstração:
```bash
python main.py
```

Executar os testes:
```bash
python -m unittest -v testes.py
```

## Programa demonstrativo

O programa em `programas.py` tem 10 instruções e usa LOAD, STORE, ADD, XOR e SUB.

Resultados esperados:
- `MEM[15] = 13`, a partir de 5 + 8.
- `MEM[14] = 14`, a partir de 13 XOR 3.
- `R0 = 12` no final, após subtrair 2 de 14.

## Convenção de 8 bits

Depois de cada operação, a CPU aplica `valor & 0xFF`, preservando os 8 bits menos significativos. Por isso, por exemplo, `SUB 5, 8` resulta em 253 (a representação sem sinal de 8 bits para o padrão de bits de -3).

## Limitações didáticas

A memória guarda strings de instruções nas posições usadas pelo programa e valores inteiros nas posições escritas por STORE. Não há codificação binária real das instruções, interrupções ou periféricos: o projeto é uma simulação didática.
