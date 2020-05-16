
from django.urls import path
from . import views
urlpatterns = [
    path('admission/', views.admission, name= "admission"),
    path('academic/', views.academic, name="academic"),
]
