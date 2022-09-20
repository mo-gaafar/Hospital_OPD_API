# django models imports
from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

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
    department = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    prescriber = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    room = models.OneToOneField(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
