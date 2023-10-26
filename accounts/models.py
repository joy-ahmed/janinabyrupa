from datetime import timezone
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager
from .utils import avatar_upload_path

class CustomUser(AbstractUser, PermissionsMixin):
    username = False
    first_name = False
    last_name = False

    type = (
        (1, 'superAdmin'),
        (2, 'admin'),
        (3, 'vendorAdmin'),
        (4, 'vendorStaff'),
        (5, 'user'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)
    user_type = models.CharField(choices=type, default=5, max_length=2)


    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    objects = CustomUserManager()