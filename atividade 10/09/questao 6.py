parcelas = int(input("Digivalor_compra = float(input("Digite o valor da compra: "))
te a quantidade de parcelas (de 1 a 24): "))

    print("Valor de cada parcela:", valor_parcela)
# Verificar se a quantidade de parcelas é válida
if parcelas < 1:
    print("Quantidade de parcelas inválida. Deve ser pelo menos 1.")
elif parcelas > 24:
    print("Quantidade de parcelas inválida. Deve ser no máximo 24.")
else:
    valor_parcela = valor_compra / parcelas
    if parcelas > 12:
        valor_parcela += 6
        valor_total = valor_compra + (valor_compra * 0.015) + (6 * (parcelas - 12))
    else:
        valor_total = valor_compra + (valor_compra * 0.015)
    
    print("Valor total a ser pago:", valor_total)