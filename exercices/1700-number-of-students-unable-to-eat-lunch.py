# THIS IS THE FIRST VERSION, BUT WAS TOO BIG AND COMPLICATE
# BUT THIS WORKS :)
class Solution:
    def countStudents(self, students, sandwiches) -> int:
        class FilaLanche:
            def __init__(self):
                self.listaAlunos = [];
                self.listaLanches = [];
            def adicionar(self, aluno, lanche):
                self.listaAlunos.append(aluno);
                self.listaLanches.append(lanche);
            def remover(self):
                self.listaAlunos.pop(0);
                self.listaLanches.pop(0);
            def adicionar_aluno(self, aluno):
                self.listaAlunos.append(aluno);
            def contar_alunos(self):
                while(self.listaAlunos and self.listaLanches[0] in self.listaAlunos != False):
                    if(self.listaAlunos[0] == self.listaLanches[0]):
                        self.remover();
                    else:
                        self.adicionar_aluno(self.listaAlunos.pop(0));
                return len(self.listaAlunos)
    
        fila = FilaLanche();
        for i in range(len(students)):
            fila.adicionar(students[i], sandwiches[i])
        return fila.contar_alunos();

# THIS IS A VERSION THAT I DID AFTER I SAW SOME EXAMPLES 
class FilaLanche:
    def counter_students(self, listaAlunos, listaLanches):       
        while(listaLanches and listaAlunos and listaLanches[0] in listaAlunos):
            if(listaAlunos[0] == listaLanches[0]):
                listaAlunos.pop(0);
                listaLanches.pop(0);
            else:
                listaAlunos.append(listaAlunos[0]);
                listaAlunos.pop(0)
        return len(listaAlunos)
     
# VALUES TO TEST
arrAlunos = [1,1,0,0]
arrLanches = [0,1,0,1]
# arrAlunos = [1,1,1,0,0,1]
# arrLanches = [1,0,0,0,1,1]

vinte_julho_2023_lanches = FilaLanche();
result = vinte_julho_2023_lanches.counter_students(arrAlunos, arrLanches);
print(result)
