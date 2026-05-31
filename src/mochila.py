def mochila_fracionada(cargas, capacidade):
    """
    Algoritmo guloso da mochila fracionada.

    Ordena as cargas pela razão valor/peso (decrescente) e preenche o caminhão
    tomando cada carga inteira quando possível ou uma fração quando necessário.

    Retorna um dict com:
      - itens_selecionados: lista de dicts com carga + fracao + peso_carregado + valor_obtido
      - peso_total:  soma do peso efetivamente carregado
      - valor_total: soma do valor obtido
      - capacidade:  capacidade do caminhão
    """
    # Calcula a razão valor/peso para cada carga e ordena (maior razão primeiro)
    ordenadas = sorted(
        cargas,
        key=lambda c: c["valor_importancia"] / c["peso_kg"],
        reverse=True,
    )

    itens_selecionados = []
    peso_restante = capacidade

    for carga in ordenadas:
        if peso_restante <= 0:
            break

        peso_disponivel = carga["peso_kg"]
        fracao = min(1.0, peso_restante / peso_disponivel)

        peso_carregado = fracao * peso_disponivel
        valor_obtido = fracao * carga["valor_importancia"]

        itens_selecionados.append(
            {
                **carga,
                "fracao": fracao,
                "peso_carregado": peso_carregado,
                "valor_obtido": valor_obtido,
            }
        )

        peso_restante -= peso_carregado

    peso_total = sum(i["peso_carregado"] for i in itens_selecionados)
    valor_total = sum(i["valor_obtido"] for i in itens_selecionados)

    return {
        "itens_selecionados": itens_selecionados,
        "peso_total": peso_total,
        "valor_total": valor_total,
        "capacidade": capacidade,
    }
