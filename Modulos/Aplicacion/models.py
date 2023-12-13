from django.db import models
from datetime import timedelta
import datetime
from django.db.models import F

# Create your models here.

class estudiante(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    semestres = [
        ('1', '1'),
        ('2', '2'), 
        ('3', '3'), 
        ('4', '4'), 
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'),
        ('10', '10'),  
    ]
    semestre = models.CharField(max_length=2, choices=semestres)
    carrera = models.CharField(max_length=40)
    escuelas = [
        ('ingenieria', 'Ingeniería'),
        ('derecho', 'Derecho'), 
        ('ingenieria_y_derecho', 'Ingeniería y derecho'),
    ]
    escuela = models.CharField(max_length=40, choices=escuelas)
    prestamos = models.CharField(max_length=6, default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula}"

class academico(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    escuelas = [
        ('ingenieria', 'Ingeniería'),
        ('derecho', 'Derecho'), 
        ('ingenieria_y_derecho', 'Ingeniería y derecho'),
    ]
    escuela = models.CharField(max_length=40, choices=escuelas)
    prestamos = models.CharField(max_length=6, default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula}"

class administrativo(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    prestamos = models.CharField(max_length=6, default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.cedula}"

class libro(models.Model):
    autor = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20, primary_key=True)
    cota = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    edicion = models.CharField(max_length=20)
    año = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=6, default=0)
    cantidadPres = models.CharField(max_length=6, default=0)

    def __str__(self):
        return f"{self.autor} {self.titulo}"

class prestamo(models.Model):
    codigo = models.AutoField(primary_key=True, default=1)
    autor = models.CharField(max_length=20, default="")
    titulo = models.CharField(max_length=20, default="")
    usuarios = [
        ('1', 'Estudiante'),
        ('2', 'Academico'),
        ('3', 'Administrativo'),  
    ]
    usuario = models.CharField(max_length=20, choices=usuarios, default="Estudiante")
    nombre = models.CharField(max_length=40, default="")
    apellido = models.CharField(max_length=40)
    cedula = models.CharField(max_length=8)
    semestres = [
        ('1', '1'),
        ('2', '2'), 
        ('3', '3'), 
        ('4', '4'), 
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'),
        ('10', '10'),  
    ]
    semestre = models.CharField(max_length=2, choices=semestres)
    escuelas = [
        ('ingenieria', 'Ingeniería'),
        ('derecho', 'Derecho'), 
        ('ingenieria_y_derecho', 'Ingeniería y derecho'),
    ]
    escuela = models.CharField(max_length=40, choices=escuelas)
    bibliotecaria = models.CharField(max_length=40)
    tipoPrestamo = models.CharField(max_length=20, default="")
    tipoUsuario = models.CharField(max_length=20, default="")
    fechaInicial = models.CharField(max_length=8, default="")
    fechaFinal = models.CharField(max_length=8, default="")
    observaciones = models.CharField(max_length=40, default="") 

    def save(self, *args, **kwargs):
        super(prestamo, self).save(*args, **kwargs)
        libro.objects.filter(titulo=self.titulo).update(cantidadPres=F('cantidadPres') + 1)
        estudiante.objects.filter(cedula=self.cedula).update(prestamos=F('prestamos') + 1)
        academico.objects.filter(cedula=self.cedula).update(prestamos=F('prestamos') + 1)
        administrativo.objects.filter(cedula=self.cedula).update(prestamos=F('prestamos') + 1)

    def __str__(self):
        return f" {self.codigo} {self.nombre} {self.titulo}"
