from django.db import models
from datetime import date
import uuid
from django.db import models


# Create your models here
class Course(models.Model):

    course_name=models.CharField(max_length=120,unique=True)
    course_duration=models.CharField(max_length=50)
    course_date=models.DateField()
    def __str__(self):
        return str(self.course_name)

class Batch(models.Model):

    Batch_code=models.CharField(max_length=120,unique=True)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_Date=models.DateField()
    action=(('1','yet_to_begin'),
            ('2','started'),
            ('3','completed'))
    Batch_Status=models.CharField(max_length=120,choices=action)
    def __str__(self):
        return str(self.Batch_code)

class Councillor(models.Model):
    councillor_name=models.CharField(max_length=60)
    def __str__(self):
        return str(self.councillor_name)


class Enquiry(models.Model):
    enquiry_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_name=models.CharField(max_length=120)
    address=models.CharField(max_length=250)
    qualification=models.CharField(max_length=120)
    college_name=models.CharField(max_length=120)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_code=models.ForeignKey(Batch,on_delete=models.CASCADE)
    phone_no=models.IntegerField()
    email=models.EmailField()
    enquiry_date=models.DateField(default=date.today())
    followup_date=models.DateField()
    sourse=models.CharField(max_length=120)
    councillor=models.ForeignKey(Councillor,on_delete=models.CASCADE)

    action=(('1','call_back'),
            ('2','admitted'),
            ('3','cancel'))
    status=models.CharField(max_length=30,choices=action)
    def __str__(self):
        return str(self.enquiry_id)


class Admission(models.Model):
    admission_no=models.CharField(max_length=20,unique=True)
    student_name=models.CharField(max_length=120)
    enquiryid=models.CharField(max_length=50)
    coursefee=models.IntegerField()
    Batch_code=models.ForeignKey(Batch,on_delete=models.CASCADE)
    date=models.DateField(default=date.today())
    def __str__(self):
        return self.admission_no

class Payment(models.Model):
    admission_no=models.CharField(max_length=15)
    student_name = models.CharField(max_length=120)
    amount=models.IntegerField()
    cfee=models.ForeignKey(Admission,on_delete=models.CASCADE)
    payment_date=models.DateField(default=date.today())
    enquiryid=models.CharField(max_length=50)
    def __str__(self):
        return self.amount