from django.db import models
# Create your models here.
class User(models.Model):
    user_id = models.CharField(db_column="user_id",max_length=255, help_text="",primary_key=True)
    name = models.CharField(db_column="name", max_length=255, help_text="")
    tz = models.CharField(db_column="tz", max_length=255, help_text="")
    class Meta:
        managed = False
        db_table = 'user'


class UserActivity(models.Model):
    user_id = models.ForeignKey(User,db_column="user_id",on_delete=models.CASCADE)
    start_time = models.CharField(db_column="start_time", max_length=255, help_text="")
    end_time = models.CharField(db_column="end_time", max_length=255, help_text="")
    class Meta:
        managed = False
        db_table = 'user_activity'