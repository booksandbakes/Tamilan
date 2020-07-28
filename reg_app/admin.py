from django.contrib import admin

# Register your models here.
from .models import publish,Userdata,image,TopUser

admin.site.register(publish)
admin.site.register(Userdata)
admin.site.register(image)
admin.site.register(TopUser)