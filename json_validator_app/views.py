import json
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.template import loader
from datetime import datetime, timezone, timedelta

class MainScreen(APIView):
    """
    Renders the main HTML page.
    """

    def get(self, request, format=None):
        try:
            template = loader.get_template('index.html')
            return HttpResponse(template.render({}, request))
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
            payload = json.loads(request.body.decode('utf-8'))
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
            payload = json.loads(request.body.decode('utf-8'))
            pretty_json = json.dumps(payload, indent=4)
            return JsonResponse({"message": "Pretty Print JSON", "data": pretty_json}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)


class EpochConverter(APIView):
    """
    Converts Epoch Time to Human Readable Format in IST
    """

    def get(self, request):
        try:
            template = loader.get_template('epoch_converter.html')
            return HttpResponse(template.render({}, request))
        except Exception as e:
            return HttpResponse(f"Error rendering template: {str(e)}", status=500)

    def post(self, request):
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        try:
            payload = json.loads(request.body.decode('utf-8'))
            epoch_time = payload.get('time')

            if epoch_time is None:
                return JsonResponse({"error": "Epoch time not provided"}, status=400)

            # Convert Epoch time to IST
            utc_time = datetime.fromtimestamp(epoch_time / 1000, tz=timezone.utc)
            ist_time = utc_time + timedelta(hours=5, minutes=30)
            formatted_time = ist_time.strftime("%a, %d %b %Y %H:%M:%S IST")

            return JsonResponse({"message": "Human Readable Time Format in IST", "data": formatted_time}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)
