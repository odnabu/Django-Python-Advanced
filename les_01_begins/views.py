from django.http import HttpResponse

# Create your views here.

def hello(request):
    print(request.method)
    return HttpResponse("Hello World!")


