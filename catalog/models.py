from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Car brand, year and complectation")
    vin = models.CharField(primary_key=True, max_length=17)
    lot_num = models.CharField(max_length=20)
    LOAN_AUCTION = (
        ('i', 'IAAI'),
        ('c', 'Copart')
    )
    auction = models.CharField(max_length=1, choices=LOAN_AUCTION, default='i')
    odometr = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100)
    highlight = models.CharField(max_length=100)
    primary_damage = models.CharField(max_length=100)
    secondary_damage = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100)
    LOAN_BODY = (
        ('s', 'Sedan'),
        ('c', 'Coupe'),
        ('b', 'Convertible'),
        ('h', 'Hatchback'),
        ('w', 'Station Wagon'),
        ('s', 'Sport-Utility Vehicle(SUV)'),
        ('p', 'Pickup Truck'),
        ('m', 'Minivan'),
    )
    body = models.CharField(max_length=1, choices=LOAN_BODY, default='g')
    engine = models.CharField(max_length=100)
    LOAN_FUEL = (
        ('g', 'Gas'),
        ('d', 'Diesel'),
        ('h', 'Hybrid'),
        ('e', 'Electrically'),
    )
    fuel = models.CharField(max_length=1, choices=LOAN_FUEL, default='g')
    LOAN_TRANSMISSION = (
        ('a', 'Automatic'),
        ('m', 'Manual')
    )
    transmission = models.CharField(max_length=1, choices=LOAN_TRANSMISSION, default='fw')

    LOAN_DRIVE = (
        ('aw', 'All-wheel Drive'),
        ('fw', 'Front-wheel Drive'),
        ('rw', 'Rear-wheel Drive'),
    )
    drive = models.CharField(max_length=2, choices=LOAN_DRIVE, default='m')
    date = models.DateField()
    LOAN_KEY = (
        (True, 'Yes'),
        (False, 'No')
    )
    keys = models.BooleanField(choices=LOAN_KEY, default='n')

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.vin)])

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='uploads/')

