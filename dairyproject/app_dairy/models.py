from django.db import models

# Create your models here.
class db_DairyList(models.Model):
    id        = models.AutoField(primary_key=True)
    user_id   = models.CharField(max_length=64)       #用户id
    date      = models.DateTimeField()                #生成时间
    pickdate  = models.CharField(max_length=32)       #自定义时间
    title     = models.CharField(max_length=64)       #名称
    class Meta:
        db_table = 'DairyList'

class db_DairyContent(models.Model):
    DairyDetail = models.OneToOneField(db_DairyList,primary_key=True, on_delete=models.CASCADE)
    content   = models.CharField(max_length=9611)
    class Meta:
        db_table = 'DairyContent'

