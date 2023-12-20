from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path("",views.index, name="index"),
    path("<int:id>/", views.detalhes, name="detalhes"),
    path("<int:id>/resultados/", views.resultados, name="resultados"),
    path("<int:id>/voto/", views.voto, name="voto"),

    ]
