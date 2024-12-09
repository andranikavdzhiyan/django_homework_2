from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name="Car", description="Germany")

        product = [
            {"name": "BMW", "price": "500000", "category": category},
            {"name": "Mersedes", "description": "555000", "category": category},
        ]

        for product_price in product:
            product, created = Product.objects.get_or_create(**product_price)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exist: {product.name}")
                )
