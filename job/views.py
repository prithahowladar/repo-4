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


@login_required
def job(request):
    obj1 = Job.objects.get(id = 1)
    obj2 = Job.objects.get(id=2)
    obj3 = Job.objects.get(id=3)

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
                   "company2": obj2.company,
                   "profile2": obj2.profile,
                   "vacancy2": obj2.vacancy,
                   "location2": obj2.location,
                   "company3": obj3.company,
                   "profile3": obj3.profile,
                   "vacancy3": obj3.vacancy,
                   "location3": obj3.location,
                   }

        return render(request, "job2.html", context)
