from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Category, Text

@api_view(['POST'])
def post_data(request):
    text_name = request.POST.get("text_name")
    text_category_id = request.data["text_category"]
    text_content = request.POST.get("text_content")
    text_char_count = len(text_content)
    text_category = Category.objects.get(id=text_category_id)
    text = Text(title=text_name, category=text_category, text=text_content,
                char_count=text_char_count, created_at=timezone.now())
    text.save()
    date_str = timezone.now().strftime('%Y-%m-%d')

    with open(f'app/data/{date_str}.txt', 'w') as f:
        f.write(f'Название текста: {text_name}\n')
        f.write(f'Категория: {text_category.title}\n')
        f.write(f'Текст: {text_content}\n')
        f.write(f'Количество символов: {text_char_count}\n')

    return Response({'id': text.id, 'date': text.created_at})

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context = {"categories": categories})