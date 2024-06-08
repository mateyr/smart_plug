from django.shortcuts import render
from plugs.PlugController import PlugController
import asyncio


# Create your views here.

from django.http import HttpResponse


def index(request):
    try:
        bc = PlugController()
        consumption = asyncio.run(bc.plug_current_consumption())
        return render(request, 'plugs/index.html', {'consumption': consumption})
    except Exception as e:
        return render(request, 'plugs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})


def controls(request):
    return render(request, 'plugs/index.html')


def off(request):
    try:
        bc = PlugController()
        asyncio.run(bc.plug_off())
        return render(request, 'plugs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'plugs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})


def on(request):
    try:
        bc = PlugController()
        asyncio.run(bc.plug_on())
        return render(request, 'plugs/index.html', {'message': 'Success', 'color': 'green'})
    except Exception as e:
        return render(request, 'plugs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})


