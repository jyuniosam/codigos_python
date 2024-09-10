horasT = int(input("informe os numeros de horas trabalhadas: "))
valorH = int(input("informe o valor por hora: "))

if horasT > 40:
    horasT = 40
    valorH = horas_trabalhadas - 40
    salario_base = horas_normais * valorH
    bonus_extra = horas_extras * valorH * 1.5

else:
    horasT = horas_trabalhadas
    valorH = 0
    salario_base = horas_normais * valorH
    bonus_extras =  0

salario_total = salario_base + bonus_extra

print(f"o salario total é: R${salario_total:.2f}")
