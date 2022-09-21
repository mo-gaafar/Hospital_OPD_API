from rest_framework import serializers
from app.models import Doctor, Patient, Department, Medicine, Room
from datetime import datetime


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(method_name='get_age')

    class Meta:
        model = Doctor
        fields = '__all__'

    def get_age(self, instance):
        return datetime.now().year - instance.birthdate.year


class PatientSerializer(serializers.ModelSerializer):
    medicines = serializers.StringRelatedField(many=True, read_only=True)
    seeing_doctors = serializers.StringRelatedField(many=True, read_only=True)
    age = serializers.SerializerMethodField(method_name='get_age')

    def get_age(self, instance):
        return datetime.now().year - instance.birthdate.year

    class Meta:
        model = Patient
        fields = ['id', 'name', 'gender', 'age',
                  'medicines', 'seeing_doctors', 'room']
