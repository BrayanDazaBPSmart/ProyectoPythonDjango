from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Info(models.Model):
    ies = models.TextField()
    sector_ies = models.TextField()
    caracter_ies = models.TextField()
    departamento_domicilio_ies = models.TextField()
    municipio_domicilio_ies = models.TextField()
    programa_academico = models.TextField()
    nivel_academico = models.TextField()
    nivel_formacion = models.TextField()
    metodologia = models.TextField()
    sexo = models.TextField()
    anio = models.TextField()
    semestre = models.IntegerField()
    graduados = models.TextField()
    matriculados = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item
