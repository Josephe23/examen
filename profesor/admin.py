from django.contrib import admin
from profesor.models import Profesor, ProfesorAdmin, Grado, GradoAdmin
# Register your models here.
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Grado, GradoAdmin)
