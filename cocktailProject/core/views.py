from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, "dashboard.html")

def test_one(request):
    return render(request, "one.html")

def test_two(request):
    return render(request, "two.html")

def test_three(request):
    return render(request, "three.html")