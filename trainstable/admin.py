from django.contrib import admin

# Register your models here.


from .models import RouteStation,Train,Station,Route

admin.site.register(RouteStation)
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Route)