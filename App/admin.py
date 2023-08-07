from django.contrib import admin

# Register your models here.
from . models import MyDb
from . models import Admin

admin.site.register(MyDb) 
admin.site.register(Admin) 