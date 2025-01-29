# Boas vindas ao usuário
print("Olá, bem vindo a sua calculadora")
user_name = input('Por favor, digite o seu nome: ')
print(f'Olá {user_name}, vamos começar?')

print('Para iniciarmos, digite abaixo a operação desejada, lembrando que serão realizadas somente operações básicas, como 1+9, 1*6, 2/5, 3-5)')

def calc_operation(math_operation): # Função para salvar o cálculo
 if '+' in math_operation:
  numbers = math_operation.split('+') # Separa os números
  result = float(numbers[0]) + float(numbers[1])
  print(f'O resultado é {result}')

 elif '-' in math_operation:
  numbers = math_operation.split('-') # Separa os números
  result = float(numbers[0]) - float(numbers[1])
  print(f'O resultado é {result}')

 elif '*' in math_operation:
  numbers = math_operation.split('*') # Separa os números
  result = float(numbers[0]) * float(numbers[1])
  print(f'O resultado é {result}')

 elif '/' in math_operation:
  numbers = math_operation.split('/') # Separa os números
  result = float(numbers[0]) / float(numbers[1])
  print(f'O resultado é {result}')

 else:
  print('Operação não permitida')

math_operation = input("Digite a operação: ") # Input para o usuário dizer a operação
calc_operation(math_operation) # Executa a função para realizar o cálculo do usuário
