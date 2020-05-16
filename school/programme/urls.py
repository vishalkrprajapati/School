from django.urls import path
from . import views
urlpatterns = [
    path('pre-primary/', views.preprimary, name="pre-primary"),
    path('primary/', views.primary, name="primary"),
    path('heigher/', views.heigher, name="heigher"),
    path('middile/', views.middile, name="middile"),
    path('heighersecondary/', views.heighersecondary, name="heighersecondary"),

]
