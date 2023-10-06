# Desafio
# Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# Entrada
# A entrada contém um único valor inteiro.
# Saída
# Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.






def Month():
    month_dic = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 
                'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    month = input(' ')

    if month.isdigit():
        month_number = int(month)
        if 1 <= month_number <= 12:
            for m, num in month_dic.items():
                if num == month_number:
                    print(m)
    else:
        print()
Month()

