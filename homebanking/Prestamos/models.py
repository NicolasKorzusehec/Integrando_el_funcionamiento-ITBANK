# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from Clientes.models import Cliente

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.ForeignKey("TipoPrestamo", on_delete=models.CASCADE, blank=True, null=True)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    loan_preapproval = models.IntegerField(null=True,blank=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE,  blank=True, null=True)

    class Meta:
        db_table = 'prestamo'
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos" 
        ordering = ["-loan_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return str(self.loan_id)


class TipoPrestamo(models.Model):
    type_id = models.AutoField (primary_key=True) 
    loan_name = models.TextField()

    class Meta:
        db_table = 'tipo_prestamo'
        verbose_name = "Tipo de prestamo"
        verbose_name_plural = "Tipo de prestamos"
        ordering = ["-type_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.loan_name



