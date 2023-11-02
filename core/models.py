"""Core models for user"""

from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from core.choices import UserKind, UserStatus, UserGender
from common.models import BaseModelWithUID


class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have a email")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.kind = UserKind.SUPER_ADMIN
        user.status = UserStatus.ACTIVE
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModelWithUID):
    """Users in the System"""

    username = models.CharField(max_length=20, unique=True, db_index=True)
    phone_number = models.CharField(
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
    is_staff = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=UserKind.choices,
        default=UserKind.UNDEFINED,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"
