from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json

# Create your views here.

class MainScreen(APIView):

    def get(self, request, format=None):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())


class ValidateJSON(APIView):
    '''Validates JSON'''

    def post(self, request, format=None):
        try:
            # Parse the JSON payload
            payload = json.loads(request.body)
            # If parsing succeeds, return a success response
            return JsonResponse({"message": "Valid JSON", "data": payload}, status=200)
        except json.JSONDecodeError as e:
            # If parsing fails, return an error response
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
