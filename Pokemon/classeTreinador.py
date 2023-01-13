import random
import classePokemon

listaNomes = ("José", "Maria", "Marcos", "Charles", "Deyvison")

class Treinador:
    def __init__(self, nome ="", pokemons=[]):
        self._pokemons = pokemons
        if nome == "":
            self._nome = random.choice(listaNomes)
        else:
            self._nome = nome

    def escolherPokemon(self):
        return random.choice(self._pokemons)

    def mostrarPokemons(self):
        print(f"O treinador {self._nome} possui os seguintes pokemons: ")
        for i in range(len(self._pokemons)):
            print(f"{i+1}. {self._pokemons[i]._nome}") 
            
        print("------------------------------------------------------------------")
        
    def capturarPokemon(self):
        if len(self._pokemons)<6:
            pokemonCapturado = random.choice(classePokemon.pokemonDisponivel)
            self._pokemons.append(pokemonCapturado)
            print(f"Capturei o {pokemonCapturado._nome}")
        else:
            print("O treinador já tem pokemons demais!")

class Jogador(Treinador):
    def __init__(self, nome="", pokemons=[]):
        super().__init__(nome, pokemons)

        if (len(self._pokemons) == 0):
            print("""Escolha um dos seguintes pokemons iniciais:
            1 - Chikorita
            2 - Totodile
            3 - Cyndaquil""")
            pokemonEscolhido = input("Sua escolha: ")

            match pokemonEscolhido:
                case "1":
                    self._pokemons.append(classePokemon.Grama("Chikorita", "Chikorita", "Grama", 35, 15, 25))
                    print("Você escolheu o Chikorita")
                case "2":
                    self._pokemons.append(classePokemon.Aquatico("Totodile", "Totodile", "Aquático", 25, 15, 20))
                    print("Você escolheu o Totodile")
                case "3":
                    self._pokemons.append(classePokemon.Fogo("Cyndaquil", "Cyndaquil", "Fogo", 30, 15, 25))
                    print("Você escolheu o Cyndaquil")
                case _:
                    print("Você não escolheu um pokemon válido!")

    def escolherPokemonJogador(self):
        while True:
            print(f"Escolha seu pokemon para batalhar: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")
            
            pokeBatalha = input("Digite o numero do pokemon a sua escolha: ")
            return self._pokemons[int(pokeBatalha)-1]
    
    def batalhaPokemon(self, inimigo):
        meuPokemon = self.escolherPokemonJogador()

        match meuPokemon._especie:
            case "Totodile":
                meuPokemon._ataque = random.randint(20,30)
                meuPokemon._defesa = random.randint(20,30)
                meuPokemon._hp = random.randint(20,30)

            case "Cyndaquil":
                meuPokemon._ataque = random.randint(40,50)
                meuPokemon._defesa = random.randint(40,50)
                meuPokemon._hp = random.randint(40,50)

            case "Electabuzz":
                meuPokemon._ataque = random.randint(30,40)
                meuPokemon._defesa = random.randint(30,40)
                meuPokemon._hp = random.randint(30,40)
            
            case "Chikorita":
                meuPokemon._ataque = random.randint(30,40)
                meuPokemon._defesa = random.randint(30,40)
                meuPokemon._hp = random.randint(30,40)
                    
            case "Geodude":
                meuPokemon._ataque = random.randint(30,40)
                meuPokemon._defesa = random.randint(30,40)
                meuPokemon._hp = random.randint(30,40)
                    
            case "Gastly": 
                meuPokemon._ataque = random.randint(20,30)
                meuPokemon._defesa = random.randint(20,30)
                meuPokemon._hp = random.randint(20,30)
                

        print(f"Meu Pokemon:", meuPokemon._nome)

        pokemonInimigo = random.choice(classePokemon.pokemonDisponivel)

        match pokemonInimigo._especie:
            case "Totodile":
                pokemonInimigo._ataque = random.randint(20,30)
                pokemonInimigo._defesa = random.randint(20,30)
                pokemonInimigo._hp = random.randint(20,30)

            case "Cyndaquil":
                pokemonInimigo._ataque = random.randint(20,30)
                pokemonInimigo._defesa = random.randint(20,30)
                pokemonInimigo._hp = random.randint(20,30)

            case "Electabuzz":
                pokemonInimigo._ataque = random.randint(30,40)
                pokemonInimigo._defesa = random.randint(30,40)
                pokemonInimigo._hp = random.randint(30,40)

            case "Chikorita":
                pokemonInimigo._ataque = random.randint(20,30)
                pokemonInimigo._defesa = random.randint(20,30)
                pokemonInimigo._hp = random.randint(20,30)
                
            case "Geodude":
                pokemonInimigo._ataque = random.randint(30,40)
                pokemonInimigo._defesa = random.randint(30,40)
                pokemonInimigo._hp = random.randint(30,40)
                
            case "Gastly": 
                pokemonInimigo._ataque = random.randint(20,30)
                pokemonInimigo._defesa = random.randint(20,30)
                pokemonInimigo._hp = random.randint(20,30)
                

        print("Pokemon inimigo:", pokemonInimigo._nome)


        meuPokemonForca = meuPokemon._ataque + meuPokemon._defesa + meuPokemon._hp
        pokemonInimigoForca = pokemonInimigo._ataque + pokemonInimigo._defesa + pokemonInimigo._hp

        if(meuPokemonForca > pokemonInimigoForca):
            print(f"Ganhei! Meu pokemon {meuPokemon._nome} ganhou o duelo com força {meuPokemonForca}")
        elif(meuPokemonForca < pokemonInimigoForca):
            print(f"Perdi! O pokemon inimigo {pokemonInimigo._nome} ganhou o duelo com força {pokemonInimigoForca}")
        else:
            print("Empatou!!!! As forças dos pokemon são iguais:", "Força do meu pokemon:", meuPokemonForca,", força do pokemon inimigo: ",pokemonInimigoForca)


class Inimigo(Treinador):
    def __init__(self, pokemons):
        super().__init__(pokemons)


#if __name__ == "__main__":