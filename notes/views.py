from django.shortcuts import render

def home(request):
    name = request.POST.get('name', '')
    greeting = f"Good Morning, {name}!" if name else ""
    return render(request, 'notes/home.html', {'greeting': greeting})
