# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    customer_type = models.ForeignKey('TipoCliente', models.DO_NOTHING, blank=True, null=True)
    customer_address = models.ForeignKey('Direccion', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-customer_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.customer_name + " with DNI = " + self.customer_dni



class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.TextField()
    number = models.IntegerField()
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ["-address_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.address_id

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.ForeignKey("Sucursal", models.DO_NOTHING, blank=True, null=True)
    employee_address = models.ForeignKey(Direccion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-employee_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.employee_name + " with DNI = " + self.employee_dni

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address = models.ForeignKey(Direccion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ["-branch_id"]

    def __str__(self): 
        return self.branch_name + " with id = " + str(self.branch_id)

class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type_name = models.TextField(unique=True)
    debit_card = models.TextField()
    credit_card = models.TextField()
    current_account = models.TextField()
    checkbook_amount = models.IntegerField()
    box_dollar = models.TextField(blank=True, null=True)
    box_peso = models.TextField(blank=True, null=True)
    withdraw_daily_max = models.IntegerField(blank=True, null=True)
    transfer_comission = models.IntegerField(blank=True, null=True)
    max_travel_reception = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'
        verbose_name = "Tipo de cliente"
        verbose_name_plural = "Tipos de clientes"
        ordering = ["-customer_type_id"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.type_name
