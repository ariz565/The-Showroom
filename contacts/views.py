from django.shortcuts import render

# Create your views here.

def inquiry(request):
    return render(request, 'contacts/inquiry.html') 
