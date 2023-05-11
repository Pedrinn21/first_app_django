from django.db import models

class TipoProduto(models.Model):
    descricao = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.descricao


class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.IntegerField()
    fktipoproduto = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.descricao
