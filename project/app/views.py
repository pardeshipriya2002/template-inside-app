from django.shortcuts import render,redirect

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



def register(request):
    return render(request, 'register.html')

def registerdata (request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('fname')
    email=request.POST.get('email')
    contact=request.POST.get('contactno')
    print(name,email,contact)







# def register(request):
#     return redirect("https://www.google.com/search?q=movies&sca_esv=7b0e25503c647052&sca_upv=1&rlz=1C1RXQR_enIN947IN947&sxsrf=ADLYWILhoUKh8C2HOr2ocMru2-mssWSW0g%3A1719576914857&ei=Uql-Zqv8M_ebseMPteeH2A8&ved=0ahUKEwir7bGZo_6GAxX3TWwGHbXzAfsQ4dUDCBA&uact=5&oq=movies&gs_lp=Egxnd3Mtd2l6LXNlcnAiBm1vdmllczIKECMYgAQYJxiKBTIKECMYgAQYJxiKBTILEAAYgAQYsQMYgwEyChAAGIAEGAoYywEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIFEAAYgARItQ5Q_gVYgQlwAXgBkAEAmAG7AqABjQaqAQUyLTIuMbgBA8gBAPgBAZgCAqACngLCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBZgDAIgGAZAGCpIHBTEuMC4xoAekEw&sclient=gws-wiz-serp")

