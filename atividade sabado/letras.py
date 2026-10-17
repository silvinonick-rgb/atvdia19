palavras= []
for in range (8):
    p= input(f"Digite a palavra  {i+1}: ")
    palavras.append(p)

palavras_com_a =[]
for p in palavras:
    # .upper()garante que considere tanto'a' quanto 'A'
    if p [0].upper = 'A':
palavras_com_a.append(p)

print("palavras que começamcom A :", palavras_com_a)