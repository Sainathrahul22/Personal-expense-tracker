from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'amount', 'category', 'date')
    list_filter = ('category', 'date', 'user')
