from .models import *
from datetime import datetime 

def crear_curso(codigo, nombre, version):
    Curso.objects.create(codigo=codigo, nombre=nombre, version=version)

def crear_profesor(rut, nombre, apellido, activo, creado_por):
    Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)

def crear_estudiante(rut, nombre, apellido, fecha_nac):
    fecha = datetime.strptime(fecha_nac, '%d-%m-%Y').date()
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha)
    estudiante.save()
    return estudiante

def crear_direccion(estudiante_id, calle, numero, dpto, comuna, ciudad, region):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    Direccion.objects.create(Estudiante_id = estudiante, calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region)

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agrega_profesor_a_curso(codigo, rut):
    curso = Curso.objects.get(codigo=codigo)
    profesor = Profesor.objects.get(rut=rut)
    curso.profesor_id.add(profesor)
    curso.save()
    
def agrega_cursos_a_estudiante(codigo, rut):
    estudiante = Estudiante.objects.get(rut=rut)
    cursos = Curso.objects.get(codigo=codigo)
    cursos.estudiante_id.add(estudiante)
    cursos.save()
    
def imprime_estudiante_cursos(rut, codigo):
    estudiante = Estudiante.objects.get(rut=rut)
    curso = estudiante.curso.all()
    for curso in curso:
        print(curso)

