from django.shortcuts import render_to_response
from django.contrib.auth.models import User
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def form_send_message(request):
    data = User.objects.all().exclude(is_superuser=True)
    return render_to_response('message/form_send_message.html',{'user':request.user,'data':data})


def form_full_view(request):
    data = None
    try:
        data = User.objects.get(pk=request.user.pk).message_set.all().order_by('-time')
        paginator = Paginator(data,15)
        page = request.GET.get('page')
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    print contacts
    return render_to_response('message/form_full_message.html',{'user':request.user,'data':contacts})

