#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Document,CustomerData
# Register your models here.
#admin.site.register(Document)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author','description','document','uploaded_at')

admin.site.register(Document,PostAdmin)
admin.site.register(CustomerData)