import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse, reverse_lazy

from .models import List, Member

from .forms import ListForm, MemberForm

class HomeView(View):

    def get(self, request):
        today = datetime.date.today()
        current_day = today.strftime('%A, %x')
        xmas = datetime.date(2017, 12, 25)
        form = ListForm()
        user = User.objects.get(username= "user10")
        context = {
        'today': current_day, 
        'xmas':xmas, 
        "form": form,
        "user": user
        }
        return render(request, "secret_santa/main.html", context)

    def post(self, request):
        form = ListForm(request.POST)
        if form.is_valid():
            print("list saved")
            List.objects.create(
                list_name=form.cleaned_data['list_name'],
                # Make this equal to user for login in
                creator= User.objects.get(username = request.POST["creator"]),
                gift_max= form.cleaned_data["gift_max"]
            )
        return redirect("/secret_santa/")


class DeleteListView(DeleteView):
    model = List
    success_url = reverse_lazy("santa_home")

    def get(self, request):
        return render(request, "secret_santa/list_confirm_delete.html")


class EnterMembersView(View):
    
    def get(self, request):
        form = MemberForm()
        current_list = List.objects.last()
        context = {
        "form": form,
        "current_list": current_list
        }
        return render(request, "secret_santa/enter_members.html", context)

    def post(self, request):
        form = MemberForm(request.POST)
        if form.is_valid():
            print("members saved")
            Member.objects.create(
                member_list=List.objects.last(),
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
            )
        return redirect("/secret_santa/enter_members")


 
def logout_view(request):
    logout(request)
    return redirect("/")