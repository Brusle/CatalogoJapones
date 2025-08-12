from django.shortcuts import render
from .models import Cliente
from django.views import View
from vector_db import buscar_personajes

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