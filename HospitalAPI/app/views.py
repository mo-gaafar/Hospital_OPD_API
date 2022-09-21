from app.models import Doctor, Patient, Department, Medicine, Room
from rest_framework.response import Response
from rest_framework.decorators import api_view

# django views imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def getData(request):
    return Response({'message': 'Hello, World!'})


# # Create your views here.
# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def doctor(request):
#     if request.method == "GET":
#         try:
#             doctor = Doctor.objects.get(id=request.GET.get("id"))
#             return JsonResponse(doctor.to_json(), safe=False)
#         except ObjectDoesNotExist:
#             return JsonResponse({"error": "Doctor does not exist"}, safe=False)
#     elif request.method == "POST":
#         doctor = Doctor()
#         doctor.name = request.POST.get("name")
#         doctor.save()
#         return JsonResponse(doctor.to_json(), safe=False)

# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def patient(request):
#     if request.method == "GET":
#         try:
#             patient = Patient.objects.get(id=request.GET.get("id"))
#             return JsonResponse(patient.to_json(), safe=False)
#         except ObjectDoesNotExist:
#             return JsonResponse({"error": "Patient does not exist"}, safe=False)
#     elif request.method == "POST":
#         patient = Patient()
#         patient.name = request.POST.get("name")
#         patient.save()
#         return JsonResponse(patient.to_json(), safe=False)
