from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.

def default(request):
    print("In Default")
    return render(request, 'learning_dashboard/dashboard.html')


@api_view(['POST', 'GET'])
def dashboard(request):
    print("In dashboard")
    return render(request, 'learning_dashboard/dashboard.html')


@api_view(['POST', 'GET'])
def classroom(request):
    print("In classroom")
    return render(request, 'learning_dashboard/classroom.html')


@api_view(['POST', 'GET'])
def announcements(request):
    print("In announcements")
    return render(request, 'learning_dashboard/announcements.html')


@api_view(['POST', 'GET'])
def resources(request):
    print("In resources")
    return render(request, 'learning_dashboard/resources.html')




"""
def resources(requests):
    print("In resources")

    if request.method == 'GET':
        

    elif request.method == 'POST':
"""