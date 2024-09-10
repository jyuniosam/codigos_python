idade = int(input("Informe a sua idade: "))

if idade < 12:
    print(f"Você é uma criança.")
elif 12 <= idade < 18:
        print(f"Você é um adolescente.")
elif 18 <= idade <= 60:
        print(f"Você é um adulto.")
elif idade > 60:
        print(f"Você é um idoso.")
