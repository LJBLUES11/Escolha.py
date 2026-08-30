from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pontuacao']

    def __str__(self):
        return f'{self.nome} — {self.pontuacao} tentativa(s)'
