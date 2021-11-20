from django.contrib import admin
from .models import Cliente
# Register your models here.


#class ClienteAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']

admin.site.register(Cliente)