from django.shortcuts import render
from regloginapp.models import RegistrationData
from regloginapp.forms import RegistrationForm
from django.http.response import HttpResponse
from regloginapp.forms import LoginForm

def index(request):
    return render(request,'indexfile.html')

def Registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            firstname1=request.POST.get("firstname")
            lastname1=request.POST.get("lastname")
            username1=request.POST.get("username")
            password1=request.POST.get("password")
            mobile1=request.POST.get("mobile")
            email1=request.POST.get("email")
            gender1=rform.cleaned_data.get("gender")
            date_of_birth1=rform.cleaned_data.get("date_of_birth")
            data=RegistrationData(
                firstname=firstname1,
                lastname=lastname1,
                username=username1,
                password=password1,
                mobile=mobile1,
                email=email1,
                gender=gender1,
                date_of_birth=date_of_birth1
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'registrationfile.html',{'lucky':rform})
        else:
            return HttpResponse("User Missing Some Values")
    else:
        rform = RegistrationForm()
        return render(request, 'registrationfile.html', {'lucky': rform})

def Login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get("username")
            pwd=request.POST.get("password")

            uname1=RegistrationData.objects.filter(username=uname)
            pwd1=RegistrationData.objects.filter(password=pwd)

            if uname1:
                if pwd1:
                    return  HttpResponse("success")
                else:
                    return HttpResponse("enter correct pass")
            else:
                return HttpResponse("enter correct details")
        else:
            return HttpResponse("Missing Some Values")
    else:
        lform=LoginForm()
        return render(request,'Login.html', {'lucky': lform})
