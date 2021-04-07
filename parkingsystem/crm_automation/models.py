from django.db import models

# Create your models here.
from django.db.models import ImageField


class Course(models.Model):
    course_name=models.CharField(max_length=120,unique=True)
    course_duration=models.CharField(max_length=10)

    def __str__(self):
        return self.course_name
class Batch(models.Model):
    batch_code=models.CharField(max_length=50,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    starting_date=models.DateField()
    course_fees=models.IntegerField()
    choicess={
        ('yettobegin','yettobegin'),
        ('progress','progress'),
        ('completed','completed'),
    }
    batch_status=models.CharField(max_length=120,choices=choicess)

    def __str__(self):
        return self.batch_code
class Enquiry(models.Model):
    enquiry_id=models.CharField(max_length=120,primary_key=True)
    student_name=models.CharField(max_length=100)
    address=models.TextField()
    qualification=models.CharField(max_length=100)
    collegename=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    phone=models.CharField(max_length=120)
    email=models.CharField(max_length=100)
    batch_code=models.ForeignKey(Batch,on_delete=models.CASCADE)
    followupdate=models.DateField()
    choice = {
        ('callback','callback'),
        ('admitted', 'admitted'),
        ('notadmitted', 'notadmitted'),
    }
    admission_status = models.CharField(max_length=120, choices=choice)

    def __str__(self):
        return str(self.enquiry_id)

class Registration(models.Model):
    admission_no=models.CharField(max_length=120,unique=True)
    enquiry_id=models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    coursefees=models.IntegerField()
    batch_code = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date=models.DateField()
    choice = {
        ('registered', 'registered'),
        ('notregistered','notregistered')
    }
    registration_status = models.CharField(max_length=120, null=True,choices=choice)
    def __str__(self):
        return str(self.admission_no)
class Feepayment(models.Model):
    admission_no=models.ForeignKey(Registration,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_date=models.DateField()

    def __str__(self):
        return str(self.admission_no)