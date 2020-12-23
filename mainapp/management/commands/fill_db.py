import os, json
from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, Contact

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        contacts = load_from_json('contact__locations')
        Contact.objects.all().delete()
        for contact in contacts:
            Contact.objects.create(**contact)

        ShopUser.objects.create_superuser('django', 'django@geekbrains.local', 'geekbrains', age = 33)