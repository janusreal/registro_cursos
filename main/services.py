from main.models import *

def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso

def crear_profesor(rut,nombre,apellido):
    profe = Profesor(rut=rut,nombre=nombre,apellido=apellido, activo=True)
    profe.save()
    return profe
    
def crear_estudiante(rut,nombre,apellido,fecha_nac):
    estudiante = Estudiante(rut=rut,nombre=nombre,apellido=apellido,fecha_nac=fecha_nac,activo=True)
    estudiante.save()
    return estudiante

def crear_direccion(calle,numero,comuna,region,rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    direccion = Direccion(calle=calle,numero=numero,comuna=comuna,region=region, estudiante=estudiante)
    direccion.save()
    return direccion

def agrega_cursos_a_estudiante(curso_codigo, estudiante_rut):
    # cursoestudiante = CursoEstudiante(curso_codigo...) -> no funciona
    #modelo implicito obliga a un enfoque distinto
    c = Curso.objects.get(codigo=curso_codigo)
    e = Estudiante.objects.get(rut=estudiante_rut)
    c.estudiantes.add(e) # ó e.cursos.add(c)

def agregar_profesor_a_curso(profesor_rut,curso_codigo):
    p = Profesor.objects.get(rut=profesor_rut)
    c = Curso.objects.get(codigo=curso_codigo)
    c.profesor=p
    c.save()

def obtiene_estudiante(estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    return estudiante

def obtiene_profesor(profesor_rut):
    profesor = Profesor.objects.get(rut=profesor_rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def imprime_estudiante_cursos(estudiante_rut):
    estudiante = obtiene_estudiante(estudiante_rut)
    cursos = estudiante.cursos.all()
    print(f'Estudiante: {estudiante.nombre} {estudiante.apellido}')
    print(f'Cursos:')
    for curso in cursos:
        print(f'{curso.nombre}')