class Paciente:
    def __init__(self, nome, numeroFicha):
        self.nome = nome
        self.numeroFicha = numeroFicha

class Atendimento:
    def __init__(self, nomePaciente, numeroFicha):
        self.paciente = Paciente(nomePaciente, numeroFicha)
        self.proximo = None

class ListaAtendimentos:
    def __init__(self):
        self.cabeca = None
        self.contador = 0

    def atualizarContador(self):
        self.contador = self.contador + 1

    def adicionar(self, nomePaciente):
        if(self.cabeca is None):
            self.cabeca = Atendimento(nomePaciente, self.contador)
        else:
            atendimentoAtual = self.cabeca

            while(atendimentoAtual.proximo is not None):
                atendimentoAtual = atendimentoAtual.proximo
            
            atendimentoAtual.proximo = Atendimento(nomePaciente, self.contador)
        
        self.atualizarContador()
    
    def remover(self, idPaciente):
        atual = self.cabeca
        anterior = None

        while(atual):
            if(atual.paciente.numeroFicha == idPaciente):
                if(anterior is None):
                    self.cabeca = atual.proximo
                    anterior = None
                else:
                    anterior.proximo = atual.proximo
                
                break;
            
            anterior = atual
            atual = atual.proximo

    def listar(self):
        current = self.cabeca
        
        while(current):
            print("NÚMERO:", current.paciente.numeroFicha,
                   "PACIENTE:", current.paciente.nome)
            current = current.proximo
    

atendimentos = ListaAtendimentos()

atendimentos.adicionar('Melly')
atendimentos.adicionar('Liniker')
atendimentos.adicionar('Duquesa')

atendimentos.listar()

atendimentos.remover(1)

atendimentos.listar()

