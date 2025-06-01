from django.contrib import admin
from .models import Evento, MensagemContato

# Personalizando a visualização de eventos no admin
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'hora')  # Colunas visíveis na listagem
    list_filter = ('data',)                    # Filtro lateral por data
    search_fields = ('titulo', 'descricao')    # Campo de busca
    ordering = ('-data', 'hora')               # Ordenação padrão: mais recentes primeiro

# Personalizando a visualização das mensagens de contato
@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem')  # Colunas visíveis
    search_fields = ('nome', 'email', 'mensagem') # Busca por esses campos
    ordering = ('-id',)                            # Mensagens mais recentes primeiro