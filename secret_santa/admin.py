from django.contrib import admin
from .models import List, Member, List_Member

# Register your models here.
admin.site.register(List)
admin.site.register(Member)
admin.site.register(List_Member)