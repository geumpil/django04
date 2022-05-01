from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.

def index(req):
    return render(req, "acc/index.html")

def login_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req, u)
            return redirect("acc:index")
        else:
            messages.error(req, "계정정보가 일치하지 않습니다.")

    return render(req, "acc/login.html")

def logout_user(req):
    logout(req)
    return redirect("acc:login")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucom")
        try:
            User.objects.create_user(username=un, password=up, age=ua, pic=pi, comment=uc)
            return redirect("acc:login")
        except:
            messages.error(req, "USERNAME이 중복되어 생성되지 않았습니다.") 
    return render(req, "acc/signup.html")

def profile(req):
    return render(req, "acc/profile.html") 

def update(req):
    if req.method == "POST":
        u = req.user
        ue = req.POST.get("uemail")
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucom")
        if up:
            u.set_password(up)
        u.email = ue
        u.age = ua
        if pi:
            u.pic.delete()
            u.pic = pi
        u.comment = uc
        u.save()
        login(req, u)
    return render(req, "acc/update.html")   

def delete(req):
    pwck = req.POST.get("pwck")
    if check_password(pwck, req.user.password):
        req.user.pic.delete()
        req.user.delete()
        return redirect("acc:index")
    else:
        messages.info(req, "계정정보가 일치하지 않아 삭제되지 않았습니다.")
        return redirect("acc:profile")