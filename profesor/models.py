from django.db import models
from django.contrib import admin
# Create your models here.
#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Profesor(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    cupo      = models.IntegerField()
    porfesores   = models.ManyToManyField(Profesor, through='Materia')
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)
    profe = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class MateriaInLine(admin.TabularInline):
    model = Materia
    extra = 1

class ProfesorAdmin(admin.ModelAdmin):
    inlines = (MateriaInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (MateriaInLine,)
