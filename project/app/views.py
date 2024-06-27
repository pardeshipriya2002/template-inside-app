from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
# def home (request):
#     data ={
#         "name": "Priya",
#         "age" : "20",
#         "address" : "Bhopal",
#         "Course" : "Full stack Python"
#     }
#     return JsonResponse(data)

def register (request):
    return render(request, 'register.html')

