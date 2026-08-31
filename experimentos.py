import argparse
import random
from pathlib import Path

from algoritmos.genetico.individuo import gerar_populacao, avaliar_populacao
from algoritmos.genetico.selecao_roleta import selecionar_roleta


def carregar_instancia(caminho: str | Path) -> tuple[float, float, int, list[tuple[float, float]]]:

    linhas = [linha.split() for linha in Path(caminho).read_text().splitlines() if linha.strip()]

    largura, altura = map(float, linhas[0])
    quantidade_antenas = int(linhas[1][0])
    quantidade_pontos = int(linhas[2][0])

    pontos_demanda = [
        (float(x), float(y))
        for x, y in linhas[3:3 + quantidade_pontos]
    ]

    return largura, altura, quantidade_antenas, pontos_demanda


def main():

    parser = argparse.ArgumentParser(description="Roda uma geração (população + fitness + roleta) sobre uma instância.")
    parser.add_argument("instancia", type=Path, help="Caminho do arquivo de instância")
    parser.add_argument("raio_cobertura", type=float, help="Raio de cobertura de cada antena")
    parser.add_argument("--tamanho-populacao", type=int, default=30)
    parser.add_argument("--quantidade-pais", type=int, default=None, help="Padrão: metade da população")
    parser.add_argument("--seed", type=int, default=None, help="Padrão: aleatório a cada execução")
    args = parser.parse_args()

    quantidade_pais = args.quantidade_pais or args.tamanho_populacao // 2

    largura, altura, quantidade_antenas, pontos_demanda = carregar_instancia(args.instancia)

    gerador = random.Random(args.seed)
    populacao = gerar_populacao(args.tamanho_populacao, quantidade_antenas, largura, altura, gerador)
    avaliar_populacao(populacao, pontos_demanda, args.raio_cobertura)

    print(f"instancia: {args.instancia.name} | regiao {largura:.0f}x{altura:.0f} | {quantidade_antenas} antenas | {len(pontos_demanda)} pontos de demanda | raio {args.raio_cobertura}")
    print(f"fitness da populacao ({args.tamanho_populacao} individuos): {sorted(individuo.fitness for individuo in populacao)}")
    print(f"melhor individuo: {max(individuo.fitness for individuo in populacao)} de {len(pontos_demanda)} pontos cobertos")

    pais = selecionar_roleta(populacao, quantidade_pais, gerador)
    print(f"fitness dos {quantidade_pais} pais selecionados: {[pai.fitness for pai in pais]}")


if __name__ == "__main__":
    main()
