"""
Gera graficos dos resultados da mochila fracionada e salva em resultados/.
Requer: matplotlib
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from mochila import mochila_fracionada

CAPACIDADE = 2200
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RESULTADOS_DIR = Path(__file__).resolve().parent.parent / "resultados"


def carregar_csv(caminho):
    cargas = []
    with caminho.open(mode="r", encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f):
            cargas.append({
                "id": linha["id"],
                "descricao": linha["descricao"],
                "peso_kg": float(linha["peso_kg"]),
                "valor_importancia": float(linha["valor_importancia"]),
            })
    return cargas


def grafico_composicao_carga(nome, cargas, resultado):
    """Grafico de barras empilhadas: peso carregado vs nao carregado por item."""
    ids = [c["id"] for c in cargas]
    pesos_totais = [c["peso_kg"] for c in cargas]

    selecionados = {i["id"]: i for i in resultado["itens_selecionados"]}
    pesos_carregados = [selecionados[i]["peso_carregado"] if i in selecionados else 0 for i in ids]
    pesos_nao_carregados = [t - c for t, c in zip(pesos_totais, pesos_carregados)]

    fig, ax = plt.subplots(figsize=(10, 5))
    x = range(len(ids))
    bars1 = ax.bar(x, pesos_carregados, label="Peso carregado", color="#2196F3")
    bars2 = ax.bar(x, pesos_nao_carregados, bottom=pesos_carregados, label="Peso nao carregado", color="#BBDEFB")

    ax.set_xticks(x)
    ax.set_xticklabels(ids)
    ax.set_xlabel("Carga")
    ax.set_ylabel("Peso (kg)")
    ax.set_title(f"Composicao de carga — {nome}")
    ax.legend()
    ax.axhline(0, color="black", linewidth=0.5)

    # Rotula fracao em cada barra
    for i, item_id in enumerate(ids):
        if item_id in selecionados:
            fracao = selecionados[item_id]["fracao"]
            ax.text(i, pesos_carregados[i] / 2, f"{fracao*100:.0f}%",
                    ha="center", va="center", color="white", fontweight="bold", fontsize=9)

    plt.tight_layout()
    caminho = RESULTADOS_DIR / f"grafico_composicao_{nome}.png"
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"  Salvo: {caminho.name}")


def grafico_razao_valor_peso(nome, cargas):
    """Grafico de barras da razao valor/peso de cada item, ordenado."""
    ordenadas = sorted(cargas, key=lambda c: c["valor_importancia"] / c["peso_kg"], reverse=True)
    ids = [c["id"] for c in ordenadas]
    razoes = [c["valor_importancia"] / c["peso_kg"] for c in ordenadas]

    fig, ax = plt.subplots(figsize=(9, 4))
    cores = ["#4CAF50" if i == 0 else "#2196F3" if i < len(ids) - 1 else "#FF9800" for i in range(len(ids))]
    ax.bar(ids, razoes, color=cores)
    ax.set_xlabel("Carga")
    ax.set_ylabel("Valor / Peso")
    ax.set_title(f"Razao valor/peso (criterio de selecao) — {nome}")

    for i, (v, r) in enumerate(zip(ids, razoes)):
        ax.text(i, r + 0.01, f"{r:.2f}", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    caminho = RESULTADOS_DIR / f"grafico_razao_{nome}.png"
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"  Salvo: {caminho.name}")


def grafico_comparativo(resumo):
    """Grafico comparativo de valor total e utilizacao entre cenarios."""
    cenarios = [r["cenario"] for r in resumo]
    valores = [r["valor_total"] for r in resumo]
    utilizacoes = [r["utilizacao_pct"] for r in resumo]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(cenarios, valores, color="#9C27B0")
    ax1.set_title("Valor total obtido por cenario")
    ax1.set_ylabel("Valor total")
    ax1.set_xticklabels(cenarios, rotation=20, ha="right")
    for i, v in enumerate(valores):
        ax1.text(i, v + 10, f"{v:.0f}", ha="center", fontsize=8)

    cores_util = ["#4CAF50" if u == 100 else "#FF9800" for u in utilizacoes]
    ax2.bar(cenarios, utilizacoes, color=cores_util)
    ax2.set_title("Utilizacao do caminhao por cenario (%)")
    ax2.set_ylabel("Utilizacao (%)")
    ax2.set_ylim(0, 110)
    ax2.set_xticklabels(cenarios, rotation=20, ha="right")
    ax2.axhline(100, color="red", linestyle="--", linewidth=1, label="Capacidade maxima")
    ax2.legend()
    for i, u in enumerate(utilizacoes):
        ax2.text(i, u + 1, f"{u:.1f}%", ha="center", fontsize=8)

    plt.tight_layout()
    caminho = RESULTADOS_DIR / "grafico_comparativo.png"
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"  Salvo: {caminho.name}")


def main():
    RESULTADOS_DIR.mkdir(exist_ok=True)
    cenarios = sorted(DATA_DIR.glob("*.csv"))
    resumo = []

    print("Gerando graficos...\n")

    for caminho_csv in cenarios:
        nome = caminho_csv.stem
        cargas = carregar_csv(caminho_csv)
        resultado = mochila_fracionada(cargas, CAPACIDADE)

        print(f"[{nome}]")
        grafico_composicao_carga(nome, cargas, resultado)
        grafico_razao_valor_peso(nome, cargas)

        resumo.append({
            "cenario": nome,
            "valor_total": resultado["valor_total"],
            "utilizacao_pct": (resultado["peso_total"] / CAPACIDADE) * 100,
        })

    print("\n[Comparativo]")
    grafico_comparativo(resumo)
    print("\nTodos os graficos gerados com sucesso.")


if __name__ == "__main__":
    main()
