from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class MainScreen(APIView):

    def get(self, request, format=None):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())


class ValidateJSON(APIView):

    def post(self, request, format=None):
        payload = self.payload
        print(payload)