from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Dept)

admin.site.register(Emp)

admin.site.register(SalGrade)