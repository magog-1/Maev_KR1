from django.shortcuts import render
import os


# Create your views here.
def index(request):
    freebase_api_key = os.environ.get("FREEBASE_API_KEY", "Ключ не найден")

    context = {"api_key": freebase_api_key}
    return render(request, "index.html", context)
