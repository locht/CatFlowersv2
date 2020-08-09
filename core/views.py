from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from datetime import datetime
from .forms import *
from .models import *

import random
import string
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# class HomeView(ListView):
#     # model = Item
#     # tao so luong san pham trong 1 page (10 sp moi qua page moi)
#     # paginate_by = 4
#     template_name = "home.html"


def Home(request):
    return render(request, "home.html")
