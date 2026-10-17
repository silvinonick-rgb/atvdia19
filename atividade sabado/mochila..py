mochila = ["caderno","caneta","lapis","borracha","regua"]
item = input("Digite o nome do objeto que deseja retirar: ")

if item in mochila:
    mochila.remove(item)
    print("item removido com sucesso")

else:
    print("o objeto nao esta na mochila")
    print("mochila atualizada:",mochila) 
