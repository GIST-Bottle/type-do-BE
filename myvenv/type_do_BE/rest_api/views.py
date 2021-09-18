from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo, Inprogress, Done
from .serializers import TodoSerializer, InprogressSerializer, DoneSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        query_set = Todo.objects.all()
        serializer = TodoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_id(request, pk):
    obj = Todo.objects.filter(pk=pk)
    # Todo.objects.get(pk=pk) makes "Todo object is not interable" error
    if request.method == 'GET':
        serializer = TodoSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
    """ 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) """
   
@csrf_exempt
def inprogress(request):
    if request.method == 'GET':
        query_set = Inprogress.objects.all()
        serializer = InprogressSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InprogressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def inprogress_id(request, pk):
    obj = Inprogress.objects.filter(pk=pk)
    if request.method == 'GET':
        serializer = InprogressSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def done(request):
    if request.method == 'GET':
        query_set = Done.objects.all()
        serializer = DoneSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DoneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def done_id(request, pk):
    obj = Done.objects.filter(pk=pk)
    if request.method == 'GET':
        serializer = DoneSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)