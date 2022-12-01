from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import CreateView
from audit.forms import SignUpForm


# Create your views here.
@login_required
def index(request):
    return render(request, "audit/index.html")


def signup(request):
    return render(request, "audit/signup.html")


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("audit")
    template_name = "registration/signup.html"
