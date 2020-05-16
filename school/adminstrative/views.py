from django.shortcuts import render

# Create your views here.
def admission(request):
    return render(request, 'aadminstrative/admission.htm')

def academic(request):
    return render(request, 'aadminstrative/academic.htm')