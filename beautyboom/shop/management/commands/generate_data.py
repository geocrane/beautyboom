import random, string
from django.core.management.base import BaseCommand

from shop.models import Category, Product


class Command(BaseCommand):
    help = "Сгенерировать базу данных магазина"

    def handle(self, *args, **options):
        def randomword(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))

        print("Генерация данных:")
        model = Category
        CATEGORIES = dict(
            nail="Ногтевой сервис",
            disposable="Одноразовый расходник",
            eyes="Брови и ресницы",
            equipment="Оборудование",
            depilation="Депиляция",
            disinfection="Дезинфекция"
        )
        print(f"Генерирую {model.__name__}")
        for slug, tittle in CATEGORIES.items():
            model.objects.create(tittle=tittle, slug=slug)

        print("Генерирую подкатегории")
        i = 0
        while i < 50:
            tittle = randomword(10)
            parent = Category.objects.order_by('?').first()
            if parent.slug in CATEGORIES:
                model.objects.create(tittle=tittle, slug=tittle, parent=parent)
                i += 1

        model = Product
        print(f"Генерирую {model.__name__}")
        i = 0
        while i < 500:
            name = randomword(7)
            category = Category.objects.order_by('?').first()
            price = random.randint(100, 1000)
            stock = random.randint(1, 100)
            if category.slug not in CATEGORIES:
                model.objects.create(category=category, name=name, slug=name, price=price, stock=stock)
                i += 1
