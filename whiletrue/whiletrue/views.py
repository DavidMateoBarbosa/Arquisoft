from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def healthCheck(request):
    return HttpResponse('ok')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)
