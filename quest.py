# Se pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    a, b = 0, 1

    while a <= num:
        if a == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b

    return f"O número {num} não pertence à sequência de Fibonacci."

print(pertence_fibonacci(21))  
print(pertence_fibonacci(22))  

# recorrencia de string
def recorrencia(s):
    s = s.lower()
    qtd = s.count('a')

    if qtd == 0:
        print('Não há recorrência de a') 
    else:
        print(f'A quantidade de a é {qtd}')

    return 

recorrencia('aaaaaa')
recorrencia('abadpḱ')
recorrencia('hgiorthg')