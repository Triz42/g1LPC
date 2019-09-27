from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pessoa(models.Model):
    class meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    usuario = models.OneToOneField(User, on_delete= models.PROTECT, verbose_name= "Usuário")
    nome = models.CharField(max_length=125)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Departamento(models.Model):
    class meta:
        verbose_name = 'Derpatamento'
        verbose_name_plural = 'Derpatamentos'

    nome = models.CharField(max_length=125)
    endereco = models.CharField('Endereço', max_length= 200)

    def __str__(self):
        return f'{self.nome}'


class Documento(models.Model):
    class meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    nome = models.CharField(max_length=125)

    def __str__(self):
        return f'{self.nome}'


class PedidoPrazo(Documento):
    justificativa = models.TextField('Justificativa', max_length=125)
    prazo = models.DateField('Novo Prazo', blank=True, null=True)

    prazoAnterior = models.DateField('Prazo Anterior', blank=True, null=True)

    def __str__(self):
        return f'{self.prazo}'


class Instauracao(Documento):
    data = models.DateField('Data de Instauração')

    def __str__(self):
        return f'{self.data}'


class EnvioProcesso(Documento):
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, verbose_name="Departamento", null=True)
    tempo = models.DateField('Tempo no Departamento', blank=True, null=True)

    def __str__(self):
        return f'{self.departamento}'


class Processo(models.Model):
    class meta:
        verbose_name = 'Processos'
        verbose_name_plural = 'Processos'

    numero_Processo = models.IntegerField('Número')
    data = models.ForeignKey(Instauracao, on_delete=models.SET_NULL, verbose_name="Data Criacao", null=True)
    criador = models.ForeignKey(Pessoa, on_delete= models.SET_NULL, verbose_name= "Criador", null=True)
    interessado = models.ManyToManyField(Pessoa, verbose_name= "Interessado", related_name= "interessados", blank= True)
    investigados = models.ManyToManyField(Pessoa, verbose_name="Investigados", related_name= "investigados", blank=True)
    local_atual = models.ForeignKey(Departamento, on_delete= models.SET_NULL, verbose_name= "Departamento", null=True, related_name= "atual")
    data_departamento = models.DateField('Data de entrada no Departamento', blank=True, null=True)

    locais = models.ForeignKey(EnvioProcesso, on_delete=models.SET_NULL, verbose_name="Departamentos Anteriores", null=True, related_name= "anteriores")
    novoPrazo =  models.ForeignKey(PedidoPrazo, on_delete=models.SET_NULL, verbose_name="Prazo de Tramitação", null=True)
    def __str__(self):
        return f'{self.numero_Processo}'

