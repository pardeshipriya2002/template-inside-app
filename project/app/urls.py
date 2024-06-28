
from django.urls import path,include

from .views import register


from app import views
urlpatterns = [
    # path('home/',home)        it show directly import
    path('register/', views.register)
]
