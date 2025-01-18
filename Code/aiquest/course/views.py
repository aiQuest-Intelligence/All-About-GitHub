from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return render(request, 'ml.html')
