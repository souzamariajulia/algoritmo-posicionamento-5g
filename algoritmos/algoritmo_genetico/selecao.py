import random

from algoritmos.algoritmo_genetico.individuo import Individuo

def selecionar_por_roleta(
    populacao: list[Individuo],
    gerador: random.Random | None = None
) -> Individuo:

    if not populacao:
        raise ValueError("A populacao nao pode estar vazia.")

    for individuo in populacao:
        if individuo.aptidao < 0:
            raise ValueError("A aptidao nao pode ser negativa.")

    if gerador is None:
        gerador = random.Random()

    aptidao_total = sum(
        individuo.aptidao
        for individuo in populacao
    )

    if aptidao_total == 0:
        return gerador.choice(populacao)

    valor_sorteado = gerador.uniform(
        0,
        aptidao_total
    )

    aptidao_acumulada = 0.0

    for individuo in populacao:

        aptidao_acumulada += individuo.aptidao

        if valor_sorteado <= aptidao_acumulada:
            return individuo
        
    return populacao[-1]