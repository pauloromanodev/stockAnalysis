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
mes_1 = int((total_dias) / 12)
mes_3 = int((total_dias) / 4)
mes_6 = int((total_dias) / 2)
mes_12 = total_dias

print(f'Total de dias: {total_dias}')
print(f'12 meses: {mes_12}')
print(f'6 meses: {mes_6}')
print(f'3 meses: {mes_3} ')
print(f'1 mês: {mes_1}')

x_mes1 = total_dias - mes_1
x_mes3 = total_dias - mes_3
x_mes6 = total_dias - mes_6
x_mes12 = 0


#corre 3 meses
for x in lista_valor_abertura[x_mes12:]:
    valor_abertura += float(x)

    conta_linhas += 1

    valor_atual = float(x)
    

preco_medio = valor_abertura / mes_12

#print(f'Linhas válidas: {str(linhas_validas)}')
print(f'Preço médio: {str(preco_medio)}')
print(f'Valor atual: {str(valor_atual)}')
