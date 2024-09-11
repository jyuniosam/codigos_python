salario = float(input("relate o seu salário: "))

if salario <= 1900:
    imposto = 0
elif 1901 <= salario <= 2800:
        imposto = salario * 0.075
elif 2801 <= salario <= 3700:
        imposto = salario * 0.15
else:
        imposto = salario * 0.225
    
print(f"O imposto de renda é: R$ {imposto:.2f}")
