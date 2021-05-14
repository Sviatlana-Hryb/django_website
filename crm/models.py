from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Tytuł statusu wniosku')
    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statusy'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Imię')
    order_phone = models.CharField(max_length=200, verbose_name='Telefon')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'zamówienie'
        verbose_name_plural = 'Zamówienia'

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Wniosek')
    coment_text = models.TextField(verbose_name='Tekst komentarza')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Data utworzenia')


    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'komentarz'
        verbose_name_plural = 'Komentarzy'