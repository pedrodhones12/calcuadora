def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica para evitar divisão por zero
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return "Erro: operação inválida"
