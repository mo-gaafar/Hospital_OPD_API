# django models imports
from django.db import models

from dateutil.relativedelta import relativedelta
from datetime import datetime

# Create your models here.


class Department(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField(unique=True, primary_key=True)
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
    # age = models.IntegerField()
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

    # # convert from birthdate to age
    # age = models.IntegerField()

    # def get_age(self):
    #     return relativedelta(self.birth_date.days, datetime.date.now()).years

    # # overriding save method to update the age field
    # def save(self, **kwargs):
    #     self.age = self.get_age()
    #     return super(Patient, self).save(**kwargs)

    def __str__(self):
        return self.name
