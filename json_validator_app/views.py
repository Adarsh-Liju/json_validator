from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class MainScreen(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())