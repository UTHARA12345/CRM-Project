from django.db.models import Count
# from itertools import count
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum
from django.core.paginator import Paginator
from enq.models import *
from enq.forms import *
# Create your views here.
from datetime import date
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView


from enq.models import *
class Home(TemplateView):
    template_name = "enq/home.html"


    #object_list=Enquiry.objects.all()
    #context={}
    #contect["object_list"]=object_list
    #return render (request, self.template_name,context)
# @method_decorator(login_required)
class RegistrationPage(TemplateView):
    model=User
    template_name = "reg/regis.html"
    form_class=CreateUserFrm()
    def get(self, request, *args, **kwargs):
        contex={}
        contex["form"]=self.form_class
        return render(request,self.template_name,contex)

    def post(self, request, *args, **kwargs):
        form=CreateUserFrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            contex = {}
            contex["form"] = self.form_class
            return render(request, self.template_name, contex)
class LoginUser(TemplateView):
    model=User
    template_name = "reg/login.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        context={}

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages='incorrect username or password'
            context["messages"]=messages
        return render(request, self.template_name,context)


def logoutuser(request):
    logout(request)
    return redirect("login")

class AddCouncillor(TemplateView):
    model=Councillor
    template_name = "batch/councillor_add.html"
    form_class=CouncillorFrm
    def get(self, request, *args, **kwargs):
        qs=Councillor.objects.all()
        form=self.form_class
        context={}
        context["form"]=form
        context["councillor"]=qs
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addcouncillor")
        else:
            context={}
            context[form]=form
            return render(request,self.template_name,context)

class CouncillorDelete(DeleteView):
    model = Councillor

    def get(self, request, *args, **kwargs):
        c_id = self.kwargs.get("pk")
        qs = Councillor.objects.get(id=c_id).delete()
        context = {}
        context["form"] = qs
        return redirect("addcouncillor")
class CouncillorUpdate(UpdateView):
    model=Councillor
    form_class = CourseUpdateFrm
    template_name = "batch/councillor_update.html"
    def get(self, request, *args, **kwargs):
        c_id=self.kwargs.get('pk')
        qs=Councillor.objects.get(id=c_id)
        form=self.form_class(instance=qs)
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        b_id = self.kwargs.get('pk')
        qs = Councillor.objects.get(id=b_id)
        form=self.form_class(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("addcouncillor")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)


class Enquiry_list(ListView):
    model = Enquiry
    template_name = "enq/enq_list.html"
    context_object_name = "enquiry"
    # def get(self, request, *args, **kwargs):
    #     qs = Enquiry.objects.filter(status="1,2")
    #     context={}
    #     context["enquiry"]=qs
    #     #
    #     return render(request,self.template_name,context)


# class  Enquiry_Create(CreateView):
#     model = Enquiry
#     form_class = EnquiryFrm
#     template_name = "enq/enq_create.html"
#     success_url = reverse_lazy("listenquiry")
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(self.__class__, self).dispatch(request, *args, **kwargs)


class  Enquiry_Create(TemplateView):
    model = Enquiry
    form_class = EnquiryFrm
    template_name = "enq/enq_create.html"
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        form=self.form_class(initial={'enquiryid': id})
        context={}
        context["form"]=form
        # context["id"]=id
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        # id = self.kwargs.get("pk")
        # qs = Enquiry.objects.get(enquiry_id=id)
        form=self.form_class(request.POST)
        if form.is_valid():
            en=form.save(commit=False)
            enquiry_id=en.enquiry_id
            # id = self.kwargs.get("pk")
            # qs=Enquiry.objects.filter(status='2')
            # qs = Enquiry.objects.get(enquiry_id=id)
            en.save()
            status=form.cleaned_data['status']
            if(status=='2'):
                return redirect('newadmission',pk=enquiry_id)
            else:
                return redirect('listenquiry')
        else:
            context={}
            context["form"]=form
            return render(request,self.template_name,context)



class EnquiryDetail(DetailView):
    model = Enquiry
    template_name = "enq/enq_details.html"
    context_object_name = "details"

    # details=Enquiry.objects.get(id=pk)
    # context={}
    # contect["object_list"]=object_list
    # return render (request, self.template_name,context)

