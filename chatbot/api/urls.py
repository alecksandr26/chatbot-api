from django.urls import path

# Import our response 
from . import views

urlpatterns = [
    # Here we are adding our function 
    path("", views.index, name="index")
]



