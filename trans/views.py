from django.shortcuts import render
from googletrans import Translator
import googletrans

# Create your views here.
def index(req):

    context = {
        "nd" : googletrans.LANGUAGES
    }
    if req.method == "POST":
        b = req.POST.get("bf")
        f = req.POST.get("fr")
        t = req.POST.get("to")

        tr = Translator()
        a = tr.translate(b, src=f, dest=t)
        context = {
            "af" : a.text,
            "bf" : b,
            "fr" : f,
            "to" : t
        }
    return render(req, "trans/index.html", context)