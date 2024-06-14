import asyncio

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from plugs.PlugController import PlugController


def index(request):
    try:
        bc = PlugController()
        consumption = asyncio.run(bc.plug_current_consumption())
        return render(request, 'plugs/index.html', {'consumption': consumption})
    except Exception as e:
        return render(request, 'plugs/index.html', {'message': 'Bulbs not responding', 'color': 'red'})


def controls(request):
    return render(request, 'plugs/index.html')


def general_info(request):
    try:
        bc = PlugController()
        general_info = asyncio.run(bc.general_info())
        return JsonResponse({'general_info': general_info})
    except Exception as e:
        return JsonResponse({'error': 'Plug not responding', 'details': str(e)}, status=500)


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


def emeter_monthly(request):
    try:
        bc = PlugController()
        emeter_monthly = asyncio.run(bc.plug_emeter_monthly())
        return JsonResponse({'emeter_monthly': emeter_monthly})
    except Exception as e:
        return JsonResponse({'error': 'Bulbs not responding', 'details': str(e)}, status=500)
