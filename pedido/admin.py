from django.contrib import admin
from .models import Pedido, ItemPedido, CupomDesconto

# Register your models here.


class ItemPedidoInline(admin.TabularInline):
    readonly_fields = ("produto", "quantidade", "preco",
                       "descricao", "adicionais",)
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]
    list_display = ("cliente", "total", "data", "entregue")
    search_fields = ("entregue", )
    readonly_fields = ("cliente", "total", "data", "pagamento", "troco",)


@admin.register(CupomDesconto)
class CupomDescontoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "desconto", "ativo",)
    readonly_fields = ("usos", )


admin.site.register(Pedido, PedidoAdmin)
