from django.contrib import admin
from .models import Categoria, Opcoes, Adicional, Produto

# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'nome_produto', 'categoria', 'preco', 'ativo')
    list_editable = ('preco', 'ativo')


admin.site.register(Opcoes)
admin.site.register(Categoria)
admin.site.register(Adicional)
