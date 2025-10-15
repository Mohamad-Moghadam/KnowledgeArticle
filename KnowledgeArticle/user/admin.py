from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'groups__name']
    list_filter = ['groups__name']