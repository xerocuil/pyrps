from django.shortcuts import get_object_or_404, render, redirect

def index(request):
  return render(request, 'pyrps/index.html')
