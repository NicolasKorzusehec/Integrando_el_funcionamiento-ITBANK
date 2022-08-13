# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from Clientes.models import Cliente

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    number_card = models.CharField(unique=True, max_length=200)
    cvv = models.IntegerField()
    issue_date = models.TextField()
    exp_date = models.TextField()
    type_card = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    brand = models.ForeignKey('MarcaTarjeta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class MarcaTarjeta(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'
