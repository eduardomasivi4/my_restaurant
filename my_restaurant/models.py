from django.db import models

class Menu(models.Model):
    imagem = models.ImageField(upload_to='img', null=True)
    name = models.CharField(max_length=50)
    descricao = models.TextField(null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    data= models.DateField()
    hora= models.TimeField()
    pessoas= models.PositiveIntegerField()
    observacoes= models.TextField(default='Nenhuma')
    
    def __str__(self):
        return self.name
