tarefas = []

for i in range (5):
tarefas = input(f"digite a tarefa {i+1}: ")
tarefas.append(tarefas)

print("\nsua lista de tarefas:")
for i , tarefa in enumerate(tarefas, start =1):
print(f"{i} - {tarefas}")