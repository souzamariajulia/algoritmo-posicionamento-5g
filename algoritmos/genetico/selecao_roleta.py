import random

from .individuo import Individuo


def selecionar_roleta(populacao: list[Individuo], quantidade: int, gerador: random.Random) -> list[Individuo]:

    pesos = [individuo.fitness for individuo in populacao]

    if sum(pesos) == 0:
        pesos = None

    return gerador.choices(populacao, weights=pesos, k=quantidade)
