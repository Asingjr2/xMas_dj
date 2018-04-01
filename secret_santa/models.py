from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

from base.models import BaseModel

# Create your models here.

class List(BaseModel):
    list_name = models.CharField(max_length=255, default='update name',  validators=[ MinLengthValidator(6)])
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_max = models.IntegerField( default=40, validators=[ MinValueValidator(0), MaxValueValidator(1000)]) 

    def __unicode__(self):
        return 'List Name = {}'.format(self.list_name)


class Member(BaseModel):
    member_list = models.ForeignKey(
        List, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, validators = [ MinLengthValidator(3)])
    email = models.CharField( max_length=200, default='unknown', validators = [
        EmailValidator])
    telephone = models.CharField(max_length=10, default='1234567890', validators = [ MinLengthValidator(10)])

    def __unicode__(self):
        return 'Member {}'.format(self.full_name)


class List_Member(BaseModel):
    lists = models.ManyToManyField(List)
    members = models.ManyToManyField(Member)