from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from prayTimes.serializers import PrayTimeTableSerializer
from prayTimes.models import PrayTimeTable
from django.http import JsonResponse


# def get_all_pray(request):
#     timeTales = PrayTimeTable.objects.all()
#     data = {
#         'pray_schedules': list(timeTales.values())
#     }
#     return JsonResponse(data)
#
#
# def get_pray(request, pk):
#     timeTable = PrayTimeTable.objects.get(pk=pk)
#     data = {
#         'month': timeTable.monthNum,
#     }
#     return JsonResponse(data)


@api_view(['GET', 'POST'])
def get_all_pray_times(request):
    if request.method == 'GET':
        time_tales = PrayTimeTable.objects.all()
        serialiser = PrayTimeTableSerializer(time_tales, many=True)
        return Response(serialiser.data)
    elif request.method == 'POST':
        time = PrayTimeTableSerializer(data=request.data)
        if time.is_valid():
            time.save()
            return Response(time.data, status=status.HTTP_201_CREATED)
        else:
            return Response(time.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def get_specific_pray(request, pk):
    if request.method == 'GET':
        tim_table = PrayTimeTable.objects.get(pk=pk)
        ser = PrayTimeTableSerializer(tim_table)
        return Response(ser.data)
    elif request.method == 'PUT':
        data = request.data
        tim_table = PrayTimeTable.objects.get(pk=pk)
        ser = PrayTimeTableSerializer(tim_table, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
    elif request.method == 'DELETE':
        PrayTimeTable.objects.get(pk=pk).delete()
        return Response({'message': 'Item was successfully deleted!'}, status=status.HTTP_204_NO_CONTENT)
