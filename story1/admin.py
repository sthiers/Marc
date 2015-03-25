from django.contrib import admin
from story1.models import Compound

# Register your models here.
class CompoundAdmin(admin.ModelAdmin):
        list_display = ('name', 'formula', 'mw', 'cas')

admin.site.register(Compound, CompoundAdmin)


