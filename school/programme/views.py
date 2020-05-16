from django.shortcuts import render

# Create your views here.

def preprimary(request):
    return render(request, 'programme/pre-primary.htm')

def primary(request):
    return render(request, 'programme/primary.htm')

def heigher(request):
    return render(request, 'programme/heigher.htm')

def middile(request):
    return render(request, 'programme/middile.htm')

def heighersecondary(request):
    return render(request, 'programme/heigher-secondary.htm')
