from django.shortcuts import render
from django.views import View
from .models import Anime, Personaje
from django.db.models import Q # Para búsquedas más complejas

class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcome.html')

class SearchSelectionView(View):
    def get(self, request):
        return render(request, 'search_selection.html')

class CharacterListView(View):
    def get(self, request):
        # Obtenemos todos los animes con sus personajes relacionados
        # para evitar múltiples consultas a la base de datos.
        todos_los_animes = Anime.objects.prefetch_related('personajes').all()
        
        context = {
            'animes': todos_los_animes
        }
        return render(request, 'character_list.html', context)

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        resultados = []

        if query:
            # Buscamos la consulta en el nombre del personaje O en su biografía.
            # Q es para condiciones OR. icontains no distingue mayúsculas/minúsculas.
            resultados = Personaje.objects.filter(
                Q(nombre__icontains=query) | Q(biografia__icontains=query)
            )
        
        context = {
            'resultados': resultados,
            'query': query,
        }
        return render(request, 'search_results.html', context)