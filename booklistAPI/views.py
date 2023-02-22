from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Book


@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        book_list = {
            'books': [
                'As the crow flies',
                'Northanger Abbey'
            ]
        }
        return JsonResponse(book_list)

    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            author = request.POST.get('author')
            price = request.POST.get('price')

            book = Book.objects.all(title=title, author=author, price=price)

            try:
                book.save()

            except IntegrityError :
                return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(book_list(books), status=201)