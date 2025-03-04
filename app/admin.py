from django.contrib import admin
from .models import Employee

# Employeeモデルを管理画面に登録（emplnmも表示）
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emplid', 'emplnm')