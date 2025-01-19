from django.shortcuts import render # type: ignore
from django.contrib.auth.models import User
def home(req):
    return render(req,'index.html')