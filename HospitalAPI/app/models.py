# django models imports
from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Male'), ('F', 'Female')]
    )
    birthdate = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100, null=True)
    # prescriber = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.dose}"


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Male'), ('F', 'Female')]
    )
    birthdate = models.DateField()
    medicines = models.ManyToManyField(Medicine)
    seeing_doctors = models.ManyToManyField(Doctor)
    room = models.OneToOneField(Room, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
