from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # id列，会自动创建，自增，主键
    username=models.CharField(max_length=32)
    pwd=models.CharField(max_length=64)