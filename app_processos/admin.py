from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Pessoa, Processo, Departamento, PedidoPrazo, Instauracao, EnvioProcesso)
class Pessoa(admin.ModelAdmin):
    pass
class Processo(admin.ModelAdmin):
    pass
class Departamento(admin.ModelAdmin):
    pass

class PedidoPrazo(admin.ModelAdmin):
    pass
class Instauracao(admin.ModelAdmin):
    pass
class EnvioProcesso(admin.ModelAdmin):
    pass