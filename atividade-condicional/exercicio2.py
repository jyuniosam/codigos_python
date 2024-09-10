salario = float(input("informe seu salario: ="))

if salario < 600:
    aumento = salario*0.30
    novo_salario = salario + aumento
    print(f"o seu salário foi reajustao para{novo_salario: .2f}")

else:
    print(f"voce não tem direito a um reajuste.")
