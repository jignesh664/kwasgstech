from django.contrib import admin

admin.site.site_header = 'KWARGS Technology'
admin.site.site_title  =  "KWARGS Technology"
admin.site.index_title  =  "KWARGS Technology"

# Register your models here.
from .models import Contact,Received_Resume,Post,Job_Description,Responsibilites,Qualifications,Skill

# admin.site.register(Contact)
admin.site.register(Received_Resume)
admin.site.register(Post)
admin.site.register(Job_Description)
admin.site.register(Responsibilites)
admin.site.register(Qualifications)
admin.site.register(Skill)

