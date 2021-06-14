import csv

linhas_validas = 0
lista_valor_abertura = []
valor_abertura = 0
conta_linhas = 0

qtd_meses = input('Digite o período de meses (máx 12): ')


with open('SBSP3.SA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')    
    
    
    for row in csv_reader:
        
        if row[6] != 0 and row[6] != 'null' and linhas_validas != 0:            
            linhas_validas += 1 
            lista_valor_abertura.insert(len(lista_valor_abertura), row[1])
        else:
            linhas_validas += 1


total_dias = len(lista_valor_abertura)

qtd_dias = int(total_dias) / (12 / int(qtd_meses))

print(f'Total de dias geral: {total_dias}')
print(f'Total de dias selecionado: {qtd_dias}')
print(f'Período: {qtd_meses} meses')

var_mes = int(total_dias) - int(qtd_dias)

print(f'var_mes:  {var_mes}')

if var_mes == 0:
    var_mes = 1

for x in lista_valor_abertura[var_mes:]:
    valor_abertura += float(x)

    conta_linhas += 1

    valor_atual = float(x)


print(valor_abertura)

preco_medio = float(valor_abertura) / int(qtd_dias)

print(f'Preço médio: {str(preco_medio)}')
print(f'Valor atual: {str(valor_atual)}')