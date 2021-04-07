from django.shortcuts import render,redirect
from django.contrib.auth.views import TemplateView
from crm_automation.forms import Loginform,courseform,Batchform,Studentform,Registrationform,Admissionform,Paymentform
from crm_automation.models import Course,Batch,Enquiry,Registration,Feepayment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
class Login(TemplateView):
    form_class=Loginform
    template_name = "crm_automation/login.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return render(request,"crm_automation/home.html")
            else:
                form = self.form_class(request.POST)
                self.context["form"] = form
                return render(request, self.template_name, self.context)
class Logout(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
class create_course(TemplateView):
    form_class=courseform
    template_name = "crm_automation/create.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"crm_automation/home.html")
        return render(request, self.template_name, self.context)
# class course_list(TemplateView):
#     model=Course
#     template_name = "crm_automation/list.html"
#     context={}
#     def get(self,request,*args,**kwargs):
#         item=self.model.objects.all()
#         self.context["item"]=item
#         return render(request,self.template_name,self.context)
class Detail_view(TemplateView):
    model=Batch
    form_class=Batchform
    template_name = "crm_automation/batchdetail.html"
    context={}
    def get(self,request,*args,**kwargs):
        batch = self.model.objects.last()
        if batch:
            last_enquiry = batch.batch_code
            list = int(last_enquiry.split('-')[0]) + 1
            batch_code =str(list)
        else:
           batch_code= "1000"
        form=self.form_class
        self.context["form"]=form(initial={"batch_code":batch_code})
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

        return render(request, self.template_name, self.context)
class detail_list(TemplateView):
    model=Batch
    template_name = "crm_automation/detail_list.html"
    context={}
    def get(self,request,*args,**kwargs):
        item=self.model.objects.all()
        self.context["item"]=item
        return render(request,self.template_name,self.context)
class course_view(TemplateView):
    model=Batch
    template_name = "crm_automation/courseview.html"
    context={}
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=self.model.objects.get(id=id)
        self.context["item"]=item
        return render(request,self.template_name,self.context)
class course_edit(TemplateView):
    model=Batch
    form_class=Batchform
    template_name = "crm_automation/edit.html"
    context={}
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        item = self.model.objects.get(id=id)
        form = self.form_class(instance=item)
        self.context["item"] = item
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        item = self.model.objects.get(id=id)
        form=self.form_class(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect("detaillist")
        return render(request, self.template_name, self.context)
class course_delete(TemplateView):
    model=Batch
    template_name = "crm_automation/detail_list.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=self.model.objects.get(id=id)
        item.delete()
        return redirect("detaillist")

# displaying for students
class course_list(TemplateView):
    model=Course
    template_name = "crm_automation/list.html"
    context={}
    def get(self,request,*args,**kwargs):
        item=self.model.objects.all()
        self.context["item"]=item
        return render(request,self.template_name,self.context)
class coursedetail(TemplateView):
    model=Batch
    template_name = "crm_automation/detailfor.html"
    context={}
    def get(self,request,*args,**kwargs):
        item=self.model.objects.all()
        self.context["item"]=item
        return render(request,self.template_name,self.context)
class about_course(TemplateView):
    template_name = "crm_automation/aboutpage.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
class Registration_for(TemplateView):
    model = User
    form_class = Registrationform
    template_name = "crm_automation/registration.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "crm_automation/home.html")
        else:
            form = self.form_class(request.POST)
            self.context["form"] = form
            return render(request, self.template_name, self.context)
class Stud_login(TemplateView):
    form_class=Loginform
    template_name = "crm_automation/studlogin.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return render(request,"crm_automation/counsillorpage.html")
            else:
                form = self.form_class(request.POST)
                self.context["form"] = form
                return render(request, self.template_name, self.context)
class counsillorpage(TemplateView):
    template_name = "crm_automation/counsillorpage.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
class Stu_reg(TemplateView):
    model=Enquiry
    form_class=Studentform
    template_name = "crm_automation/studentinfo.html"
    context={}
    def get(self,request,*args,**kwargs):
        order = self.model.objects.last()
        if order:
            last_enquiry = order.enquiry_id
            list = int(last_enquiry.split('-')[1]) + 1
            enquiry_id = 'EQ-' + str(list)
        else:
            enquiry_id = "EQ-1000"
        form = self.form_class(initial={"enquiry_id": enquiry_id})
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            date=form.cleaned_data.get("followupdate")
            if(date<date.today()):
                return render(request,self.template_name,{'message':'notvalid'})
            else:
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("counsil")

        return render(request, self.template_name, self.context)
class admission(TemplateView):
    model=Registration
    form_class=Admissionform
    template_name = "crm_automation/admissionpage.html"
    context={}
    def get(self,request,*args,**kwargs):
        pay = self.model.objects.last()
        if pay:
            last_enquiry = pay.admission_no
            list = int(last_enquiry.split('-')[1]) + 1
            admission_no = 'AD-' + str(list)
        else:
            admission_no= "AD-1000"
        enquiry_id=kwargs.get('enquiry_id')
        form = self.form_class
        self.context["form"]=form(initial={'enquiry_id':enquiry_id,"admission_no": admission_no})
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            enquiry_id=kwargs.get("enquiry_id")
            enquiry_obj=Enquiry.objects.get(enquiry_id=enquiry_id)
            enquiry_obj.admission_status='admitted'
            enquiry_obj.save()
            return redirect("counsil")
        return render(request, self.template_name, self.context)
class admission_list(TemplateView):
    model=Enquiry
    template_name = "crm_automation/admissionlist.html"
    context={}
    def get(self,request,*args,**kwargs):
        obj=self.model.objects.all()
        self.context["obj"]=obj
        return render(request, self.template_name, self.context)
# class admission_list_delete(TemplateView):
#     model = Enquiry
#     def get(self, request, *args, **kwargs):
#             obj = self.model.objects.all()
#             obj.delete()
#             return redirect("admitlist")
class Payment(TemplateView):
    form_class=Paymentform
    template_name = "crm_automation/feepayment.html"
    context={}
    def get(self,request,*args,**kwargs):
        admission_no=kwargs.get("admission_no")
        form = self.form_class(initial={"admission_no":admission_no})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            admission_no=form.cleaned_data.get("admission_no")
            enquiry_obj = Registration.objects.get(admission_no=admission_no)
            enquiry_obj.registration_status = 'registered'
            enquiry_obj.save()
            return redirect("counsil")
class Feepaymentlist(TemplateView):
    model = Registration
    template_name = "crm_automation/studentregistrationlist.html"
    context = {}
    def get(self, request, *args, **kwargs):
        obj = self.model.objects.all()
        self.context["obj"] = obj
        return render(request, self.template_name, self.context)
class Finallist(TemplateView):
    model = Feepayment
    template_name = "crm_automation/paymentlist.html"
    context = {}
    def get(self, request, *args, **kwargs):
        obj = self.model.objects.all()
        self.context["obj"] = obj
        return render(request, self.template_name, self.context)
class studlogout(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("studlogin")


