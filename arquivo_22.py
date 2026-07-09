#Construindo tabelas dinâmicas com Pretty Table!


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Estabelecimentos",
                 ["A", "B", "C"])

table.add_column("Type", ["Restaurante", "Lanchonete", "Loja de comércio"])

print(table.align)
table.align = "l"
print(table)


