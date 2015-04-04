from django.contrib import admin
from gesevent.models import Tipus, Tematica, Pais, Carrer, Ubicacio, \
    Administrador, Persona


# Register your models here.
class UbicacioInline(admin.StackedInline):
    model = Ubicacio
    extra = 1


class CarrerAdmin(admin.ModelAdmin):
    inlines = [UbicacioInline]


admin.site.register(Tematica)
admin.site.register(Tipus)
admin.site.register(Pais)
admin.site.register(Carrer, CarrerAdmin)
admin.site.register(Administrador)
admin.site.register(Persona)
