meme_dict = {
            "XITADO": "quando você acha que alguem esta trapaceando",
            "200": "no Fortnite significa quando você dá um tiro de 200 de dano ou mais",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("palavra não encontrada. vc foi moggado pelo beta")
