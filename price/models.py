from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Cena')
    pc_description = models.CharField(max_length=200, verbose_name='Opis')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Ceny'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Usługa')
    pt_old_price = models.CharField(max_length=200, verbose_name='Stara cena')
    pt_new_price = models.CharField(max_length=200, verbose_name='Nowa cena')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'usługę'
        verbose_name_plural = 'Usługi'