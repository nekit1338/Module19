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


class Product_list(models.Model):
    name = models.CharField(max_length=255,
                            null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    description = models.TextField(null=True,
                                   blank=True)

    class Meta:
        db_table = 'products_list'

    def __str__(self):
        return self.name


class Users_of_shop(models.Model):
    username = models.CharField(max_length=50,
                                unique=True,
                                null=False)
    email = models.CharField(max_length=100,
                             null=True,
                             blank=True)
    registration_date = models.DateField(null=True,
                                         blank=True)

    class Meta:
        db_table = 'users_of_shop'

    def __str__(self):
        return self.username


"""Список использованных команд в shell к домашнему заданию по теме "QuerySet запросы в базу данных"""
#
#  "Добавление покупателей в таблицу Buyer"
#
#  first_buyer = Buyer.objects.create(name="Ilya", balance=1500.05, age=24)
#  second_buyer = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
#  third_buyer = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)
#
#  "Добавление игр в таблицу Game"
#
#  first_game = Game.objects.create(title="Cyberpunk 2077", cost=31, size=46.2, description="Game of the year", age_limited=True)
#  second_game = Game.objects.create(title="Mario", cost=5, size=0.5, description="Old Game", age_limited=False)
#  third_game = Game.objects.create(title="Hitman", cost=12, size=36.6, description="Who kills Mark?", age_limited=True)
#
#  "Связывание Buyer и Game"
#
#  first_buyer.games.set([first_game, second_game, third_game])  # У первого покупателя есть все игры
#
#  second_game.buyer.add(second_buyer)  # У второго 2 игры
#  third_game.buyer.add(second_buyer)
#
#  third_buyer.games.add(second_game)  # Третий покупатель (младше 18) имеет только одну игру "Mario"


"""Список использованных команд в shell к домашнему заданию по теме "Настраиваем СУБД postgre в django"""
#
# 1) Запросы на создание и удаление объектов
#
# "Добавление продуктов в таблицу Product_list"
#
# new_product = Product_list(name="Первый продукт", price=100, description="Описание первого продукта")
# new_product.save()
#
# new_product = Product_list(name="Второй продукт", price=200, description="Описание второго продукта")
# new_product.save()
#
# new_product = Product_list(name="Третий продукт", price=300, description="Описание третьего продукта")
# new_product.save()
#
# new_product = Product_list(name="Четвертый продукт", price=400, discount=10, description="Описание четвертый продукта")
# new_product.save()
#
# "Добавление юзеров в таблицу Users_of_shop"
#
# new_user = Users_of_shop(username="Andrei", email="andrei@example.com", registration_date=date(2024,1,15))
# new_user.save()
#
# new_user = Users_of_shop(username="Oleg", email="oleg@example.com", registration_date=date(2024,2,29))
# new_user.save()
#
# new_user = Users_of_shop(username="Alina", email="Alina@example.com", registration_date=date(2024,3,11))
# new_user.save()
#
# "Удаление объектов из таблиц"
#
# product_to_delete = Product_list.objects.get(id=2)
# product_to_delete.delete()
#
# user_to_delete = Users_of_shop.objects.get(username="Oleg")
# user_to_delete.delete()
#
#
# 2) "Запросы на получение всех (и отдельно по id) продуктов, юзеров из таблиц"
#
# all_products = Product_list.objects.all()
# print(all_products)
#
# product_id_4 = Product_list.objects.get(id=4)
# print(product_id_3)
#
# all_users = Users_of_shop.objects.all()
# print(all_users)
#
# user_id_1 = Users_of_shop.objects.get(id=1)
# print(user_id_1)
#
# 3) Запросы на фильтрацию
#
# expensive_products = Product_list.objects.filter(price__gt=100)
# print(expensive_products)
#
# users_after_date = Users_of_shop.objects.filter(registration_date__gt=date(2024, 1, 29))
# print(users_after_date)
#
# discount_products = Product_list.objects.filter(price__gt=50, discount__lt=5)
# print(discount_products)
#
# 4) Запрос на подсчет количества объектов (len())
#
# product_count = Product_list.objects.count()
# print(f"Количество продуктов: {product_count}")
#
# user_count = Users_of_shop.objects.count()
# print(f"Количество пользователей: {user_count}")
#
# expensive_product_count = Product_list.objects.filter(price__gt=200).count()
# print(f"Количество дорогих продуктов: {expensive_product_count}")
#
# users_after_date_count = Users_of_shop.objects.filter(registration_date__gt=date(2024, 1, 29)).count()
# print(f"Количество пользователей, зарегистрированных после 29.1.2024: {users_after_date_count}")
