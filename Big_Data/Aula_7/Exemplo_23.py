Funcionario = float(input("Informe o valor que você recebe por hora: "))
horas_trabalhadas = int(input("Informe quantas horas você trabalha por mês: "))

calculo = Funcionario*horas_trabalhadas
print(f"Seu salário bruto no fim do mês será de: {calculo}")

desconto_IRRF = calculo * 0.89
print(f"Com o desconto do imposto IRRF o valor ficará: {desconto_IRRF:.2f}, você pagou ao IRRF: {calculo - desconto_IRRF:.2f}")

desconto_INSS = calculo * 0.92
print(f"Com o desconto do imposto INSS o valor ficará: {desconto_INSS:.2f}, você pagou ao INSS: {calculo - desconto_INSS:.2f}")

desconto_sindicato = calculo * 0.95
print(f"Com o desconto do imposto do sindicato o valor ficará: {desconto_sindicato:.2f}, você pagou ao sindicato: {calculo - desconto_sindicato:.2f}")

liquido = calculo - (desconto_IRRF + desconto_INSS + desconto_sindicato)
print(f"O salário liquido será: {liquido:.2f}")














