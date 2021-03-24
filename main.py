# Construa um algoritmo para implementar a classe Aluno(código, nome, matrícula).
# A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano) e AlunoGraduacao(semestre).
# As 3 classes possuem o método construtor e também o método imprimir(), que imprimi na tela
# os valores de todos os atributos da sua classe 


# Aluno
# codigo: int
# nome: string
# matricula:string
# imprimir():void

# AlunoEnsinoMedio
# ano: int
# imprimir():void

# AlunoGraduação
# semestre: int
# imprimir():void



from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

a = Aluno(1, "João", "123.456.789")
a.imprimir()

al = AlunoEnsinoMedio(2, "Maria", "321.654.987", 2)
al.imprimir()

ag = AlunoGraduacao(3, "Ricardo", "213.564.897", 4)
ag.imprimir()