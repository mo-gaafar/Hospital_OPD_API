
from django.urls import path
from . import views
from .views import DoctorsList, DoctorDetail, PatientsList, PatientDetail, DepartmentsList, DepartmentDetail, MedicinesList, MedicineDetail, RoomsList, RoomDetail

urlpatterns = [
    path('doctors/', DoctorsList.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),
    path('patients/', PatientsList.as_view()),
    path('patients/<int:pk>/', PatientDetail.as_view()),
    path('departments/', DepartmentsList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('medicines/', MedicinesList.as_view()),
    path('medicines/<int:pk>/', MedicineDetail.as_view()),
    path('rooms/', RoomsList.as_view()),
    path('rooms/<int:pk>/', RoomDetail.as_view()),
]