class EnquiryUpdate(UpdateView):
    model = Enquiry
    form_class = EnquiryUpdateFrm
    template_name = "enq/enq_update.html"
    success_url = reverse_lazy("listenquiry")
    # def get(self, request, *args, **kwargs):
    #     e_id=self.kwargs.get('pk')
    #     qs=Course.objects.get(id=e_id)
    #     form=self.form_class(instance=qs)
    #     context={}
    #     context["form"]=form
    #     return render(request,self.template_name,context)
    # def post(self, request, *args, **kwargs):
    #     e_id = self.kwargs.get('pk')
    #     qs = Course.objects.get(id=e_id)
    #     form=self.form_class(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listenquiry")
    #     else:
    #         context = {}
    #         context["form"] = form
    #         return render(request, self.template_name, context)
class EnquiryDelete(DeleteView):
    model = Enquiry
    form_class = EnquiryUpdateFrm
    template_name = "enq/enq_delete.html"
    success_url = reverse_lazy("listenquiry")
class FollowUp(TemplateView):
    model = Enquiry
    template_name = "enq/followups.html"

    def get_queryset(self):
        return Enquiry.objects.filter(followup_date= date.today(),status="1")
        # return Enquiry.objects.filter(status="1")
    def get(self, request, *args, **kwargs):
        context={}
        context["enquires"]=self.get_queryset()
        return render(request,self.template_name,context)

# class FollowUpDetail(TemplateView):
#     model = Enquiry
#     template_name = "enq/followupdetails.html"
#     form_class = EnquiryUpdateFrm
#     def get(self,request,*args,**kwargs):
#         id = self.kwargs.get('pk')
#         qs=Enquiry.objects.get(enquiry_id=id)
#         form=self.form_class(instance=qs)
#         context={}
#         context["form"]=form
#         return render(request,self.template_name,context)
#     def post(self,request,*args,**kwargs):
#         form=self.form_class(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect("followup")
#         else:
#             context = {}
#             context["form"] = form
#             return render(request, self.template_name,context)
class FollowUpDetail(UpdateView):
    model = Enquiry
    form_class = EnquiryUpdateFrm
    template_name = "enq/followupdetails.html"
    # success_url = reverse_lazy("followup")
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        qs=Enquiry.objects.get(enquiry_id=id)
        form=self.form_class(instance=qs)
        context = {}
        context["form"]= form
        context["id"]=id
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        qs=Enquiry.objects.get(enquiry_id=id)
        form=self.form_class(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("followup")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)
# class SearchDate(TemplateView):
#     model=Enquiry
#     form_class=SearchDateFrm
#     template_name = "enq/followup_searchdate.html"
#     def get(self, request, *args, **kwargs):
#         form=self.form_class
#         context={}
#         context["form"]=form
#         return render(request,self.template_name,context)
#
#     def post(self, request, *args, **kwargs):
#         form=self.form_class(request.POST)
#         if(form.is_valid()):
#
#             dte=form.cleaned_data['followup_date']
#             dte2 = form.cleaned_data['enquiry_date']
#             print(dte)
#             qs=Enquiry.objects.filter(followup_date__lte=dte,followup_date__gte=dte2,status="1")
#             if(qs):
#                 print(qs)
#                 context={}
#                 context["enquires"]=qs
#                 template_name="enq/followups.html"
#                 return render(request,template_name,context)
#             else:
#                 form=self.form_class(request.POST)
#                 context={}
#                 context["form"]=form
#                 return render(request,self.template_name,context)
#         else:
#             form=self.form_class(request.POST)
#             context = {}
#             context["form"] = form
#             return render(request, self.template_name, context)
class SearchDate(TemplateView):
    model=Enquiry
    template_name = "enq/followup_searchdate.html"
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        # qs2 = Enquiry.objects.get(enquiry_id=id)
        context={}
        context["id"]=id
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        # id = self.kwargs.get("pk")
        # qs2 = Enquiry.objects.get(enquiry_id=id)
        datef = request.POST['fromdate']
        datet = request.POST['todate']
        qs = Enquiry.objects.filter(followup_date__lte=datet, followup_date__gte=datef, status='1')
        context = {}
        context["data"] = qs
        # context["id"]=id
        return render(request,self.template_name, context)



