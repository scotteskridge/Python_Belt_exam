from django.shortcuts import render, HttpResponse, redirect
from .. login.models import User

# Create your views here.


def index(request):
    if not "user_id" in request.session:
        messages.error(request, "Must be logged in to continue")
        return redirect("login:index")
    #pass over my user to make it accessable in my template
    user = User.objects.get(id = request.session["user_id"])
    context = {
        "user" : user,
    }

    return render(request, "main/index.html", context)

def next_page(request):
    if not "user_id" in request.session:
        messages.error(request, "Must be logged in to continue")
        return redirect("login:index")
    #pass over my user to make it accessable in my template
    user = User.objects.get(id = request.session["user_id"])
    context = {
        "user" : user,
    }

    return render(request, "main/next_page.html", context)
