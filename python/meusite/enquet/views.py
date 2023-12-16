from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá! vôce na página da enquete")
