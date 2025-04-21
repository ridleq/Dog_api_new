from django.db import models


class Breed(models.Model):
    """
    Модель для предоставления Породы.
    """
    SIZE_CHOICES = [
        ('Tiny', 'Очень маленькая'),
        ('Small', 'Маленькая'),
        ('Medium', 'Средняя'),
        ('Large', 'Большая'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    shedding_amount = models.IntegerField(
       choices=[(i, i) for i in range(1, 6)],
       blank=False
    )
    exercise_needs = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        """Возвращает название породы как строку."""
        return self.name


class Dog(models.Model):
    """
    Модель для предоставления собаки.
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        """Возвращает имя собаки как строку."""
        return self.name
