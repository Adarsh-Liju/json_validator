from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json

class MainScreen(APIView):
    """
    Renders the main HTML page.
    """

    def get(self, request, format=None):
        try:
            template = loader.get_template('index.html')
            return HttpResponse(template.render())
        except Exception as e:
            return HttpResponse(f"Error rendering template: {str(e)}", status=500)


class ValidateJSON(APIView):
    """
    Validates JSON sent in the request body.
    """

    def post(self, request):
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        try:
            # Attempt to parse the JSON payload
            payload = json.loads(request.body)
            return JsonResponse({"message": "Valid JSON", "data": payload}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)


class PrettifyJSON(APIView):
    """
    Pretty-prints JSON sent in the request body.
    """

    def post(self, request):
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        try:
            # Attempt to parse the JSON payload
            payload = json.loads(request.body)
            pretty_json = json.dumps(payload, indent=4)
            return JsonResponse({"message": "Pretty Print JSON", "data": pretty_json}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)