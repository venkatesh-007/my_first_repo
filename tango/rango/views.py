from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def rango_index(request):
    return render(request, 'rango/index.html', {'text' : "Hello rango, i'm django"})


def rango_about(request):
    return HttpResponse("This is about page")
