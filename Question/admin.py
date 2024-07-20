from django.contrib import admin

from .models import User


# Register your models here.


@admin.register(User)
class register_user(admin.ModelAdmin):
    list_display = ['user_id', 'full_name', 'phone_number', 'score', 'received_a_certificate', 'is_calling']
    list_filter = ['score', 'is_calling', 'received_a_certificate', 'created_time']
    list_editable = ['received_a_certificate', 'is_calling']
    ordering = ['-correct_answer']
    search_fields = ['first_name', 'last_name']
