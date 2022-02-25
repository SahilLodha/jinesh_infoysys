from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View


# Create your views here.
# class HomeView(LoginRequiredMixin, View):
#     def get(self, request):
#         return HttpResponse("This will be the Home Page.")
@login_required
def HomeView(request):
    if request.method=='GET':
        return HttpResponse('test')