from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# Create your models here.

from Clientes.models import Cliente



class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, clave=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            clave = clave,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, clave=None):
        user = self.create_user(
            username,
            email,
            password,
            clave
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return 



class Usuario(AbstractUser, PermissionsMixin):
    username = models.CharField(verbose_name="Nombre de usuario", max_length=200, unique=True)
    first_name = models.CharField(verbose_name="Nombre", max_length=25)
    last_name = models.CharField(verbose_name="Apellido", max_length=25)
    password = models.CharField(verbose_name="Contraseña", max_length=200)
    clave = models.CharField(verbose_name = "Clave", max_length=4)
    telefono = models.IntegerField(verbose_name = "Telefono", blank=True, null=True) ##Se debera mejorar la especificidad posteriormente, quizas desde el form de creacion de clientes.
    customer = models.OneToOneField(Cliente, verbose_name = "Cliente", on_delete=models.CASCADE, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    
    objects = MyUserManager()
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




    # Ver ejemplo extendido: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#auth-custom-user
    
