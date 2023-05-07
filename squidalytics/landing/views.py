from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request: HttpRequest) -> HttpResponse:
    title = "Hello World"
    content = "Hello World! This is the landing page!"

    context = {
        "title": title,
        "content": content,
    }
    return render(request, "landing/hello_world.html", context=context)
