
from django.http import HttpResponse
from django.shortcuts import render
import faker
from faker import Faker
from myapp.models import *
# Create your views here.
def index(request):
    i = 0;
    while i < 50:
        fk = Faker()
        st =student()
        st.stu_name = fk.name()
        st.department = "Biology"
        st.stu_roll = i
        st.save()
        i=i+1
        print(i)
    return HttpResponse("asfdgadfh")

    