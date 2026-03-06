from django.db import models

class Menu(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(default='Nenhuma')
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'Prato: {self.nome}, preco: {self.preco}'

class Reserva(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    data= models.DateField()
    hora= models.TimeField()
    pessoas= models.PositiveIntegerField()
    observacoes= models.TextField(default='Nenhuma')
    
    def __str__(self):
        return self.name
