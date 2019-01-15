import uuid
from django.db import models


class RandomUserManager(models.Manager):
    def create_user_code(self):
        code = uuid.uuid4()
        if super().get_queryset().filter(code=code).exists():
            return self.create_user_code()
        return code

    def save_data(self, data):
        for obj in data:
            obj.code = self.create_user_code()
        RandomUser.objects_randomuser.bulk_create(data)


class RandomUser(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=25)
    age = models.IntegerField()
    code = models.CharField(max_length=70)
    objects_randomuser = RandomUserManager()

    class Meta:
        db_table = 'randomuser'

    def __str__(self):
        return self.name + ' ' + self.last_name