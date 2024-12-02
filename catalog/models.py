from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Наименование",
        help_text="Введите название продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена",
        help_text="Введите цену",
        blank=True,
        null=True,
    )

    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Имя продукта"
        verbose_name_plural = "Имена продуктов"
        ordering = ["name"]

    def __str__(self):
        return self.name
