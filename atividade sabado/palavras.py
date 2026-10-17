palavras = ["sol","computador","casa","programaçao","pe","python"]
palavras_grandes =[]

for p in palavras:
    if len(p) >=5:
        palavras_grandes.append(p)

print("palavras com 5 ou mais caracteristicas:",palavras_grandes)