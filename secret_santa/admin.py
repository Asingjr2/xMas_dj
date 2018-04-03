from django.contrib import admin
from .models import List, Member, GiftPair

# Register your models here.
admin.site.register(List)
admin.site.register(Member)
admin.site.register(GiftPair)