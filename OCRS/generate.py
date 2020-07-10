import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','OCRS.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from mysite.models import Student,Teacher
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # create fake data
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        uname = first_name[0] + last_name
        pass_gen = User.objects.make_random_password()
        print(pass_gen)
        newUser = User.objects.create(username=uname.lower(),first_name=first_name,last_name=last_name)
        newUser.set_password(pass_gen)
        newUser.save()
        print("CREATED USER")
        student = Student.objects.create(name="{} {}".format(first_name,last_name),user=newUser)
        print("CREATED STUDENT")

        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        uname = first_name[0]+ last_name
        pass_gen = User.objects.make_random_password()
        print(pass_gen)
        newUser = User.objects.create(username=uname.lower(),first_name=first_name,last_name=last_name)
        newUser.set_password(pass_gen)
        newUser.save()
        print("CREATED USER")
        teacher = Student.objects.create(name="{} {}".format(first_name,last_name),user=newUser)
        print("CREATED STUDENT")



if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
