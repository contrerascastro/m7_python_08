from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.rut} - {self.apellido}, {self.nombre}'
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.rut} - {self.apellido}, {self.nombre}'

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor_id = models.ManyToManyField(Profesor)
    estudiante_id = models.ManyToManyField(Estudiante)
    
    def __str__(self):
        return f'{self.codigo} - {self.nombre}, v:{self.version}'

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10,)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    Estudiante_id = models.OneToOneField(Estudiante, unique=True, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Estudiante_id} - {self.calle} - {self.dpto} - {self.comuna} - {self.ciudad} - {self.region}'
