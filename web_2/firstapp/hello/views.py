from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Это мой первый проект в Django")

# Create your views here.
