import datetime
from random import shuffle

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse, reverse_lazy

from .models import List, Member, GiftPair
from .forms import ListForm, MemberForm, ModifyListForm

class HomeView(View):

    def get(self, request):
        today = datetime.date.today()
        current_day = today.strftime('%A, %x')
        xmas = datetime.date(2017, 12, 25)
        form = ListForm()
        user = User.objects.get(username= str(request.user.username))
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


class ListDetailView(DetailView):
    model = List
    pk_url_kwarg = 'list_id'


class DeleteListView(DeleteView):
    model = List
    success_url = reverse_lazy("secret_santa:santa_home")


class DeleteMemberView(DeleteView):
    model = Member
    success_url = reverse_lazy("secret_santa:santa_home")


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


class UpdateListView(UpdateView):
    model= List
    fields = ["list_name", "gift_max" ]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("secret_santa:santa_home")


class UpdateMemberView(UpdateView):
    model= Member
    fields = ["full_name", "email", "telephone"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("secret_santa:santa_home")


class AddMemberView(View):

    def get(self, request, pk):
            form = MemberForm()
            current_list = List.objects.get(id= pk)
            context = {
            "form": form,
            "current_list": current_list
            }
            return render(request, "secret_santa/add_member.html", context)

    def post(self, request,pk):
        form = MemberForm(request.POST)
        if form.is_valid():
            print("members saved")
            Member.objects.create(
                member_list=List.objects.get(id= request.POST["list_id"]),
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
            )
        return redirect("secret_santa:santa_home")


class ModifyListView(View):
    
    def get(self, request):
        form = ModifyListForm()
        user = User.objects.get(username= request.user.username)
        context = {
        "form": form,
        "user": user
        }
        return render(request, "secret_santa/modify_list.html", context)

    def post(self, request):
        form = ModifyListForm(request.POST)
        if form.is_valid():
            print("list saved")
            list_to_update = List.objects.get(list.id == request.POST["list.id"])
            list_to_update.list_name = form.cleaned_data['list_name']
            list_to_update.gift_max = form.cleaned_data['gift_max']
            list_to_update.save()
        return redirect("/secret_santa/")

 
class GiftPairsView(View):
    
    def get(self, request, pk):
        original_list = List.objects.get(id = pk)
        return render(request, "secret_santa/secret_santa_list.html", {"original_list": original_list})

    def post(self, request, pk):
        current_list = List.objects.get(id = pk)
        if current_list.giftpair_set.all().count() > 0:
            for pair in current_list.giftpair_set.all():
                if pair.gift_pair_original_list.id == current_list.id:
                    pair.delete()
        reordered_current_list_members = list(current_list.member_set.all())
        shuffle(reordered_current_list_members)
        print(reordered_current_list_members)
        string_gift_pairs_dict = {}
        for i, person in enumerate(reordered_current_list_members):
            try:
                string_gift_pairs_dict[person.full_name] = reordered_current_list_members[i+1]
                print("pair added")
            except IndexError:
                string_gift_pairs_dict[person.full_name] = reordered_current_list_members[0]
                print("pair not added")
        
        for k,v in string_gift_pairs_dict.items():
            GiftPair.objects.create(
                gift_pair_original_list= current_list, 
                santa= str(k),
                gift_receiver = Member.objects.get(id = v.id)
            )
        return redirect("secret_santa:gift_pairs",  pk=current_list.id)


def logout_view(request):
    logout(request)
    return redirect("/")