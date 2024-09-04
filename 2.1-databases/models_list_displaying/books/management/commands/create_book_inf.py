import json
from django.core.management.base import BaseCommand

from books.models import Book

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as f:
            lt = json.load(f)
            for l in lt:
                book = Book(id=l.get('pk'), **l.get('fields'))
                book.save()