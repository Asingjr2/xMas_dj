from django import forms
from django.forms import ModelForm, TextInput
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from .models import List, Member


class ListForm(forms.Form):
    list_name = forms.CharField( max_length=255, min_length=6)
    gift_max= forms.IntegerField(validators = [MaxValueValidator(1000), MinValueValidator(0)], widget = forms.NumberInput(attrs={'value': '40'}))



class ModifyListForm(forms.Form):
    list_name = forms.CharField( max_length=255, min_length=6)
    gift_max= forms.IntegerField(validators = [MaxValueValidator(1000), MinValueValidator(0)], widget = forms.NumberInput(attrs={'value': '40'}))

class MemberForm(ModelForm):
    
    class Meta:
        model = Member
        fields = [ "full_name", "email", "telephone"]
