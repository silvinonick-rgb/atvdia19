convidados =[]

for i in range(8):
    nome  =input(f"digite o nome do convidado {i+1}: ")
if nome in convidados:
    print("aviso: convidado ja for cadastrado!")
else:
    convidados.append(nome)

print("lista final de convidados unicos:"convidados)