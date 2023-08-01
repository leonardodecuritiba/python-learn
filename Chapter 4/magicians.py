magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, thats was a great trick!")
    print(f"I cant wait for your next trick {magician.title()}!\n")
    
print("Thank you for the show!\n")

# Criando listas numéricas
# Devido ao comportamento off-by-one, o python imprime de 1 a 4
for value in range(1, 5):
    print(value)

print("\n")
# Para incluir o número 5:
for value in range(1, 6):
    print(value)

print("\n")
# Para iniciar do 0, passamos apenas um argumento para o range()
for value in range(6):
    print(value)

print("\n")
# Usando o range para retornar uma lista de números
numbers = list(range(1, 6))
print(numbers)

# usando o passo no range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# numeros quadráticos
square_numbers = []
for value in range(1, 11):
    square = value ** 2
    square_numbers.append(square)

print(square_numbers)

# Estatisticas simples
digits = list(range(1, 10))
digits.append(0)
print(digits)
print(f"MIN: {min(digits)}")
print(f"MAX: {max(digits)}")
print(f"SUM: {sum(digits)}")

# List Comprehension são listas cuja criação é combinada com um laço for
squares = [value**2 for value in range(1,11)]
print(f"List Comprehension: {squares}")
