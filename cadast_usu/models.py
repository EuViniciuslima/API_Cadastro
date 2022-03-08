from django.db import models

# Create your models her

class Cliente(models.Model):
    nome = models.CharField(max_length=120) #Precisa de um limitador para quantos caracters conter no nome.
    data_nascimento = models.DateField(blank=True, null=True) # infoemar que este campo não é obrigatório.  
    habilitado = models.BooleanField(blank=True, null=True) 
    observação = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome