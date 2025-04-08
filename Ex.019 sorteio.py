# Um professor quer sortear quatro alunos. faça um proframa que leia o nome escolhido.
from random import choice
alunos = input('Escreva os nomes do alunos separando por vírgula:').split(",")

print(f'O aluno escolhido é: {choice(alunos)}')