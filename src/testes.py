"""
Testes e registro de resultados para a mochila fracionada.
Executa todos os cenarios de data/ e salva os resultados em resultados/.
"""

import csv
from pathlib import Path

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


def formatar_resultado(nome_cenario, cargas, resultado, capacidade):
    linhas = []
    linhas.append("=" * 70)
    linhas.append(f"Cenario: {nome_cenario}")
    linhas.append(f"Capacidade do caminhao: {capacidade} kg")
    linhas.append(f"Total de cargas disponiveis: {len(cargas)}")
    linhas.append("-" * 70)
    linhas.append(f"{'ID':<6} {'Descricao':<38} {'Fracao':>7} {'Peso':>8} {'Valor':>8}")
    linhas.append("-" * 70)
    for item in resultado["itens_selecionados"]:
        linhas.append(
            f"{item['id']:<6} {item['descricao']:<38} "
            f"{item['fracao']*100:>6.1f}% "
            f"{item['peso_carregado']:>8.1f} "
            f"{item['valor_obtido']:>8.1f}"
        )
    linhas.append("-" * 70)
    linhas.append(
        f"{'TOTAL':<6} {'':<38} {'':>7} "
        f"{resultado['peso_total']:>8.1f} {resultado['valor_total']:>8.1f}"
    )
    utilizacao = (resultado["peso_total"] / capacidade) * 100
    linhas.append(f"Utilizacao do caminhao: {utilizacao:.1f}%")
    linhas.append("")
    return "\n".join(linhas)


def executar_testes():
    RESULTADOS_DIR.mkdir(exist_ok=True)

    cenarios = sorted(DATA_DIR.glob("*.csv"))
    todos_resultados = []
    resumo = []

    print(f"Encontrados {len(cenarios)} cenario(s).\n")

    for caminho_csv in cenarios:
        nome = caminho_csv.stem
        cargas = carregar_csv(caminho_csv)
        resultado = mochila_fracionada(cargas, CAPACIDADE)

        texto = formatar_resultado(nome, cargas, resultado, CAPACIDADE)
        todos_resultados.append(texto)
        print(texto)

        utilizacao = (resultado["peso_total"] / CAPACIDADE) * 100
        resumo.append({
            "cenario": nome,
            "cargas_disponiveis": len(cargas),
            "cargas_selecionadas": len(resultado["itens_selecionados"]),
            "peso_total": resultado["peso_total"],
            "valor_total": resultado["valor_total"],
            "utilizacao_pct": utilizacao,
        })

    # Salva resultados em texto
    arquivo_txt = RESULTADOS_DIR / "resultados.txt"
    arquivo_txt.write_text("\n".join(todos_resultados), encoding="utf-8")
    print(f"Resultados salvos em: {arquivo_txt}")

    # Salva resumo CSV
    arquivo_csv = RESULTADOS_DIR / "resumo.csv"
    with arquivo_csv.open("w", encoding="utf-8", newline="") as f:
        campos = ["cenario", "cargas_disponiveis", "cargas_selecionadas",
                  "peso_total", "valor_total", "utilizacao_pct"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resumo)
    print(f"Resumo CSV salvo em: {arquivo_csv}")

    return resumo


if __name__ == "__main__":
    executar_testes()
