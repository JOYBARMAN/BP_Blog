"""Core models for user"""

from django.db import models
from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
)

from core.choices import UserType
from common.models import BaseModelWithUID


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, phone, user_type, password=None):
        """
        Creates and saves a User with the given email, username ,password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), username=username, phone=phone, user_type=user_type)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email,username and password.
        """
        user = self.create_user(email, password=password, username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModelWithUID):
    """Users model in the System"""

    username = models.CharField(max_length=20, unique=True, db_index=True)
    phone = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.UNDEFINED,
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
