from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Job, CheckBox
from django.contrib.auth.forms import UserCreationForm
# Create your views here.from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import CheckBoxForm



def job(request):
    if request.user.is_authenticated:
        obj1 = Job.objects.get(id=1)
        obj2 = Job.objects.get(id=2)
        obj3 = Job.objects.get(id=3)
        obj4 = Job.objects.get(id=4)
        obj5 = Job.objects.get(id=5)

        if request.method == "POST":
            form = CheckBoxForm(request.POST)

            if form.is_valid():
                checkbox = form.save(commit=False)

                checkbox.user = request.user
                checkbox.save()

                return redirect('/register/thankyou')
        else:
            form = CheckBoxForm()
            context = {"form": form,
                       "company1": obj1.company,
                       "profile1": obj1.profile,
                       "vacancy1": obj1.vacancy,
                       "location1": obj1.location,
                       "salary1": obj1.salary,

                       "company2": obj2.company,
                       "profile2": obj2.profile,
                       "vacancy2": obj2.vacancy,
                       "location2": obj2.location,
                       "salary2": obj2.salary,
                       "company3": obj3.company,
                       "profile3": obj3.profile,
                       "vacancy3": obj3.vacancy,
                       "location3": obj3.location,
                       "salary3": obj3.salary,
                       "company4": obj4.company,
                       "profile4": obj4.profile,
                       "vacancy4": obj4.vacancy,
                       "location4": obj4.location,
                       "salary4": obj4.salary,
                       "company5": obj5.company,
                       "profile5": obj5.profile,
                       "vacancy5": obj5.vacancy,
                       "location5": obj5.location,
                       "salary5": obj5.salary,

                       }

            return render(request, "testing.html", context)
    else:
        return render(request, 'pleaselogin.html')
