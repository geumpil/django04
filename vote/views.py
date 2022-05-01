from django.shortcuts import redirect, render
from .models import Topic, Choice
from django.utils import timezone

# Create your views here.

def index(req):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(req, "vote/index.html", context)

def detail(req, tpk):
    print(req.POST.get("sub"))
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(req, "vote/detail.html", context)

def vote(req, tpk):
    t = Topic.objects.get(id=tpk)
    if not req.user in t.voter.all():
        t.voter.add(req.user)
        cpk = req.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.num += 1
        c.save()
    else:
        pass #메시지! 
    return redirect("vote:detail", tpk)

def create(req):
    if req.method == "POST":
        s = req.POST.get("sub")
        c = req.POST.get("con")
        m = req.POST.getlist("chname")
        if len(m) > 2:
            t = Topic(subject=s, maker=req.user, content=c, pubdate=timezone.now())
            t.save()

            for i in m:
                Choice(topic=t, name=i).save()
            return redirect("vote:index")
    return render(req, "vote/create.html")
