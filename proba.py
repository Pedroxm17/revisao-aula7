def calculo_nota(nota:float, quantidade:int):
    media = nota / quantidade
    return media

lista_alunos = []
soma_notas = 0
sair = 'nao'
quantidade_notas = 0

while sair == 'nao':
    quantidade_notas = int(input('Digite a quantidade de notas: '))
    for count in range (0, quantidade_notas):
        nota = float(input('Digite sua nota '))
        soma_notas  += nota
        
    resultado_media = calculo_nota(soma_notas, quantidade_notas)

    print(f'O resultado da media e {resultado_media}')
    lista_alunos.append(resultado_media)

    sair = (input('Sim deseja sair Digite sim , caso contrario digite nao '))
    
print(lista_alunos)
    

    
    
        
    
    
    
    
    