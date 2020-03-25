from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserModel(BaseUserManager):
    """ Creates and saves a new user """
    
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Customer model using email instead of username """
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserModel()

    USERNAME_FIELD = 'email'

