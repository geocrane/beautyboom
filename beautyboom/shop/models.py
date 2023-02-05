from django.db import models
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey(
        "self",
        related_name="child",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    tittle = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    icon = models.ImageField(upload_to="categories/icons", blank=True)

    class Meta:
        ordering = ("tittle",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.tittle


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.PositiveIntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name
