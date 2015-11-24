from django.contrib import admin

# Register your models here.


from .models import TimeTable,Train,Station

admin.site.register(TimeTable)
admin.site.register(Train)
admin.site.register(Station)