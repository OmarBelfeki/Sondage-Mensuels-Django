from django.urls import path
from . import views

urlpatterns = [
    path('sondage/', views.sondage, name="sondage"),

]
