from django.shortcuts import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Olá! vôce na página da enquete")


def detalhes(request, id):
    return HttpResponse("Você está visualizando a questão %s." % id)
def resultados(request, id):
    resposta = "Você está visualizando o resultado da questão %s." 
    return HttpResponse(resposta % id)
def voto(request, id):
    return HttpResponse("Você está votando na questão %s." % id)