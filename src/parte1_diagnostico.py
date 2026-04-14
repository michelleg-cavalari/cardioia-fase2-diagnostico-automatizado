import csv
from collections import Counter

# Caminhos dos arquivos
ARQUIVO_FRASES = "data/frases_sintomas.txt"
ARQUIVO_MAPA = "data/mapa_conhecimento.csv"


def carregar_frases(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        frases = [linha.strip() for linha in arquivo if linha.strip()]
    return frases


def carregar_mapa_conhecimento(caminho):
    mapa = []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            mapa.append({
                "sintoma1": linha["sintoma1"].lower(),
                "sintoma2": linha["sintoma2"].lower(),
                "doenca": linha["doenca"]
            })
    return mapa


def identificar_sintomas_e_diagnostico(frase, mapa):
    frase_lower = frase.lower()
    sintomas_encontrados = []
    diagnosticos = []

    for item in mapa:
        encontrou_1 = item["sintoma1"] in frase_lower
        encontrou_2 = item["sintoma2"] in frase_lower

        if encontrou_1:
            sintomas_encontrados.append(item["sintoma1"])
        if encontrou_2:
            sintomas_encontrados.append(item["sintoma2"])

        if encontrou_1 or encontrou_2:
            diagnosticos.append(item["doenca"])

    if diagnosticos:
        diagnostico_final = Counter(diagnosticos).most_common(1)[0][0]
    else:
        diagnostico_final = "Diagnóstico não identificado"

    return list(set(sintomas_encontrados)), diagnostico_final


def main():
    frases = carregar_frases(ARQUIVO_FRASES)
    mapa = carregar_mapa_conhecimento(ARQUIVO_MAPA)

    print("=" * 60)
    print("CARDIOIA - DIAGNÓSTICO AUTOMATIZADO")
    print("=" * 60)

    for i, frase in enumerate(frases, start=1):
        sintomas, diagnostico = identificar_sintomas_e_diagnostico(frase, mapa)

        print(f"\nPaciente {i}")
        print(f"Frase: {frase}")
        print(f"Sintomas identificados: {', '.join(sintomas) if sintomas else 'Nenhum'}")
        print(f"Diagnóstico sugerido: {diagnostico}")


if __name__ == "__main__":
    main()
