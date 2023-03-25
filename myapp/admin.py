from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')


admin.site.register(Contact, ContactAdmin)

title = "Transmudanzas Niquepa | Panel "

admin.site.site_header = title
admin.site.site_title = title 
admin.site.index_title = "Panel de Gestion"