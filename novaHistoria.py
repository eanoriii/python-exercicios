import random

def gerar_introducao():
    introducoes = ["em um dia quente em sardenha", "na italia, a muito tempo atras", "em uma noite chuvosa, dentro do instituto agnes"]
    return random.choice(introducoes)

def gerar_desenvolvimento():
    desencolvimentos = [", Gaia,"  , ", Judith," , ", Vitor,", ", Corintio,", ", Nick,"]

    return random.choice(desencolvimentos)

def  gerar_conclusao():
    conclusoes = ["acabou sendo atacado(a) e se tornou vampiro(a)!", "acabou sendo deixado(a) para tra pois estava muito ferido(a) para continuar em combate", "se aposentou e esta vivendo do bem bom da vida!", "morreu por um vampiro aff :("]
    return random.choice(conclusoes)

def  gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    conclusao = gerar_conclusao()
    historia = f"{introducao} {desenvolvimento} {conclusao}"
    return historia

if __name__ ==  "__main__":
    print(gerar_historia())
