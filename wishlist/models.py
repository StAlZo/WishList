from django.db import models
from django.urls import reverse
from DreamBoard.DreamBoard import settings
# Create your models here.


class Status(models.Model):
    """выносная модель статуса пользователя"""
    status = models.CharField(max_length=100, verbose_name="статус")

    def __str__(self):
        return ""

    def get_absolute_url(self):
        return reverse("Status")

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"


class CountPeople(models.Model):
    """модель настройки колво людей для прем акка"""
    count_people = models.IntegerField(verbose_name='кол-во людей')

    def __str__(self):
        return "porebyx"

    class Meta:
        verbose_name = "настройка кол-ва людей"
        verbose_name_plural = "настройки кол-ва людей"


class Giver(models.Model):
    """модель дарителя"""
    list_wish_id = models.ForeignKey("WishList", on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "popa"

    class Meta:
        verbose_name = "даритель"
        verbose_name_plural = "дарители"


class Booking(models.Model):
    """модель бронирования"""
    goods_list_wish_id = models.ForeignKey("GoodsInWishList", on_delete=models.CASCADE)
    giver_id = models.ForeignKey(Giver, on_delete=models.CASCADE)

    def __str__(self):
        return "jepa"

    class Meta:
        verbose_name = "бронь"
        verbose_name_plural = "бронирование"


class GoodsInWishList(models.Model):
    """ модель товары в списке желаний"""
    list_wish_id = models.ForeignKey("WishList", on_delete=models.CASCADE)
    goods_id = models.ForeignKey("Goods", on_delete=models.CASCADE)

    def __str__(self):
        return "aaaaa ya ystal"

    class Meta:
        verbose_name = "помолчу"
        verbose_name_plural = "помолчим"


class Goods(models.Model):
    """модель товаров"""
    title = models.CharField(max_length=250, verbose_name='Название')
    link = models.TextField()

    def __str__(self):
        return "tovar"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class WishList(models.Model):
    """модель вишлиста"""
    title = models.CharField(max_length=250, verbose_name='Название')
    count_user = models.IntegerField(verbose_name='кол-во людей в списке пользователей')
    owner_user_id =models.ForeignKey(settings.AUTH_USER_MODEL)