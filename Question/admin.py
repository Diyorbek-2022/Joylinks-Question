from django.contrib import admin

from .models import User


# Register your models here.


admin.site.register(User)
# class register_user(admin.ModelAdmin):
#     list_display = ['user_id', 'full_name', 'email', 'score']
#     ordering = ['-correct_answer', '-created_time']
#     search_fields = ['first_name']
#     list_filter = ['score', 'created_time']
