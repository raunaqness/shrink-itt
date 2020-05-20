from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

from .models import URLs

import urllib
import hashlib

# Create your views here.
def home(request):
    return render(request, template_name = 'home.html')

def shrink_url(request):
    complete_url = request.GET["long_url"]
    hash_object = hashlib.md5(complete_url.encode())
    shrinked_url = hash_object.hexdigest()[:8]

    try:
        check = URLs.objects.get(shrinked_url=shrinked_url)
    except URLs.DoesNotExist:
        entry = URLs(shrinked_url=shrinked_url, complete_url=complete_url)
        entry.save()


    print("new shrinked_url : {}".format(shrinked_url))

    return render(request, 'home.html', {
        'shrinked_url': shrinked_url
    })

def get_long_url(request, shrinked_url):
    print("Shrinked url : {}".format(shrinked_url))

    target = get_object_or_404(URLs, shrinked_url=shrinked_url)
    final_url = target.complete_url

    if (final_url[:4] != 'http'):
        final_url = 'http://' + final_url

    return redirect(final_url)