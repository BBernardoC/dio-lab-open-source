

deposito = []
saque = []
def operacoes():
    conta = 0

    while True:
        comando = input("Digite um comando")
        
        match comando:
            case 'd':
                quantiaDeposito = float(input("Digite a quantia que deseja depositar"))
                deposito.append(quantiaDeposito)
                conta+=quantiaDeposito
            case 's':
                quantiaSaque = float(input("Digite a quantia que deseja sacar"))
                if quantiaSaque>conta:
                    print("Sem dinheiro suficiente")
                else:
                    conta-=quantiaSaque
                    saque.append(quantiaSaque)
                
            case 'e':
                if len(deposito)>0 or len(saque)>0:
                    print(f"movimento na conta:\nvalor na conta: R${conta}\nDepositos feitos {deposito}\nSaques feitos {saque}")
                else:
                    print("não foram realizadas movimentações")
            case _:
                print("Tente de novo!")
            
operacoes()