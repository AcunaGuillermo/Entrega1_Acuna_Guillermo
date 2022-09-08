
from django.shortcuts import render, redirect
from django.urls import reverse
from AppFutbol.models import Jugador, Equipo, Posicion
from AppFutbol.forms import EquipoFormulario, JugadorFormulario, PosicionFormulario

def inicio(request):

    return render(request, "AppFutbol/inicio.html")

# Vistas de Equipo

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "AppFutbol/equipo.html", {'equipos': equipos})


def crear_equipo(request):
    if request.method == 'POST':
        formulario = EquipoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo = Equipo(**data)
            equipo.save()
            return redirect(reverse('equipo'))
            
    else:  
        formulario = EquipoFormulario() 
    return render(request, "AppFutbol/form_equipo.html", {"formulario": formulario})


def busqueda_equipos(request):
    return render(request, "AppFutbol/form_busqueda_equipo.html")


def buscar_equipo(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        equipos = Equipo.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFutbol/equipo.html", {'equipos': equipos})
    else:
        return render(request, "AppFutbol/equipo.html", {'equipos': []})

def eliminar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    borrado_id = equipo.id
    equipo.delete()
    url_final = f"{reverse('equipo')}?borrado={borrado_id}"

    return redirect(url_final)


# Vistas de jugadores

def jugadores(request):
    jugadores = Jugador.objects.all() 
    contexto = {"jugadores": jugadores}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppFutbol/jugadores.html", contexto)


def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    borrado_id = jugador.id
    jugador.delete()
    url_final = f"{reverse('jugador')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_jugador(request):
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador = Jugador(**data)
            jugador.save()
            
            return redirect(reverse('jugador'))
    else:  
        formulario = JugadorFormulario()  
    return render(request, "AppFutbol/form_jugador.html", {"formulario": formulario})


def editar_jugador(request, id):
    
    jugador = Jugador.objects.get(id=id)

    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador = Jugador(**data)

            jugador.save()

            return redirect(reverse('jugador'))
    else: 
        inicial = {
            'nombre': jugador.nombre,
            'pais': jugador.apellido,
            'fecha de nacimiento': jugador.fecha_nacimiento,
            
        }
        formulario = JugadorFormulario(initial=inicial)
    return render(request, "AppFutbol/form_jugador.html", {"formulario": formulario})

    # Vistas de posiciones

def posiciones(request):
    posiciones = Posicion.objects.all()  
    contexto = {"posiciones": posiciones}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppFutbol/posiciones.html", contexto)


def eliminar_posicion(request, id):
    posicion = Posicion.objects.get(id=id)
    borrado_id = posicion.id
    posicion.delete()
    url_final = f"{reverse('posicion')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_posicion(request):
    if request.method == 'POST':
        formulario = PosicionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            posicion = Posicion(**data)
            posicion.save()
            return redirect(reverse('posicion'))
    else:  
        formulario = PosicionFormulario()  
    return render(request, "AppFutbol/form_posicion.html", {"formulario": formulario})


def editar_posicion(request, id):
    
    posicion = Posicion.objects.get(id=id)

    if request.method == 'POST':
        formulario = PosicionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            posicion.posicion = data['posicion']
            posicion.equipo = data['equipo']            

            posicion.save()

            return redirect(reverse('posicion'))
    else:  
        inicial = {
            'nombre': posicion.posicion,
            'equipo': posicion.equipo,
                        
        }
        formulario = PosicionFormulario(initial=inicial)
    return render(request, "AppFutbol/form_posicion.html", {"formulario": formulario})



