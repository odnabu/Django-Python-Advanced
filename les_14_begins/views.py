from django.http import HttpResponse

# Create your views here.

def hello(request):
    print(request.method)
    return HttpResponse("<h1>Hello, world!</h1>")


