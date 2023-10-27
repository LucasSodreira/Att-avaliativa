from django.db import models

    
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + ' - ' + self.sigla_estado
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso", default="Curso")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default="Cidade", verbose_name="Cidade")
    