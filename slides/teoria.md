# Teoria, Pseudocodigo e Roteiro do Video
## Grupo 1 — Mochila Fracionada | PAA - I

---

## 1. Contexto do Problema

A **MidWest Logistics S/A** precisa carregar um caminhao com capacidade limitada (2200 kg).
Ha diversas cargas disponiveis, cada uma com um peso e um valor de importancia.
O objetivo e **maximizar o valor total transportado** sem ultrapassar a capacidade.

Diferente da mochila 0/1 classica, aqui as cargas sao **fracionaveis**: e possivel
transportar uma fração de uma carga e obter a fração correspondente do valor.

---

## 2. Estrategia Gulosa (Greedy)

A abordagem gulosa funciona porque o problema tem a **propriedade da escolha gulosa**:
a decisao localmente otima em cada passo leva ao otimo global.

**Intuicao:** se voce pode fracionara carga, sempre vale a pena priorizar aquelas
com maior relacao valor por quilograma.

**Prova informal:** suponha que o algoritmo nao escolheu o item com maior razao
valor/peso primeiro. Trocar qualquer fracao de outro item por uma fracao desse item
so pode aumentar o valor total — logo a solucao sem ele nao e otima. Contradicao.

---

## 3. Pseudocodigo

```
ALGORITMO MochilaFracionada(cargas, capacidade):

  // Passo 1: calcular a razao valor/peso de cada carga
  PARA CADA carga em cargas:
    carga.razao <- carga.valor / carga.peso

  // Passo 2: ordenar em ordem decrescente de razao
  ORDENAR cargas por carga.razao (decrescente)

  // Passo 3: preencher o caminhao gulodosamente
  peso_restante <- capacidade
  valor_total   <- 0
  itens_selecionados <- []

  PARA CADA carga em cargas (ja ordenadas):
    SE peso_restante <= 0:
      PARAR

    fracao <- MIN(1.0, peso_restante / carga.peso)

    peso_carregado <- fracao * carga.peso
    valor_obtido   <- fracao * carga.valor

    ADICIONAR (carga, fracao, peso_carregado, valor_obtido) a itens_selecionados
    peso_restante <- peso_restante - peso_carregado
    valor_total   <- valor_total + valor_obtido

  RETORNAR itens_selecionados, valor_total
```

---

## 4. Complexidade

| Etapa                        | Complexidade |
|------------------------------|-------------|
| Calculo da razao valor/peso  | O(n)        |
| Ordenacao                    | O(n log n)  |
| Preenchimento do caminhao    | O(n)        |
| **Total**                    | **O(n log n)** |

- **n** = numero de cargas disponiveis
- A complexidade e dominada pela ordenacao (Timsort no Python).
- Espaco auxiliar: O(n) para armazenar os itens selecionados.

**Por que O(n log n) e eficiente?**
Para n = 1.000.000 de cargas, sao aproximadamente 20.000.000 operacoes — executavel
em frações de segundo em qualquer computador moderno.

---

## 5. Exemplo Passo a Passo (Cenario Basico)

Capacidade do caminhao: **2200 kg**

| ID | Descricao              | Peso (kg) | Valor | Razao (V/P) |
|----|------------------------|-----------|-------|-------------|
| R2 | Refrigerados Goiania   | 600       | 950   | **1.583**   |
| R1 | Hosp. Brasilia         | 800       | 1200  | **1.500**   |
| R3 | Fertilizante Rondonia  | 1200      | 1300  | **1.083**   |
| R5 | Bebidas Cuiaba         | 1000      | 900   | 0.900       |
| R4 | Seca Dourados          | 500       | 500   | 1.000       |

**Execucao:**
1. R2 entra inteiro → peso restante: 2200 - 600 = 1600 kg, valor: 950
2. R1 entra inteiro → peso restante: 1600 - 800 = 800 kg, valor: 950 + 1200 = 2150
3. R3: peso 1200 > 800 restantes → entra 800/1200 = **66,7%** → valor: 2150 + 866,7 = 3016,7
4. Caminhao lotado. Para.

**Resultado: valor total = 3016,7 | peso = 2200 kg (100% utilizado)**

---

## 6. Roteiro do Video

### Duracao sugerida: 5 a 8 minutos

---

**[0:00 – 0:30] Abertura**
- Mostrar o nome do grupo e o tema: "Mochila Fracionada — Grupo 1"
- Apresentar rapidamente os integrantes

---

**[0:30 – 1:30] Apresentacao do problema**
- Contextualizar: empresa MidWest Logistics S/A
- Caminhao com capacidade de 2200 kg
- Diversas cargas com pesos e valores diferentes
- Objetivo: maximizar o valor sem ultrapassar o peso
- Diferenca entre mochila 0/1 (sem fracao) e mochila fracionada (com fracao)

---

**[1:30 – 3:00] Estrategia e algoritmo**
- Explicar a ideia da razao valor/peso
- Mostrar o pseudocodigo no slide
- Explicar passo a passo com o exemplo do cenario basico

---

**[3:00 – 4:30] Demonstracao do codigo**
- Abrir o arquivo `src/mochila.py` e explicar o codigo Python
- Mostrar o arquivo `data/cargas.csv`
- Executar `python src/main.py` no terminal ao vivo
- Mostrar a saida formatada

---

**[4:30 – 5:30] Resultados e graficos**
- Mostrar os graficos gerados em `resultados/`
- Grafico de composicao de carga (o que coube e o que nao coube)
- Grafico de razao valor/peso (criterio de selecao)
- Grafico comparativo entre os cenarios de teste

---

**[5:30 – 6:30] Complexidade**
- Mostrar a tabela de complexidade
- Explicar por que O(n log n) e eficiente na pratica

---

**[6:30 – 7:00] Conclusao**
- Resumir o que foi feito
- Destacar que o algoritmo guloso encontra a solucao otima para este problema
- Agradecer e encerrar
