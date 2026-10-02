import random


def gerar_dados():

    geracao_solar = round(random.uniform(2, 10), 2)
    consumo = round(random.uniform(2, 8), 2)
    bateria = random.randint(20, 90)

    return geracao_solar, consumo, bateria