from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
import stripe

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def index(request):


    context = {
        'active' : 0
        }

    return render(request, 'pSite/index.html', context)

def about(request):

    context = {
    'active' : 1
        }

    return render(request, 'pSite/about.html', context)

def slideshow(request):

    context = {
    'active' : 2
        }

    return render(request, 'pSite/slideshow.html', context)

def success(request):

    context = {
        }

    return render(request, 'pSite/success.html', context)

def cancel(request):

    context = {
        }

    return render(request, 'pSite/cancel.html', context)

def charge(request, item_id):
    stripe.api_key = "sk_test_KmC6QMGCkYiLu1RijawnCnJ5"

    stripe.api_version = "2019-02-19; checkout_sessions_beta=v1"

    session = stripe.checkout.Session.create(
    success_url="http://127.0.0.1:8000/success",
    cancel_url="http://127.0.0.1:8000/cancel",
    payment_method_types=["card"],
    line_items=[
        {
        "amount": 4999,
        "quantity": 1,
        "name": "Landscape 1",
        "currency": "gbp"
        },
    ])

    context = {
        'session' : session
        }

    return render(request, 'pSite/charge.html', context)

def handler404(request, exception, template_name='pSite/error404.html'):
    response = render_to_response('pSite/error404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, exception, template_name='pSite/error500.html'):
    response = render_to_response('pSite/error500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
