import uuid

from django.db import models


class Restaurant(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name="name", max_length=100)
    address = models.CharField(verbose_name="address", max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return f'{self.name} ({self.address})'


class Menu(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    date = models.DateField(verbose_name="date", auto_now_add=True)
    image = models.FileField(verbose_name='image', upload_to="media/files/%Y/%m/%d/", )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, related_name='menus', blank=True,
                                   verbose_name='restaurant')

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f'{self.restaurant.name} menu for the {self.date}'


class Vote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name="user", related_name='votes')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant")
    date = models.DateField(verbose_name="Date", auto_now_add=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f'{self.restaurant.name}'
