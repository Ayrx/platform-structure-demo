from django.shortcuts import render

def index(request):
    """Render the main Todo application page."""
    return render(request, 'todo_app/index.html')

