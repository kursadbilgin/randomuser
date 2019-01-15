from django.contrib import admin
from randomuser.models import RandomUser


class RandomUserAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'last_name')
    list_filter = ('age',)
    search_fields = ['name',]

admin.site.register(RandomUser, RandomUserAdmin)