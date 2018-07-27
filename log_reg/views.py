from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse

from .forms import RegisterForm, LoginForm

class LogRegView(View):
    form_class = RegisterForm
    template_name = "log_reg/registration_form.html"

    def get(self, request):
        form = self.form_class(None) # none = not bound
        form2 = LoginForm()
        
        if request.user is not None:
            print(request.user.username)
        return render(request, self.template_name, {"form":form, "form2":form2})
        
    def post(self,request):
        form = self.form_class(None) 
        form2 = LoginForm()

        # Actions based on hidden form-type field
        if request.POST["form-type"] == "register":
    
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save(commit = False)
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user.set_password(password)
                user.save()
                print("user created")
                return redirect("log_reg")
            else:
                print("form not valid")
                # Can add a message for error in form submission
                return redirect("log_reg")

        if request.POST["form-type"] == "login":
            submitted_form = LoginForm(request.POST)
            if submitted_form.is_valid():
                try:
                    username = submitted_form.cleaned_data["username"]
                    password = submitted_form.cleaned_data["password"]
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    # change to redirect to home page
                    return redirect("secret_santa/")
                except:
                    print("user not authentic")
                    return render(request, self.template_name, {"form": form, "form2": form2})

            return redirect("log_reg")

