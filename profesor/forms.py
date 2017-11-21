from django import forms
from .models import Grado, Profesor, Materia

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre', 'cupo', 'porfesores')
def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
        self.fields["porfesores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["porfesores"].help_text = "Ingrese los Profesores que imparten cursos ese grado"
        self.fields["porfesores"].queryset = Profesor.objects.all()

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nombre', 'profe', 'grado')
def __init__ (self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["profe"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["profe"].help_text = "Ingrese el Profesor que imparte curso ese grado"
        self.fields["profe"].queryset = Profesor.objects.all()
        self.fields["grado"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["grado"].help_text = "Ingrese el Grado que corresponde"
        self.fields["grado"].queryset = Grado.objects.all()
