import random
from dataclasses import dataclass


@dataclass
class Individuo:
    antenas: list[tuple[float, float]]
    fitness: int = 0
    probabilidade: float = 0.0


def gerar_populacao(tamanho_populacao: int, quantidade_antenas: int, largura_regiao: float, altura_regiao: float, gerador: random.Random) -> list[Individuo]:

    populacao = []

    for _ in range(tamanho_populacao):

        antenas = []

        for _ in range(quantidade_antenas):

            x = gerador.uniform(0, largura_regiao)
            y = gerador.uniform(0, altura_regiao)

            antenas.append((x, y))

        populacao.append(
            Individuo(antenas=antenas)
        )

    return populacao


def calcular_fitness(individuo: Individuo, pontos_demanda: list[tuple[float, float]], raio_cobertura: float) -> int:
  
    pontos_cobertos = 0
    raio_quadrado = raio_cobertura ** 2

    for ponto_x, ponto_y in pontos_demanda:

        for antena_x, antena_y in individuo.antenas:

            distancia_quadrada = ((ponto_x - antena_x) ** 2 + (ponto_y - antena_y) ** 2)
            if distancia_quadrada <= raio_quadrado:
                pontos_cobertos += 1
                break

    return pontos_cobertos


def avaliar_populacao(populacao: list[Individuo], pontos_demanda: list[tuple[float, float]], raio_cobertura: float) -> None:
    
    for individuo in populacao:

        individuo.fitness = calcular_fitness( individuo, pontos_demanda, raio_cobertura)


def calcular_probabilidades( populacao: list[Individuo]) -> None:

    fitness_total = sum(
        individuo.fitness
        for individuo in populacao
    )

    if fitness_total == 0:

        probabilidade_igual = 1 / len(populacao)

        for individuo in populacao:
            individuo.probabilidade = probabilidade_igual

        return

    for individuo in populacao:

        individuo.probabilidade = (
            individuo.fitness / fitness_total
        )


def selecionar_por_roleta(populacao: list[Individuo], gerador: random.Random) -> Individuo:

    numero_sorteado = gerador.random()

    probabilidade_acumulada = 0.0

    for individuo in populacao:

        probabilidade_acumulada += individuo.probabilidade

        if numero_sorteado <= probabilidade_acumulada:
            return individuo

    return populacao[-1]


def selecionar_individuos(populacao: list[Individuo], quantidade: int, gerador: random.Random) -> list[Individuo]:
   
    selecionados = []

    for _ in range(quantidade):

        individuo = selecionar_por_roleta(
            populacao,
            gerador
        )

        selecionados.append(individuo)

    return selecionados