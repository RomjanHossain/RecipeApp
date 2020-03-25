from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserModel(BaseUserManager):
    """ Creates and saves a new user """
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Enter an Email , dumb!")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Customer model using email instead of username """
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserModel()

    USERNAME_FIELD = 'email'

