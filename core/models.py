from django.db import models

# Create your models here.

class Degree(models.Model):
    degree_name = models.CharField(max_length=150)

    def __str__(self):
        return self.degree_name

class Program(models.Model):
    program_name = models.CharField(max_length=150)
    degree = models.ForeignKey(
        Degree, max_length=150, on_delete=models.CASCADE, related_name="program"
    )

    def __str__(self):
        return self.program_name

class University(models.Model):
    university_name = models.CharField(max_length=150)
    programs = models.ManyToManyField(Program)

    def __str__(self):
        return self.university_name