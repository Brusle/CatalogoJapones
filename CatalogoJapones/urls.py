from django.contrib import admin
from django.urls import path
from mi_app.views import WelcomeView, SearchSelectionView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('search/', SearchSelectionView.as_view(), name='search_selection'),
    path('search/results/', SearchView.as_view(), name='search_results'),
]