from django.shortcuts import render

# Create your views here.
def index_django(request):
    return render(request, "index.html", {"name":"chandan"})