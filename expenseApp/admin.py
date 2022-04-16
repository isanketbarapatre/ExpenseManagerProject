from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = admin.site.site_title = "Expenses Manager"

admin.site.register(Master)
admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(Saving)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)