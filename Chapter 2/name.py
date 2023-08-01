name = "ada lovelace"
print(name.title())

# ==============================================================================
# PÁG. 54
first_name = "ada"
last_name = "lovelace"
# f é chamado f-strings, f é de formato, nesse caso, o Python converte o nome da
# variável entre chaves para seu o valor
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)

# PÁG. 62
universe_age = 14_000_000_000
print(universe_age)

# Atribuição rápida
x, y, z = 0, 0, 0
print(x, y, z)

# Constantes, usam letras maiúsculas para indicar constantes
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