class NewAdmission(TemplateView):
    model=Admission
    template_name = "admi/take_admi.html"
    form_class=NewAdmissionFrm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")

        form=self.form_class(initial={'enquiryid':id})
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            id=self.kwargs.get("pk")
            qs=Enquiry.objects.get(enquiry_id=id)
            qs.status='2'
            qs.save()
            admission_no=form.cleaned_data['admission_no']

            form.save()
            # request.method='GET'
            # return PaymentDetails.as_view()(self.request,*args, **kwargs)
            return redirect("payment",pk=admission_no)
        else:
            form=self.form_class(request.POST)
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)
# class (TemplateView):
#     model = Enquiry
#     template_name = "enq/followups.html"
#
#     def get_queryset(self):
#         return Enquiry.objects.filter(followup_date= date.today(),status="1")
#     def get(self, request, *args, **kwargs):
#         context={}
#         context["enquires"]=self.get_queryset()
#         return render(request,self.template_name,context)

class PaymentDetails(TemplateView):
    model=Payment
    template_name = "admi/payment.html"
    form_class=PaymentFrm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        qs=Admission.objects.get(admission_no=id)
        qs3=Payment.objects.filter(admission_no=id)
        enqid=qs.enquiryid
        fees=qs.coursefee
        qs1=Enquiry.objects.get(enquiry_id=enqid)

        qs2=Payment.objects.filter(admission_no=id).values('amount').annotate(remaining=Sum('amount'))
        print(qs2)
        if(qs2):
            remaining=fees-(qs2[0]['remaining'])
        else:
            remaining=fees

        form=self.form_class(initial={'admission_no':id,'enquiryid':enqid})
        context={}
        context["form"]=form
        # context={}
        context["pay"]=qs1
        context["remaining"]=remaining
        context["detail"]=qs3

        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = self.form_class(request.POST)
            context = {}
            context["form"] = form

            return render(request, self.template_name, context)

class Pay(TemplateView):
    model=Payment
    template_name = "admi/pay.html"
    form_class=PayFrm
    def get(self, request, *args, **kwargs):
        form=self.form_class
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            id=form.cleaned_data["admission_no"]
            return redirect("payment",pk=id)
        else:
            form = self.form_class(request.POST)
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)

class SearchName(TemplateView):
    model=Payment
    template_name = "enq/searching.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        srch = request.POST['srh']
        if srch:
            match = Admission.objects.filter(Q(student_name__istartswith=srch)).distinct()

            if match:
                return render(request,self.template_name, {"sr": match})
            else:
                messages.error(request, 'no result found')
        else:
            return redirect("search")
        return render(request,self.template_name)



# class Admission_list(ListView):
#     model = Enquiry
#     template_name = "admi/admilist.html"
#     def get(self, request, *args, **kwargs):
#         id = self.kwargs.get("pk")
#         # qs = Enquiry.objects.get(enquiry_id=id)
#         qs=Enquiry.objects.filter(status="2").values('Batch_code__admission_no','student_name','Batch_code')
#         context={}
#         context["admi"]=qs
#         return render(request,self.template_name,context)


# p=Pay()

# p1=PaymentDetails
# p.get()
# p.post()




class AddCourse(TemplateView):
    model=Course
    template_name = "course/course_add.html"
    form_class=CourseFrm
    def get(self, request, *args, **kwargs):
        qs=Course.objects.all()
        form=self.form_class
        context={}
        context["form"]=form
        context["courses"]=qs
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcourse')
        else:
            context={}
            context["form"]=form
            return render(request,self.template_name,context)

class AddBatch(TemplateView):
    model=Batch
    template_name = "batch/batch_create.html"
    form_class=BatchFrm
    def get(self, request, *args, **kwargs):
        qs=Batch.objects.all()
        form=self.form_class
        context={}
        context["form"]=form
        context["batch"]=qs
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addbatch")
        else:
            context={}
            context[form]=form
            return render(request,self.template_name,context)
