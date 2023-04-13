from django.shortcuts import render
from rest_framework.views import APIView
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings
import os

from .models import Category, Text


class Index(APIView):

    def post(self, request):
        text_title = request.POST.get('text-title')
        text_category_id = request.POST.get('text-category')
        text_content = request.POST.get('text-content')
        text_category = Category.objects.get(id=text_category_id)
        text = Text(title=text_title, category=text_category, content=text_content, created_at=datetime.now())

        date_str = datetime.now().strftime('%Y-%m-%d')
        with open('file.txt', 'a') as f:
            f.write('info')

        text.save()
        return JsonResponse({'id': text.id, 'date': text.created_at})

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context = {"categories": categories})