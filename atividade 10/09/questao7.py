nota_final = float(input("informe a nota final do aluno: "))
frequencia = float(input("informe a frequencia do aluno em %: "))

if nota_final >= 7 and frequencia >= 75:
    print(f"O aluno está aprovado.")

else:
    print(f"O aluno está reprovado.")