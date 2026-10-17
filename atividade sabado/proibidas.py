proibidas= ["spam","propaganda", "golpe"]
palavras = []

for i in range(5):
    p= input (f"digite a palavra {i+1}:")
    palavras.append(p)

bloqueados_count = 0 
for p in palavras:
    if p in rpoibidas:
        print(f"'{p}': bloqueada")
        bloqueadas_count += 1
else:
    print(f"'{p}': permitida")

    print(f"total de palavras bloqueadas:")