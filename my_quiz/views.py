from django.shortcuts import render

# Create your views here.
def appmain(request):
   return render(request, 'quiz/main.html', {})

def appfifa(request):
    return render(request, 'quiz/fifa.html', {})

def appflag(request):
    return render(request, 'quiz/flag.html', {})
