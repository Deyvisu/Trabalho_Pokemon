class Pokemon:
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        self._nome = nome
        self._especie = especie
        self._tipo = tipo
        self._hp = hp
        self._ataque = ataque
        self._defesa = defesa
        self._movimento = "Investida"

class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "aquatico"
        self._movimento = "Canhão de bolhas"

class Eletrico(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "eletrico"
        self._movimento = "Investida trovão"

class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "fogo"
        self._movimento = "Cinzas"

class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "grama"
        self._movimento = "Folha navalha"

class Pedra(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "pedra"
        self._movimento = "Rolamento"

class Fantasma(Pokemon):
    def __init__(self, nome, especie, tipo, hp, ataque, defesa):
        super().__init__(nome, especie, tipo, hp, ataque, defesa)

        self._tipo = "fantasma"
        self._movimento = "Pesadelo"

pokemonDisponivel = [
    Fogo("Cyndaquil", "Cyndaquil", "Fogo", 30, 15, 25),
    Aquatico("Totodile", "Totodile", "Aquático", 25, 15, 20),
    Eletrico("Electabuzz", "Electabuzz", "Elétrico", 40, 35, 30),
    Grama("Chikorita", "Chikorita", "Grama", 35, 15, 25),
    Pedra("Geodude", "Geodude", "Pedra", 30, 25, 50),
    Fantasma("Gastly", "Gastly", "Fantasma", 30, 40, 30)
]
