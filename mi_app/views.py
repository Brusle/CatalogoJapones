from django.shortcuts import render
from .models import Cliente
from django.views import View
from vector_db import buscar_personajes, cargar_datos_verificados


class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcome.html')

class SearchSelectionView(View):
    def get(self, request):
        return render(request, 'search_selection.html')

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        metric = request.GET.get('metric', 'cosine')
        
        if query:
            resultados = buscar_personajes(query, metric)
        else:
            resultados = []
            
        return render(request, 'search_results.html', {'resultados': resultados, 'query': query})
    
class CharacterListView(View):
    def get(self, request):
        df_personajes = cargar_datos_verificados()
        # Agrupamos los personajes por Anime
        animes = {}
        for _, row in df_personajes.iterrows():
            anime = row['Anime']
            if anime not in animes:
                animes[anime] = []
            animes[anime].append(row['Personaje'])
        
        context = {
            'animes': animes
        }
        return render(request, 'character_list.html', context)