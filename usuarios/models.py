from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, tipo='dojo', **extra_fields):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(username=username, tipo=tipo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self.create_user(username, password, tipo='general', is_superuser=True, is_staff=True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPOS = (
        ('general', 'Admin General'),
        ('dojo', 'Admin Dojo'),
    )
    username = models.CharField(max_length=150, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default='dojo')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.tipo})"
