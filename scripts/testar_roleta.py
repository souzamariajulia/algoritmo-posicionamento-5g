import random
from collections import Counter

from algoritmos.algoritmo_genetico.individuo import Individuo
from algoritmos.algoritmo_genetico.selecao import selecionar_por_roleta

def main():

    individuo_1 = Individuo(
        antenas=[(10, 10)],
        aptidao=10
    )

    individuo_2 = Individuo(
        antenas=[(20, 20)],
        aptidao=5
    )

    individuo_3 = Individuo(
        antenas=[(30, 30)],
        aptidao=20
    )

    populacao = [
        individuo_1,
        individuo_2,
        individuo_3
    ]

    gerador = random.Random(42)

    quantidade_execucoes = 10_000

    resultados = []

    for _ in range(quantidade_execucoes):

        selecionado = selecionar_por_roleta(
            populacao,
            gerador
        )

        resultados.append(
            selecionado.aptidao
        )

    contagem = Counter(resultados)

    print("Resultado da roleta:\n")

    for individuo in populacao:

        quantidade = contagem[individuo.aptidao]

        porcentagem = (
            quantidade / quantidade_execucoes
        ) * 100

        print(
            f"Aptidao {individuo.aptidao:>5}: "
            f"{quantidade:>5} selecoes "
            f"({porcentagem:.2f}%)"
        )


if __name__ == "__main__":
    main()