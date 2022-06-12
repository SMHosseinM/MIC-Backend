from django.shortcuts import render

from prayTimes.models import PrayTimeTable
from django.http import JsonResponse


def get_all_pray(request):
    timeTales = PrayTimeTable.objects.all()
    data = {
        'pray_schedules': list(timeTales.values())
    }
    return JsonResponse(data)


def get_pray(request, pk):
    timeTable = PrayTimeTable.objects.get(pk=pk)
    data = {
        'month': timeTable.monthNum,
    }
    return JsonResponse(data)
