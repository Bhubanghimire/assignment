from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {}
    print("home")
    return render(request, 'index.html', context=context)

def login(request):
    if request.method=="POST":
        #login logic
        return redirect("home")
    context = {}
    return render(request, 'Login.html', context=context)

def signup(request):
    if request.method=="POST":
        #login logic
        return redirect("home")
    context = {}
    return render(request, 'Login.html', context=context)

def contact(request):
    if request.method =="POST":
        # contact create login here
        return redirect("home")

    return render(request, 'contact.html')

