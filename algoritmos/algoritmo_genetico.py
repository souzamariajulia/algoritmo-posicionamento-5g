import random
from dataclasses import dataclass


@dataclass
class Individuo:
    antenas: list[tuple[float, float]]
    fitness: int = 0


def gerar_populacao(tamanho_populacao: int, quantidade_antenas: int, largura_regiao: float, altura_regiao: float, gerador: random.Random) -> list[Individuo]:

    return [
        Individuo(antenas=[
            (gerador.uniform(0, largura_regiao), gerador.uniform(0, altura_regiao))
            for _ in range(quantidade_antenas)
        ])
        for _ in range(tamanho_populacao)
    ]


def calcular_fitness(individuo: Individuo, pontos_demanda: list[tuple[float, float]], raio_cobertura: float) -> int:

    raio_quadrado = raio_cobertura ** 2

    return sum(
        any((ponto_x - antena_x) ** 2 + (ponto_y - antena_y) ** 2 <= raio_quadrado for antena_x, antena_y in individuo.antenas)
        for ponto_x, ponto_y in pontos_demanda
    )


def avaliar_populacao(populacao: list[Individuo], pontos_demanda: list[tuple[float, float]], raio_cobertura: float) -> None:

    for individuo in populacao:
        individuo.fitness = calcular_fitness(individuo, pontos_demanda, raio_cobertura)


def selecionar_individuos(populacao: list[Individuo], quantidade: int, gerador: random.Random) -> list[Individuo]:

    pesos = [individuo.fitness for individuo in populacao]

    if sum(pesos) == 0:
        pesos = None

    return gerador.choices(populacao, weights=pesos, k=quantidade)
