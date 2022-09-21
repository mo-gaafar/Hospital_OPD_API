from urllib import request
from .models import Doctor, Patient, Department, Medicine, Room
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer, PatientSerializerRead, PatientSerializerWrite, DepartmentSerializer, MedicineSerializer, RoomSerializer

# Create your views here.


class DoctorsList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        department = self.request.query_params.get('department')
        if department is not None:
            queryset = queryset.filter(department=department)
        return queryset


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientsList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientSerializerRead
        else:
            return PatientSerializerWrite


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Patient.objects.all()
    # serializer_class = PatientSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientSerializerRead
        else:
            return PatientSerializerWrite


class DepartmentsList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class MedicinesList(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class RoomsList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
