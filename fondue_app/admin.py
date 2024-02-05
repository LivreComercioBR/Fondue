from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from fondue_app.models import User, Rua, Cidade, Bairro, Cep

# Register your models here.


@admin.register(User)
class PersonAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff",)
    search_fields = ("username", "email", )


admin.site.register(Cep)
admin.site.register(Rua)
admin.site.register(Bairro)
admin.site.register(Cidade)
