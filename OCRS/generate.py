import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','OCRS.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from mysite.models import Student,Teacher
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # create fake data
        fake_name = fakegen.name()
        student = Student.objects.get_or_create(name=fake_name)
        fake_name = fakegen.name()
        teacher = Teacher.objects.get_or_create(teacher_name=fake_name)


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
