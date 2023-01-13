import classePokemon
import classeTreinador


treinador = classeTreinador.Treinador()
jogador = classeTreinador.Jogador()
treinadorInimigo = classeTreinador.Inimigo(classePokemon.pokemonDisponivel)

while (True):

   menu = input("""Escolha a ação que você quer executar:
      1 - Captura pokemon
      2 - Exibir pokemons
      3 - Batalhar
      4 - Sair do jogo
      
      Sua escolha: """)


   match menu:
      case "1":
         if (len(jogador._pokemons)>=6):
            print("Você já possui o limite de pokemons por time!")
            print("---------------------------------------------------------------------------")
         else:
            jogador.capturarPokemon()
            
         jogador.mostrarPokemons()
      case "2":
         jogador.mostrarPokemons()
      case "3":
         jogador.batalhaPokemon(treinadorInimigo)
         print("---------------------------------------------------------------------------")
      case "4":
         print("Você saiu do joguinho, volte sempre!")
         print("---------------------------------------------------------------------------")
         break
