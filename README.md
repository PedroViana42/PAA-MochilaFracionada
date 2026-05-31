# Grupo 1 - Mochila Fracionada

## Tema

Mochila Fracionada.

## Objetivo

Simular a selecao de cargas fracionaveis para um caminhao da empresa ficticia MidWest Logistics S/A, buscando maximizar o valor total transportado sem ultrapassar o limite de peso do caminhao.

## Integrantes e divisao de tarefas

- Pedro: estrutura do projeto, `main.py`, integracao, README e GitHub.
- Alexandre: algoritmo da mochila fracionada.
- Diogenes: dados CSV e cenarios de teste.
- Leonardo: testes, resultados e graficos.
- Miguel: slides, teoria, pseudocodigo, complexidade e roteiro do video.

## Estrutura de pastas

```text
grupo1-mochila-fracionada/
├── data/
│   └── cargas.csv
├── src/
│   ├── main.py
│   └── mochila.py
├── resultados/
├── slides/
├── README.md
├── requirements.txt
└── .gitignore
```

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python src/main.py
```

O programa le o arquivo `data/cargas.csv`, define a capacidade padrao do caminhao como 2200 kg e chama a funcao `mochila_fracionada`.

## Algoritmo

O algoritmo guloso implementado em `src/mochila.py` segue os passos:

1. Calcula a razao valor/peso de cada carga.
2. Ordena as cargas de forma decrescente por essa razao.
3. Preenche o caminhao tomando cada carga inteira quando couber ou uma fracao quando necessario.

**Complexidade:** O(n log n), dominada pela etapa de ordenacao.

## Checklist de requisitos do trabalho

- [x] Criar estrutura inicial do projeto.
- [x] Criar arquivo `src/main.py`.
- [x] Preparar integracao com `mochila_fracionada`.
- [x] Criar README inicial.
- [x] Organizar arquivos para GitHub.
- [x] Incluir CSV inicial de exemplo.
- [x] Implementar algoritmo da mochila fracionada.
- [x] Criar cenarios de teste adicionais.
- [x] Criar testes e registrar resultados.
- [x] Criar graficos.
- [x] Criar slides, teoria, pseudocodigo, complexidade e roteiro do video.
