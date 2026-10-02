import streamlit as st
import pandas as pd

from simulation import gerar_dados
from energy_manager import gerenciar_energia
from calculations import calcular_economia, calcular_co2


# ====== CONFIGURAÇÃO DA PÁGINA ======

st.set_page_config(
    page_title="GoodWe Smart Energy",
    page_icon="☀️",
    layout="wide"
)


# ====== TÍTULO ======

st.title("☀️ GoodWe Smart Energy")

st.write(
    "Sistema inteligente de gerenciamento e otimização "
    "de energia renovável."
)

st.info(
    "Projeto acadêmico desenvolvido para o Sprint 4. "
    "Os dados apresentados são simulados."
)


#  ====== BOTÃO DE SIMULAÇÃO ======

if st.button("▶️ Executar nova simulação", use_container_width=True):

    # Gera os dados
    geracao, consumo, bateria = gerar_dados()

    # Define a decisão do sistema
    decisao = gerenciar_energia(
        geracao,
        consumo,
        bateria
    )

    # Calcula consumo da rede e custo
    energia_rede, custo = calcular_economia(
        geracao,
        consumo,
        bateria
    )

    # Calcula CO2 evitado
    co2 = calcular_co2(
        geracao,
        consumo
    )



    #  ====== MONITORAMENTO ======

    st.subheader("📊 Monitoramento energético")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "☀️ Geração Solar",
            f"{geracao:.2f} kW"
        )

    with col2:
        st.metric(
            "⚡ Consumo",
            f"{consumo:.2f} kW"
        )

    with col3:
        st.metric(
            "🔋 Bateria",
            f"{bateria}%"
        )

    with col4:
        st.metric(
            "🌐 Energia da Rede",
            f"{energia_rede:.2f} kWh"
        )


    #  ====== DECISÃO INTELIGENTE ======

    st.subheader("🤖 Decisão inteligente")

    st.success(
        f"**Ação do sistema:** {decisao}"
    )



    # ====== FLUXO DE ENERGIA ======

    st.subheader("🔄 Fluxo de energia")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ☀️ Solar")
        st.write(
            f"{geracao:.2f} kW disponíveis"
        )

    with col2:
        st.markdown("### 🔋 Bateria")
        st.write(
            f"{bateria}% de carga"
        )

    with col3:
        st.markdown("### 🏢 Consumo")
        st.write(
            f"{consumo:.2f} kW utilizados"
        )



    # ====== RESULTADOS DA SIMULAÇÃO ======

    st.subheader("🌱 Resultados da simulação")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💰 Custo estimado",
            f"R$ {custo:.2f}"
        )

    with col2:
        st.metric(
            "🌱 CO₂ evitado",
            f"{co2:.2f} kg"
        )

    with col3:
        st.metric(
            "☀️ Energia renovável",
            f"{min(geracao, consumo):.2f} kWh"
        )



    # ====== GRÁFICO ======


    st.subheader("📈 Geração x Consumo")

    dados = pd.DataFrame(
        {
            "Energia (kW)": [
                geracao,
                consumo
            ]
        },
        index=[
            "☀️ Geração Solar",
            "⚡ Consumo"
        ]
    )

    st.bar_chart(dados)



    # ====== ANÁLISE DO SISTEMA ======


    st.subheader("🧠 Análise")

    if geracao > consumo:

        excedente = geracao - consumo

        st.write(
            f"A geração solar foi **{excedente:.2f} kW** "
            "maior que o consumo. O sistema identificou "
            "um excedente energético e priorizou o "
            "armazenamento na bateria."
        )

    elif geracao < consumo:

        falta = consumo - geracao

        st.write(
            f"O consumo foi **{falta:.2f} kW** maior que "
            "a geração solar. O sistema verificou o nível "
            "da bateria para complementar a energia."
        )

    else:

        st.write(
            "A geração solar foi suficiente para atender "
            "exatamente ao consumo."
        )



    # ====== SUSTENTABILIDADE ======


    st.subheader("🌎 Sustentabilidade")

    st.write(
        "A solução busca aumentar o aproveitamento da "
        "energia renovável e reduzir a necessidade de "
        "utilização da rede elétrica."
    )

    st.write(
        f"Na simulação atual, aproximadamente "
        f"**{min(geracao, consumo):.2f} kWh** foram "
        "atendidos diretamente pela geração solar."
    )

    st.write(
        f"A estimativa de redução de emissões é de "
        f"**{co2:.2f} kg de CO₂**."
    )


#  ====== TELA INICIAL =======

else:

    st.warning(
        "Clique em **Executar nova simulação** "
        "para iniciar o sistema."
    )

    st.subheader("💡 Como funciona?")

    st.write(
        "O sistema simula um cenário de geração de energia "
        "solar, consumo e armazenamento em bateria."
    )

    st.write(
        "A partir desses dados, um algoritmo simples "
        "analisa o cenário e define a estratégia de "
        "gerenciamento energético."
    )

    st.markdown(
        """
        **☀️ Geração Solar → 🤖 Gerenciamento → 🔋 Bateria → 🏢 Consumo**
        """
    )
