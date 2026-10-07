import time
import sys
import os

# Garante que o diretório raiz do projeto esteja no sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.simulation import gerar_dados
from src.energy_manager import gerenciar_energia
from src.calculations import calcular_economia, calcular_co2


def exibir_barra_progresso(porcentagem, largura=25):
    """Gera uma barra visual ASCII para percentuais."""
    preenchido = int(largura * (porcentagem / 100))
    barra = "█" * preenchido + "░" * (largura - preenchido)
    return f"[{barra}] {porcentagem}%"


def exibir_grafico_comparativo(geracao, consumo, escala_max=12):
    """Exibe um gráfico de barras horizontal comparando geração e consumo."""
    largura = 30
    bar_geracao = "█" * int(min(geracao / escala_max, 1.0) * largura)
    bar_consumo = "█" * int(min(consumo / escala_max, 1.0) * largura)

    print("\n📊 GRÁFICO COMPARATIVO (Geração vs Consumo)")
    print(f"  ☀️  Geração Solar : {bar_geracao:<30} ({geracao:.2f} kW)")
    print(f"  ⚡  Consumo       : {bar_consumo:<30} ({consumo:.2f} kW)")


def executar_ciclo(geracao=None, consumo=None, bateria=None, ciclo_num=None):
    """Executa a simulação e imprime o relatório completo no terminal."""
    if geracao is None or consumo is None or bateria is None:
        geracao, consumo, bateria = gerar_dados()

    decisao = gerenciar_energia(geracao, consumo, bateria)
    energia_rede, custo = calcular_economia(geracao, consumo, bateria)
    co2 = calcular_co2(geracao, consumo)
    energia_renovavel = min(geracao, consumo)

    print("\n" + "=" * 65)
    if ciclo_num:
        print(f"☀️  GOODWE SMART ENERGY — RELATÓRIO DO CICLO #{ciclo_num}")
    else:
        print("☀️  GOODWE SMART ENERGY — RELATÓRIO DE MONITORAMENTO")
    print("=" * 65)

    # Monitoramento
    print("\n📡 DADOS COLETADOS:")
    print(f"  • Geração Solar Fotovoltaica : {geracao:.2f} kW")
    print(f"  • Demanda de Consumo Local   : {consumo:.2f} kW")
    print(f"  • Nível da Bateria (SoC)     : {exibir_barra_progresso(bateria)}")
    print(f"  • Energia Importada da Rede  : {energia_rede:.2f} kWh")

    # Gráfico
    exibir_grafico_comparativo(geracao, consumo)

    # Decisão
    print("\n🤖 DECISÃO INTELIGENTE DO SISTEMA (GOODWE ESS):")
    print(f"  👉 Ação recomendada: [{decisao.upper()}]")

    # Análise Técnica
    print("\n🧠 ANÁLISE DE FLUXO ENERGÉTICO:")
    if geracao > consumo:
        excedente = geracao - consumo
        if bateria < 100:
            print(f"  • Excedente solar de {excedente:.2f} kW direcionado para recarga do banco de baterias.")
        else:
            print(f"  • Bateria 100% carregada! Excedente de {excedente:.2f} kW injetado na rede para créditos.")
    elif geracao < consumo:
        falta = consumo - geracao
        if bateria > 20:
            print(f"  • Déficit solar de {falta:.2f} kW atendido pelo descarregamento seguro da bateria.")
        else:
            print(f"  • Bateria no limite de segurança (<=20%). Rede elétrica acionada para suprir {falta:.2f} kW.")
    else:
        print("  • Equilíbrio perfeito: geração solar atende exatamente a demanda de consumo.")

    # Indicadores e Sustentabilidade
    print("\n🌱 INDICADORES DE SUSTENTABILIDADE & ECONOMIA:")
    print(f"  • Autoconsumo Solar Direto : {energia_renovavel:.2f} kWh")
    print(f"  • Redução de Emissões (CO₂) : {co2:.2f} kg de CO₂ evitados")
    print(f"  • Custo da Energia da Rede : R$ {custo:.2f} (Tarifa ref: R$ 0.85/kWh)")
    print("=" * 65)


