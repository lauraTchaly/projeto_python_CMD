from django.contrib import path
from . import views
# Create your views here.
urlpatterns = [
    path("",views.index, name="index"),

    ]
