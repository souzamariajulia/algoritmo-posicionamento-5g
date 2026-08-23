from dataclasses import dataclass

Coordenada = tuple[float, float]

@dataclass
class Individuo:

    antenas: list[Coordenada]
    aptidao: float = 0.0
    