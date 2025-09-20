nomes = ["João", "Maria", "Pedro", "Ana"]
for i in range(len(nomes)):
    if len(nomes[i]) > 4:
        print(f"{nomes[i]} tem mais de 4 letras.")
    else:
        print(f"{nomes[i]} tem 4 ou menos letras.")