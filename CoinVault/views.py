from django.shortcuts import render


def index(request):
    if request.htmx:
        print("HTMX")
    else:
        print("NOT HTMX")
    return render(request, 'index.html')
