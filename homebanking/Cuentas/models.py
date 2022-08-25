# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from Clientes.models import Cliente

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey("TipoCuenta", on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True) 

    class Meta:
        db_table = 'cuenta'
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
        ordering = ["-account_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        #return str(self.account_id)
        return self.customer.customer_name + " de tipo: " + self.account_type.account_name 


class TipoCuenta(models.Model):
    type_id = models.AutoField (primary_key=True) 
    account_name = models.TextField()

    class Meta:
        db_table = 'tipo_cuenta'
        verbose_name = "Tipo de cuenta"
        verbose_name_plural = "Tipo de cuentas"
        ordering = ["-type_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.account_name


class Movimientos(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Cuenta, on_delete=models.CASCADE, blank=True, null=True)
    operation_type = models.TextField()
    amount = models.IntegerField()
    changed_at = models.TextField()

    class Meta:
        db_table = 'movimientos'

        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        ordering = ["-transaction_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.account + " de tipo: " + self.operation_type
