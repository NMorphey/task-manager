from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class IndexView(View):

    def get(self, request):
        return HttpResponse('This is the main page!')