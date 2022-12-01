from abc import ABC, abstractclassmethod,abstractproperty
       
clientes = []  
contas =[]  
valida =[]
class Conta:
    def __init__(self, _saldo,_numero,_agencia,_cliente, _historico):
        self._saldo = _saldo
        self._numero = _numero
        self._agencia = _agencia
        self._cliente = _cliente
        self._historico= _historico

    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

  
            

  


class Conta_corrente(Conta):
    def __init__(self, _saldo, _numero, _agencia, _cliente, _historico, _limite, _limite_saque):
        super().__init__(_saldo, _numero, _agencia, _cliente, _historico)
        self._limite=_limite
        self._limite_saque = _limite_saque
    def criarConta(cpf_valor):
        return Conta_corrente(
            _saldo= int(input("Informe o saldo")),
            _numero= len(contas)+1,
            _agencia = "001",
            _cliente = cpf_valor,
            _historico = "",
            _limite= 1000,
            _limite_saque = 3

        )
    def depositar(cpf_valor):
        
        for conta in contas:
           
            if conta._cliente==cpf_valor:
                valor_deposito = int(input("Informe o valor"))
                if valor_deposito<0:
                    print("valor invalido")
                else:
                    conta._saldo += valor_deposito
                    conta._historico += f" Deposito realizado com sucesso no valor de R${valor_deposito:.2f}- O Saldo em conta é de R$ {conta._saldo:.2f}"
                    print(f"<<<Deposito realizado no valor de R${valor_deposito:.2f} realizado com sucesso!! Seu saldo em conta é de R$ {conta._saldo:.2f}>>>")
            
                
            else:
                return  input("Informe cpf : //")

    def sacar(cpf):
                for conta in contas:
                    if conta._cliente==cpf:
                        valor_saque = int(input(" Informe o valor do saque :"))
                        print(conta._limite)
                        if conta._limite>=3:
                           
                            if conta._saldo >= valor_saque:
                                 conta._saldo -= valor_saque
                                 conta._limite_saque-=1
                                 print(f" <<<Saque realizado com  sucesso - Saldo Atual :R$ {conta._saldo:.2f} Limite de Saque : {conta._limite_saque}>>>")
                                 conta._historico += (f" \n Saque realizado - no valor de R$ {valor_saque:.2f} Saldo da conta R$ {conta._saldo:.2f} ")
                            elif conta._saldo <valor_saque:
                                if conta._limite + conta._saldo >= valor_saque:
                                    resto = conta._saldo - valor_saque
                                    conta._saldo -= valor_saque
                                    conta._limite += resto
                                    print(f" Limite da conta :{conta._limite:.2f} - Saldo da Conta R$ {conta._saldo:.2f}")
                            else:
                                print(f"valor maior que o saldo - O valor do saque deve ser inferior")

                        else:
                          print("Passou  do limite")
                    else:
                        print("CPF não encontrado")
    def historico(cpf):
        for conta in contas:
            if conta._cliente==cpf:
                print(conta._historico)   
            else:
                print("CPf não encontrado")         


class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        

    pass

class PessoaFisica(Cliente):
     def __init__(self,cpf, nome, data_nascimento,endereco):
        super().__init__(endereco)
        self.cpf= cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.lista_usuario = []
     def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    
     def criar_usuario(valor):
        
                       
        return PessoaFisica(
        cpf = valor, 
        nome = input("Informe o nome: "),
        data_nascimento = input("Informe nascimento: "),
        endereco = input("Informe endereco: ")
        
        )
     def verifica_cpf(valor_cpf):
        print(valor_cpf)
        for cliente in clientes:
          
            if cliente.cpf==valor_cpf:
                return 1
          
       
     def listar_usuario(self, lista_usuario):
        print(lista_usuario)

    
  


    

#cliente1= PessoaFisica("0907121802","fernanda","21101981","rua cdomendador","conta0001")
#print(cliente1)
#metodo construtor  ???

#inserir o input no Pyhton class

menu= """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuario
[a] Abrir Conta
[b] Listar Contas
[u] Listar Usuários
[q] Sair \n Informe uma opção :"""


while True :
    opcao = input(menu)
    if opcao=='d':
        print(cpf)
        Conta_corrente.depositar(cpf)     
         
            
    elif opcao =='s':
        print(cpf)
        Conta_corrente.sacar(cpf)

      
        
    elif opcao == 'e':
        print(cpf)
        Conta_corrente.historico(cpf)
       
    
    elif opcao =='c':
        cpf = input("Informe o cpf:")
       
        if PessoaFisica.verifica_cpf(cpf)==1:
            print("cpf já existe- não pode cadastrar o mesmo cpf")  
        else:  
            clientes.append( PessoaFisica.criar_usuario(cpf))
       

         
    
    
    elif opcao =='a':
        cpf = input("Informe o cpf:")
       
       
        if PessoaFisica.verifica_cpf(cpf)!=1:
          print(" CPF não cadastrado , é necessário cadastrar usuário primeiro")

            
            
        else :
            contas.append(Conta_corrente.criarConta(cpf))

     
    
    elif opcao=='u':
        for cliente in clientes:
            print(f" Nome do cliente : {cliente.nome}, \n Endereco :{cliente.endereco}, \n CPF:   {cliente.cpf} \n, Data Nascimento: {cliente.data_nascimento}")
     
    
    elif opcao=='b':
        for conta in contas:
            print(f" Saldo da conta : R$ {conta._saldo:.2f} \n Numero da Conta: {conta._numero} \n Numero da Agencia:{conta._agencia} \n Cliente : {conta._cliente} \n Saldo: R${conta._saldo:.2f} \n Limite: R$ {conta._limite:.2f} \n Limite Saque : {conta._limite_saque}")        

       
   
    elif opcao =='q':
         break
    else:
        print("opcao invalida , por favor selecione novamente a operação desejada")
    




