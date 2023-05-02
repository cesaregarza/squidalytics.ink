from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, 'landing/hello_world.html')