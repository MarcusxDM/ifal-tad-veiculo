class Veiculo():
    def __init__(self, placa, marca, modelo, ano, cod):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cod = cod 

    def imprime(self):
        print("Placa: ", self.placa)
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)
        print("COD: ", self.cod)
        print("\n")

    def imprimeFinalPlaca(self):
        print(self.placa[-1])
        return self.placa[-1]

class ListaVeiculos():
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0
        self.lista = [None]*maximo

    def update(self):
        if self.atual>0:
            for i in range(self.atual):
                ant = self.lista[i]
                if ant == None:
                   self.lista[i] = self.lista[i+1]
                   self.lista[i+1] = None 
    
    def add(self, veiculo):
        if self.atual < self.maximo:
            self.lista[self.atual] = veiculo
            self.atual += 1

    def remove(self, placa):
        if self.atual > 0:
            for i in range(self.atual):
                if self.lista[i] and self.lista[i].placa == placa:
                    self.lista[i] = None
                    self.update()
                    self.atual -=1
                else:
                    pass
        else:
            pass

    def findPlaca(self, placa):
        for veiculo in self.lista:
            if veiculo and veiculo.placa == placa:
                veiculo.imprime()
                return veiculo
            else: 
                return None
    
    def findPlacaFinal(self, numero):
        for veiculo in self.lista:
            if veiculo and veiculo.imprimeFinalPlaca() == numero:
                veiculo.imprime()
            else:
                pass

    def imprime(self):
        for i in range(self.atual):
            self.lista[i].imprime()

        
        
# - Inserir um veículo na lista (no fim da lista);
# - Remover um veículo da lista, dada a placa deste (executar a operação somente se a lista não estiver vazia e se a placa de fato existir);
# - Consultar o cadastro da seguinte maneira: 
# + Dada a placa de um veículo, se a mesma existir, escrever todos os dados do veículo; 
# + Se for dado apenas um inteiro de 0 a 9, o programa escreverá todos os dados dos veículos cujos finais de placa sejam o tal número
