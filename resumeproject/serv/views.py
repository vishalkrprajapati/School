from django.shortcuts import render

# Create your views here.
def service(request):
    context = {'service' : 'active'}
    return render(request, 'serve/service.htm', context)