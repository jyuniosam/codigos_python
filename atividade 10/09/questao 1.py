num = int(input("Digite um número de 0 a 100: "))

if 0 <= num <= 25:
    print(f"O número está na banda de 0 a 25.")
elif 26 <= num <= 50:
        print(f"O número está na banda de 26 a 50.")
elif 51 <= num <= 75:
        print(f"O número está na banda de 51 a 75.")
elif 76 <= num <= 100:
        print(f"O número está na banda de 76 a 100.")
else:
        print(f"Número fora da banda permitida.")
