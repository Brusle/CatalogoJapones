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
        # Cargamos los datos de los personajes
        df_personajes = cargar_datos_verificados()
        # Convertimos el DataFrame a una lista de diccionarios para usarla en la plantilla
        lista_personajes = df_personajes.to_dict('records')
        
        context = {
            'personajes': lista_personajes
        }
        return render(request, 'character_list.html', context)