def simulacao_continua(qtd_ciclos=5):
    """Executa múltiplos ciclos simulando a passagem do tempo."""
    print(f"\n🔄 Iniciando Simulação Contínua ({qtd_ciclos} ciclos)...")
    total_solar = 0.0
    total_consumo = 0.0
    total_co2 = 0.0
    total_custo = 0.0

    for i in range(1, qtd_ciclos + 1):
        geracao, consumo, bateria = gerar_dados()
        energia_rede, custo = calcular_economia(geracao, consumo, bateria)
        co2 = calcular_co2(geracao, consumo)

        total_solar += geracao
        total_consumo += consumo
        total_co2 += co2
        total_custo += custo

        executar_ciclo(geracao, consumo, bateria, ciclo_num=i)
        if i < qtd_ciclos:
            time.sleep(1.2)

    print("\n" + "#" * 65)
    print("📈 RESUMO CONSOLIDADO DO PERÍODO:")
    print(f"  • Total de Energia Solar Gerada : {total_solar:.2f} kWh")
    print(f"  • Total de Consumo Demandado    : {total_consumo:.2f} kWh")
    print(f"  • Total de CO₂ Evitado          : {total_co2:.2f} kg")
    print(f"  • Custo Total com Rede Elétrica : R$ {total_custo:.2f}")
    print("#" * 65 + "\n")


def inserir_dados_manualmente():
    """Permite testar cenários específicos com valores inseridos pelo usuário."""
    print("\n📝 INSERÇÃO DE DADOS PERSONALIZADOS:")
    try:
        geracao = float(input("  Digite a Geração Solar (kW) [ex: 5.5]: "))
        consumo = float(input("  Digite o Consumo Local (kW) [ex: 3.2]: "))
        bateria = int(input("  Digite o Nível da Bateria (%) [0 a 100]: "))

        if bateria < 0 or bateria > 100:
            print("  ⚠️ Nível de bateria inválido. Utilizando 50%.")
            bateria = 50

        executar_ciclo(geracao, consumo, bateria)
    except ValueError:
        print("  ❌ Entrada inválida. Digite apenas números.")


def exibir_sobre():
    """Exibe informações do projeto e alinhamento GoodWe."""
    print("\n" + "=" * 65)
    print("ℹ️ SOBRE O PROJETO GOODWE SMART ENERGY")
    print("=" * 65)
    print("• Disciplina / Desafio : Sprint 4 — Solução Final Integrada")
    print("• Foco                 : Gerenciamento inteligente de energia renovável")
    print("• Tecnologia GoodWe    : Emulação de inversores híbridos e ESS")
    print("• Benefícios           : Otimização de autoconsumo, corte de picos,")
    print("                         preservação da bateria e redução de carbono.")
    print("=" * 65)


def menu():
    """Menu principal executado no console."""
    while True:
        print("\n" + "╔" + "═" * 45 + "╗")
        print("║      ☀️  GOODWE SMART ENERGY SYSTEM       ║")
        print("║   Gestão e Otimização de Energia Renovável  ║")
        print("╚" + "═" * 45 + "╝")
        print("  [1] Executar Nova Simulação (1 Ciclo)")
        print("  [2] Executar Simulação Contínua (5 Ciclos)")
        print("  [3] Testar Cenário Personalizado (Manual)")
        print("  [4] Sobre o Projeto e Tecnologias GoodWe")
        print("  [0] Sair")

        opcao = input("\n👉 Escolha uma opção: ").strip()

        if opcao == "1":
            executar_ciclo()
        elif opcao == "2":
            simulacao_continua()
        elif opcao == "3":
            inserir_dados_manualmente()
        elif opcao == "4":
            exibir_sobre()
        elif opcao == "0":
            print("\n👋 Encerrando o GoodWe Smart Energy. Até logo!\n")
            break
        else:
            print("❌ Opção inválida! Escolha entre 0 e 4.")
            break


if __name__ == "__main__":
    menu()
