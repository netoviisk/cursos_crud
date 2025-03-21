from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    carga_horaria = models.IntegerField(verbose_name='Carga Horaria')
    instrutor = models.CharField(max_length=255, verbose_name='Instrutor')

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Aluno')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscrição')

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome}"