class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateFrm
    template_name = "course/course_update.html"
    def get(self, request, *args, **kwargs):
        c_id=self.kwargs.get('pk')
        qs=Course.objects.get(id=c_id)
        form=self.form_class(instance=qs)
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        c_id = self.kwargs.get('pk')
        qs = Course.objects.get(id=c_id)
        form=self.form_class(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("addcourse")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)
class CourseDelete(DeleteView):
     model = Course
#     form_class=CourseUpdateFrm
#     template_name = "course/course_delete.html"
#     # success_url = reverse_lazy("addcourse")
     def get(self, request, *args, **kwargs):
        d_id=self.kwargs.get("pk")
        qs=Course.objects.get(id=d_id).delete()
#         form = self.form_class(instance=qs)
        context = {}
        context["form"] = qs
        return redirect("addcourse")


class BatchDelete(DeleteView):
    model = Batch

    def get(self, request, *args, **kwargs):
        d_id = self.kwargs.get("pk")
        qs = Batch.objects.get(id=d_id).delete()
        context = {}
        context["form"] = qs
        return redirect("addbatch")
class BatchUpdate(UpdateView):
    model=Batch
    form_class = BatchUpdateFrm
    template_name = "batch/batch_update.html"
    def get(self, request, *args, **kwargs):
        b_id=self.kwargs.get('pk')
        qs=Batch.objects.get(id=b_id)
        form=self.form_class(instance=qs)
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        b_id = self.kwargs.get('pk')
        qs = Batch.objects.get(id=b_id)
        form=self.form_class(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("addbatch")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)

class BatchReport(TemplateView):
    model=Enquiry
    template_name = "batch/batchreport.html"
    def get(self, request, *args, **kwargs):
        b_id = self.kwargs.get('pk')

        qs_enq=Enquiry.objects.filter(Batch_code=b_id).values('Batch_code__Batch_code','student_name','phone_no','councillor','councillor').annotate(enq1=(Count('enquiry_id')))
        qs_stu=Enquiry.objects.filter(Batch_code=b_id,status='2').values('Batch_code__Batch_code').annotate(stu=(Count('enquiry_id')))
        qs_stu2=Enquiry.objects.filter(Batch_code=b_id,status='1').values('Batch_code__Batch_code').annotate(stu2=(Count('enquiry_id')))
        # qs11=Admission.objects.get(id=b_id).values('Batch_code__Batch_Date','Batch_code','coursefee').annotate(enqadmitted11=(Count('admission_no')),fee=(Sum('coursefee')))
        # qs11=Enquiry.objects.filter()
        print(qs_enq)
        print(qs_stu)
        context={}

        context["form1"]=qs_enq
        context["form2"]=qs_stu
        context["form3"]=qs_stu2

        return render(request,self.template_name,context)
    # def post(self, request, *args, **kwargs):


class DashBoard(TemplateView):
    model=Enquiry
    template_name = "enq/home.html"
    # form_class=EnquiryFrm
    def get(self, request, *args, **kwargs):
        # id=self.kwargs.get('pk')
        qs_yet=Enquiry.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_Date','Batch_code__Batch_code').annotate(yet=(Count('enquiry_id')))
        qs_going=Enquiry.objects.filter(Batch_code__Batch_Status='2').values('Batch_code__Batch_Date','Batch_code__Batch_code').annotate(going=(Count('enquiry_id')))
        qs_complete=Enquiry.objects.filter(Batch_code__Batch_Status='2').values('Batch_code__Batch_Date','Batch_code__Batch_code').annotate(complete=(Count('enquiry_id')))


        qs=Enquiry.objects.filter(status='2',Batch_code__Batch_Status='1').values('Batch_code__Batch_Date','Batch_code__Batch_code').annotate(enq222=(Count('enquiry_id')))
        qs2=Enquiry.objects.all().values('Batch_code__Batch_Date','Batch_code__Batch_code','course__course_name').annotate(enqcount2=(Count('enquiry_id')))
        print(qs)
        context={}
        context["form"]=qs
        context["form2"]=qs2
        context["form3"]=qs_yet
        context["form4"]=qs_going
        context["form5"]=qs_complete
        return render(request, self.template_name, context)

