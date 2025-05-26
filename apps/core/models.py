from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.titulo} - {self.data} {self.hora}"

class Sociedade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Diretoria(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    sociedade = models.ForeignKey(Sociedade, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.funcao} ({self.sociedade.nome})"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    duvida = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} em {self.data_envio}"
