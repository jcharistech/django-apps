from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {"title": "API"}
    return render(request,"index.html", context)