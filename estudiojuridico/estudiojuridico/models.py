from django.db import models


class Cliente(models.Model):
    dni = models.IntegerField(max_length=8, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.dni} - {self.nombre} - {self.apellido} - {self.nacimiento} - {self.pais}"


class Pais(models.Model):
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    calle = models.CharField(max_length=50, null=True, blank=True)
    numero = models.IntegerField(max_length=4, null=True, blank=True)
    departamento = models.IntegerField(max_length=2, null=True, blank=True)
    piso = models.IntegerField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.pais} - {self.provincia} - {self.ciudad} - {self.calle} - {self.numero} - {self.departamento} - {self.piso}"


class Derecho(models.model):
    derecho = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField

    def __str__(self):
        return f"{self.derecho} involucra {self.descripcion}"
