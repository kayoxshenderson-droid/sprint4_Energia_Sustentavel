def calcular_economia(geracao, consumo, bateria):
    if geracao >= consumo:
        energia_rede = 0
    else:
        falta = consumo - geracao
        energia_bateria = bateria / 10
        energia_rede = max(
            falta - energia_bateria,
            0
        )

    custo = energia_rede * 0.85
    return energia_rede, custo


def calcular_co2(geracao, consumo):
    energia_solar_utilizada = min(
        geracao,
        consumo
    )
    co2 = energia_solar_utilizada * 0.08
    return co2
