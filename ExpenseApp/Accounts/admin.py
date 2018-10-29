from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Account, Activity, User

admin.site.register(Account)

admin.site.register(Activity)



