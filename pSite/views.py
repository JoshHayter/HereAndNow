from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Stock
import stripe

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

testStock1 = Stock(title = "Landscape 1", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 49.99, quantity = 1, image = "1")

testStock2 = Stock(title = "Landscape 2", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 89.99, quantity = 1, image = "2")

testStock3 = Stock(title = "Landscape 3", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 200.00, quantity = 1, image = "3")

testStock4 = Stock(title = "Landscape 4", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 150.00, quantity = 1, image = "4")

testStock5 = Stock(title = "Landscape 5", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 75.00, quantity = 1, image = "5")

testStock6 = Stock(title = "Landscape 6", artist = "John Doe",
                    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    price = 80.00, quantity = 1, image = "6")

stockList = []
stockList.append(testStock1)
stockList.append(testStock2)
stockList.append(testStock3)
stockList.append(testStock4)
stockList.append(testStock5)
stockList.append(testStock6)


def index(request):


    context = {
        'active' : 0,
        'stockList' : stockList
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
