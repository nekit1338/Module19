from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    age = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Game(models.Model):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

#  """Список использованных команд в shell"""
#
#  "Добавление покупателей в таблицу Buyer"
#
#  first_buyer = Buyer.objects.create(name="Ilya", balance=1500.05, age=24)
#  second_buyer = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
#  third_buyer = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)
#
#  "Добавление игр в таблицу Game"
#
#  first_game = Game.objects.create(title="Cyberpunk 2077", cost=31, size=46.2, description="Game of the year",
#                                   age_limited=True)
#  second_game = Game.objects.create(title="Mario", cost=5, size=0.5, description="Old Game", age_limited=False)
#  third_game = Game.objects.create(title="Hitman", cost=12, size=36.6, description="Who kills Mark?", age_limited=True)
#
#  "Связывание Buyer и Game"
#
#  first_buyer.games.set([first_game, second_game, third_game])  # У первого покупателя есть все игры
#
#  second_game.buyers.add(second_buyer)  # У второго 2 игры
#  third_game.buyers.add(second_buyer)
#
#  third_buyer.games.add(second_game)  # Третий покупатель (младше 18) имеет только одну игру "Mario"
