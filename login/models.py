from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome