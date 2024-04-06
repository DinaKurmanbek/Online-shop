from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=200, default= 'Other')
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    # TYPE = (
    #     ('F', 'food'),
    #     ('NF', 'not food')
    # )
    name = models.CharField(max_length=200)
    description = models.TextField()

    # photo = models.ImageField(upload_to = 'images/',blank=True, null = True)
    # type = models.CharField(default='NF', choices=TYPE)


    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def demo_content(self):
        return f" {self.content[:10]}...."

    def __str__(self):
        return self.name

class SavedItems(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SavedItems - {self.user.username} ({self.pk})"

class SavedItem(models.Model):
    saved_items = models.ForeignKey(SavedItems, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"

class Order(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    saved_items = models.OneToOneField(SavedItems, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - {self.user.username} ({self.pk})"



