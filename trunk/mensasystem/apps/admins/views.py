from django.shortcuts import render_to_response,render,HttpResponseRedirect,Http404,HttpResponse,RequestContext,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.db import models
# Create your views here.
from ..mensa_app.forms import UserForm,UserProfileForm
from django.template import Template,loader, Context
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required,permission_required
from ..mensa_app.models import *
from django.core.paginator import Paginator
from dateutil import parser
import smtplib
from django.db import load_backend
import mensa.settings


def auth(request):
    from django.contrib.auth.models import User,Permission,Group

    return render_to_response('admin/auth/auth.html',{'request':request,'app_list':[User,Permission,Group]})