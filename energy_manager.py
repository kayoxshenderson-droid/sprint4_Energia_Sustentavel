def gerenciar_energia(geracao, consumo, bateria):

    if geracao > consumo:

        excedente = geracao - consumo

        if bateria < 100:
            decisao = "Carregar bateria"
        else:
            decisao = "Enviar excedente para a rede"

    elif geracao < consumo:

        falta = consumo - geracao

        if bateria > 20:
            decisao = "Usar energia da bateria"
        else:
            decisao = "Utilizar energia da rede"

    else:

        decisao = "Energia solar atende o consumo"

    return decisao