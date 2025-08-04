from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from common.mixins import TimeStampMixin

User = get_user_model()


class Cart(TimeStampMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart for {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(TimeStampMixin, models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # Generic foreign key to any product (motorcycle, part, accessory, clothing)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('cart', 'content_type', 'object_id')

    def __str__(self):
        return f"{self.quantity}x {self.product}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
