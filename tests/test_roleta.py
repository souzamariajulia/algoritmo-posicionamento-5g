import random
from collections import Counter

import pytest

from algoritmos.algoritmo_genetico.individuo import Individuo
from algoritmos.algoritmo_genetico.selecao import selecionar_por_roleta


def test_roleta_prioriza_individuos_com_maior_aptidao():
    """
    Verifica se o método da roleta seleciona com maior
    frequência os indivíduos que possuem maior aptidão.
    """

    populacao = [
        Individuo(
            antenas=[(10, 10)],
            aptidao=10
        ),
        Individuo(
            antenas=[(20, 20)],
            aptidao=5
        ),
        Individuo(
            antenas=[(30, 30)],
            aptidao=20
        )
    ]

    gerador = random.Random(42)

    resultados = []

    for _ in range(10_000):
        selecionado = selecionar_por_roleta(
            populacao,
            gerador
        )

        resultados.append(
            selecionado.aptidao
        )

    contagem = Counter(resultados)

    assert contagem[20] > contagem[10]
    assert contagem[10] > contagem[5]


def test_roleta_nao_aceita_populacao_vazia():

    with pytest.raises(ValueError):
        selecionar_por_roleta([])


def test_roleta_nao_aceita_aptidao_negativa():
    """
    Verifica se indivíduos com aptidão negativa
    não são aceitos pela seleção por roleta.
    """

    populacao = [
        Individuo(
            antenas=[(10, 10)],
            aptidao=-5
        )
    ]


    with pytest.raises(ValueError):
        selecionar_por_roleta(populacao)