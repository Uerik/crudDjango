from django.contrib import admin
from .models import Basico

# Register your models here.
class Basicoadm(admin.ModelAdmin):
  list_display = ("nome", "telefone",)

admin.site.register(Basico, Basicoadm)

