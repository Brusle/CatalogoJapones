from django.contrib import admin
from django.urls import path
# Importaciones nuevas
from django.conf import settings
from django.conf.urls.static import static
from mi_app.views import WelcomeView, SearchSelectionView, SearchView, CharacterListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('search/', SearchSelectionView.as_view(), name='search_selection'),
    path('search/results/', SearchView.as_view(), name='search_results'),
    path('characters/', CharacterListView.as_view(), name='character_list'),
]

# Añade esta línea al final para servir las imágenes subidas
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)