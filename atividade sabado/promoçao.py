preços = [25.0, 00.0, 15.0, 120.0, 45,0]
promoçao = []

for preço in preços:
    if preço > 50 :
     preço_com_desconto = preço * 0.90 #10% de desconto
    preço_com_append(preço_com_desconto)
else:
    promoçao.append(preços)

print(" preços originais :", preços)
print("preço em promoçao:", promoçao)