class ReportUpdate(TemplateView):
    model = Enquiry
    template_name = "batch/coun_report.html"
    def get(self, request, *args, **kwargs):
        # qs1=Enquiry.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_Date','Batch_code','course__course_name').annotate(enqcount1=(Count('enquiry_id')))
        # qs11=Admission.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_Date','Batch_code','coursefee').annotate(enqadmitted11=(Count('admission_no')),fee=(Sum('coursefee')))
        # qs111=Payment.objects.filter().values('amount').annotate(amount1=(Sum('amount')))

        qs_counci=Enquiry.objects.filter(status='1').values('councillor__councillor_name').annotate(co=(Count('enquiry_id')))
        qs_counci2=Enquiry.objects.filter(status='2').values('councillor__councillor_name').annotate(co2=(Count('enquiry_id')))

        print(qs_counci)
        context={}
        context["form0"]=qs_counci
        context["form00"]=qs_counci2
        # context["form1"]=qs1
        # context["form11"]=qs11
        # context["form111"]=qs111
        return render(request, self.template_name, context)


class ViewBatch(TemplateView):
    model=Enquiry
    template_name = "batch/viewbatch.html"
    context_object_name = "details"
    form_class=EnquiryFrm
    def get(self, request, *args, **kwargs):
        qs2=Enquiry.objects.filter(status='2').values('student_name','qualification','college_name','phone_no','Batch_code__Batch_code').annotate(enq2=(Count('enquiry_id')))
        #qs=Enquiry.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_code').annotate(enq1=(Count('enquiry_id')))
        #qs=Admission.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_code','Batch_code__course_name','Batch_code__Batch_Date').annotate(enq1=(Count('admission_no')))
        qs=Admission.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_Date','Batch_code__Batch_code','coursefee','Batch_code__course_name__course_name').annotate(enqadmitted11=(Count('admission_no')),fee=(Sum('coursefee')))
        context={}
        context["form"]=qs
        context["form2"]=qs2
        return render(request,self.template_name,context)
class ViewBatchOngoing(TemplateView):
    model=Enquiry
    template_name = "batch/viewbatch2.html"

    form_class=EnquiryFrm
    def get(self, request, *args, **kwargs):
        qs2=Enquiry.objects.filter(status='2').values('student_name','qualification','college_name','phone_no','Batch_code__Batch_code').annotate(enq2=(Count('enquiry_id')))
        #qs=Enquiry.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_code').annotate(enq1=(Count('enquiry_id')))
        #qs=Admission.objects.filter(Batch_code__Batch_Status='1').values('Batch_code__Batch_code','Batch_code__course_name','Batch_code__Batch_Date').annotate(enq1=(Count('admission_no')))
        qs=Admission.objects.filter(Batch_code__Batch_Status='2').values('Batch_code__Batch_Date','Batch_code__Batch_code','coursefee','Batch_code__course_name__course_name').annotate(enqadmitted11=(Count('admission_no')),fee=(Sum('coursefee')))
        context={}
        context["form"]=qs
        context["form2"]=qs2
        return render(request,self.template_name,context)

from django.db.models import Q
# class SearchEnq(TemplateView):
#     model=Enquiry
#     template_name = "enq/enq_list.html"
#     form_class=EnquiryFrm
#     def get(self, request, *args, **kwargs):
#         return render(request,self.template_name)
#     def post(self, request, *args, **kwargs):
#         queryset_list=Enquiry.objects.all()
#         query=request.GET.get("q")
#         if query:
#             queryset_list=queryset_list.filter(
#                 q(student_name=query)|
#             ).distinct()
#         return render(request,self.template_name,queryset_list)
# class EnquiryPageList(ListView):
#     paginate_by = 12
#     model = Enquiry


def Search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=Admission.objects.filter(Q(student_name__istartswith=srch)).distinct()

            if match:
                return render(request,'enq/searching.html',{"sr":match})
            else:
                messages.error(request,'no result found')
        else:
            return redirect("search")
    return render(request,'enq/searching.html')