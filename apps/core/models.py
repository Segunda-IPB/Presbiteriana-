from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.titulo} - {self.data} {self.hora}"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    duvida = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} em {self.data_envio}"
    