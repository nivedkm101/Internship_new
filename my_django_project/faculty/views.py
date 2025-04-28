from django.shortcuts import render


def career(request):
    return render(request, 'faculty/career.html')