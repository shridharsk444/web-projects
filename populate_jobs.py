import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','secondproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumber():
    d1=randint(7,9)
    num="" + str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('manager','teamlead','software_engineer'))
        feligibility=fake.random_element(elements=('mtec','b.e','mca','bca'))
        faddress=fake.address()
        femail=fake.email()
        #fphonenumber=phonenumber()
        BLR_jobs=BangloreJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,
                                                address=faddress,email=femail)#phonenumber=phonenumber)
populate(30)
