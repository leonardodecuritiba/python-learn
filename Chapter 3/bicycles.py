# LISTAS
# Um exemplo simples contendo uma lista de bicicletas
# PÁG 68
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[-1]) # Imprime o último item
print(bicycles[-2]) # Imprime o penúltimo item

# Anexando itens a uma lista ========================
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Anexando itens ao final da lista
motorcycles.append('ducati')
print(motorcycles)

# Inserindo no início de uma lista
motorcycles.insert(0, 'bmw')
print(motorcycles)

# Removendo um elemento com del, com índice ========================
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removendo um elemento com pop (final da lista) ========================
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Removendo elementos de qualquer posição da lista ========================
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"First motorcycle popped was {first_owned.title()}")


# Removendo um elemento por valor ========================
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
print(motorcycles)
motorcycles.remove(too_expensive)
print(motorcycles)
print( f"\nA {too_expensive.title()} is too expensive for me")


# Organizando uma lista
print("\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # sort altera permanentemente a ordem da lista
print(cars)

# ordenando em ordem alfabética reversa
cars.sort(reverse=True)
print(cars)

# ordenanando temporariamente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True)) # em ordem reversa

# organizando de maneira reversa (sem ordem alfabética)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# identificando o tamanho de uma lista
print(len(cars))