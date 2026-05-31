import csv
from pathlib import Path

from mochila import mochila_fracionada


CAPACIDADE_PADRAO_KG = 2200
CAMINHO_CSV = Path(__file__).resolve().parent.parent / "data" / "cargas.csv"


def carregar_cargas(caminho_csv):
    cargas = []

    with caminho_csv.open(mode="r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            cargas.append(
                {
                    "id": linha["id"],
                    "descricao": linha["descricao"],
                    "peso_kg": float(linha["peso_kg"]),
                    "valor_importancia": float(linha["valor_importancia"]),
                }
            )

    return cargas


def exibir_cargas(cargas):
    print("Cargas disponiveis:")

    for carga in cargas:
        print(
            f"- {carga['id']} | {carga['descricao']} | "
            f"{carga['peso_kg']:.0f} kg | valor {carga['valor_importancia']:.0f}"
        )


def main():
    print("=" * 60)
    print("Grupo 1 - Mochila Fracionada")
    print("MidWest Logistics S/A")
    print("=" * 60)
    print(f"Capacidade padrao do caminhao: {CAPACIDADE_PADRAO_KG} kg")
    print()

    try:
        cargas = carregar_cargas(CAMINHO_CSV)
    except FileNotFoundError:
        print("Erro: arquivo CSV nao encontrado.")
        print(f"Caminho esperado: {CAMINHO_CSV}")
        return

    exibir_cargas(cargas)
    print()

    # Integracao com o algoritmo do Alexandre:
    # quando a funcao mochila_fracionada for implementada em mochila.py,
    # o resultado final da selecao de cargas sera retornado nesta chamada.
    resultado = mochila_fracionada(cargas, CAPACIDADE_PADRAO_KG)

    print("Resultado da mochila fracionada:")
    if resultado is None:
        print("Algoritmo ainda nao implementado em src/mochila.py.")
        print("Aguardando implementacao do Alexandre.")
    else:
        print(resultado)


if __name__ == "__main__":
    main()
