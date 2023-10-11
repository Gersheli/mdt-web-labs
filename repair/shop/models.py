from django.db import models
from typing import List
from django.urls import reverse

from login.models import CustomUser


class Author(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter author name')

    def get_absolute_url(self):
        return reverse('shop:author-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter genre name')

    def get_absolute_url(self):
        return reverse('shop:usluga_list_by_genre', args=[str(self.name)])

    def __str__(self):
        return self.name


class Usluga(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Enter usluga title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=200,
                                   help_text='Enter usluga description', default='unknown')

    image = models.ImageField(upload_to='usluga/%Y/%m/%d', blank=True)
    quantity = models.IntegerField()
    purchase_count = models.PositiveIntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    LOAN_STATUS = (
        ('A', 'available'),
        ('U', 'unavailable')
    )
    status = models.CharField(max_length=1,
                              choices=LOAN_STATUS,
                              help_text="units of product")

    def get_absolute_url(self):
        return reverse('shop:usluga_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Client(models.Model):
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    short_description = models.TextField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="static/images/posts/")

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
