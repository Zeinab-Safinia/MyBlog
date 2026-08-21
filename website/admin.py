from django.contrib import admin
from website.models import Contact
# Register your models here.




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','subject','created_date')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    ordering = ['created_date']
    search_fields = ['name']
    list_filter = ('email',)
    
admin.site.register(Contact,ContactAdmin)