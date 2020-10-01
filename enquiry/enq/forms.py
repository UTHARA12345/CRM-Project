from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from enq.models import *
from django import forms
class EnquiryFrm(ModelForm):
    class Meta:
        model=Enquiry
        fields=['student_name','address','qualification','college_name','course','Batch_code','phone_no','email','followup_date','sourse','councillor','status']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'Batch_code': forms.Select(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'followup_date':forms.SelectDateWidget(),
            'sourse': forms.TextInput(attrs={'class': 'form-control'}),
            'councillor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


        def clean(self):
            print("clean enquiry")
class EnquiryUpdateFrm(ModelForm):
    class Meta:
        model=Enquiry
        fields=['student_name','address','qualification','college_name','course','Batch_code','phone_no','email','followup_date','sourse','councillor','status']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'Batch_code': forms.Select(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'followup_date':forms.SelectDateWidget(),
            'sourse': forms.TextInput(attrs={'class': 'form-control'}),
            'councillor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        def clean(self):
            print("clean enquiry update")


class CourseFrm(ModelForm):
    class Meta:
        model=Course
        fields=['course_name','course_duration','course_date']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'course_date': forms.SelectDateWidget(),
        }

    def clean(self):
        print("clean course")

class CourseUpdateFrm(ModelForm):
    class Meta:
        model=Course
        fields=['course_name','course_duration','course_date']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'course_date': forms.SelectDateWidget(),
        }
    def clean(self):
        print("clean course")

class BatchFrm(ModelForm):
    class Meta:
        model=Batch
        fields=['Batch_code','course_name','Batch_Date','Batch_Status']
        widgets = {
            'Batch_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.Select(attrs={'class': 'form-control'}),
            'Batch_Date': forms.SelectDateWidget(),
            'Batch_Status': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        print("clean batch")
class BatchUpdateFrm(ModelForm):
    class Meta:
        model=Batch
        fields=['Batch_code','course_name','Batch_Date','Batch_Status']
        widgets={
            'Batch_code':forms.TextInput(attrs={'class':'form-control'}),
            # 'Batch_Date':forms.DateInput(format=('%y/%m/%d'),attrs={'class':'form-contol','type':'date'})
            'course_name': forms.Select(attrs={'class': 'form-control'}),
            'Batch_Date': forms.SelectDateWidget(),
            'Batch_Status': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        print("clean batch")
class SearchDateFrm(ModelForm):
    class Meta:
        model=Enquiry
        fields=['followup_date','enquiry_date']
        widgets={
            'followup_date':forms.SelectDateWidget(),
            'enquiry_date': forms.SelectDateWidget(),
        }
    def clean(self):
        print("clean date")
        # cleaned_data=super().clean()
        # date=cleaned_data.get('followup_date')
        # qs=Enquiry.objects.filter(followup_date=date,status='1')
        #
        # if(qs):
        #     print("date found")
        # else:
        #     msg="No Followups"
        #     self.add_error("followup_date",msg)

class NewAdmissionFrm(ModelForm):
    class Meta:
        model=Admission
        exclude=['date']
        widgets={
            'admission_no': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name':forms.TextInput(attrs={'class': 'form-control'}),
            'enquiryid': forms.TextInput(attrs={'class': 'form-control'}),
            'coursefee': forms.TextInput(attrs={'class': 'form-control'}),
            'Batch_code': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        print("clean admission")

class PaymentFrm(ModelForm):
    class Meta:
        model=Payment
        exclude=['payment_date','student_name']

    def clean(self):
        print("clean payment")

class PayFrm(ModelForm):
    class Meta:
        model=Payment
        fields=['admission_no']

    def clean(self):
        print("clean pay")

class CreateUserFrm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'password1': forms.TextInput(attrs={'class': 'form-control'}),
            # 'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CouncillorFrm(ModelForm):
    class Meta:
        model=Councillor
        fields="__all__"
        widgets = {
            'councillor_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def clean(self):
            print("clean councillor")

class CouncillorUpdateFrm(ModelForm):
    class Meta:
        model=Councillor
        fields="__all__"
        widgets = {
            'councillor_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def clean(self):
            print("clean councillor")