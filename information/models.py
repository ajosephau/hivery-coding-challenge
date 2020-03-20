from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    name = models.CharField(max_length=200)
    FRUIT = 'frt'
    VEGETABLE = 'veg'
    TYPE_CHOICES = [
        (FRUIT, 'Fruit'),
        (VEGETABLE, 'Vegetable'),
    ]
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=FRUIT,
    )

class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NOT_SPECIFIED = 'N'
    TYPE_GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_SPECIFIED, 'Other/Not specified'),
    ]
    id = models.CharField(max_length=24)
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    guid = models.UUIDField()
    has_died = models.BooleanField(default=False)
    balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    picture = models.URLField()
    age = models.IntegerField()
    eye_colour = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=TYPE_GENDER,
        default=NOT_SPECIFIED,
    )
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.TextField()
    about = models.TextField()
    greeting = models.TextField()
    registered = models.DateTimeField()

    # relationships
    favourite_food = models.ManyToManyField(Food)
    tags = models.ManyToManyField(Tag)
    friends = models.ManyToManyField("Person", related_name="friends_of")
