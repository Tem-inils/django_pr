from django.db import models


class User(models.Model):
    tg_id = models.IntegerField()
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    birthday = models.DateField()
    location = models.CharField(max_length=255)
    language = models.CharField(max_length=50)

    class Meta:
        managed = False

class Product(models.Model):
    pr_category = models.CharField(max_length=255)
    pr_name = models.CharField(max_length=255)
    pr_price = models.FloatField()
    pr_quantity = models.IntegerField()
    pr_des = models.TextField()
    pr_photo = models.TextField()

    class Meta:
        managed = False


class UserCart(models.Model):
    user_id = models.IntegerField()
    user_product = models.TextField()
    quantity = models.IntegerField()
    total_for_price = models.FloatField()

    class Meta:
        managed = False


class Restaurant(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    description = models.TextField()
    number = models.CharField(max_length=20)

    class Meta:
        managed = False
