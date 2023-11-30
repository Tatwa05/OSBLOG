from django.shortcuts import render

# Create your views here.
def racefn(request):
    return render(request,"racecondition.html")

def criticalfn(request):
    return render(request,"criticalsection.html")

def mutualfn(request):
    return render(request,"mutualexclusion.html")

def peterfn(request):
    return render(request,"petersonssolution.html")

def semaphoresfn(request):
    return render(request,"semaphores.html")