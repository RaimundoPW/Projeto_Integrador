from django.db import models

class PacoteTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    url_botao = models.URLField(max_length=500)
    imagem = models.ImageField(upload_to='pacotes/')

    def __str__(self):
        return self.nome