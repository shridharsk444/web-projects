from django.contrib import admin
from testapp.models import BangloreJobs,HydrabadJobs,ChennaiJobs,PuneJobs

# Register your models here.
#class loginmodeladmin(admin.ModelAdmin):
 #   list_display=['username','password']

class BangloreJobsadmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email']

class HydrabadJobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email']


class ChennaiJobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email']

class PuneJobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email']

#admin.site.register(loginmodel,loginmodeladmin)
admin.site.register(BangloreJobs, BangloreJobsadmin)
admin.site.register(HydrabadJobs,HydrabadJobsadmin)
admin.site.register(ChennaiJobs,ChennaiJobsadmin)
admin.site.register(PuneJobs,PuneJobsadmin)
