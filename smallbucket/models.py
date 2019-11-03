from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Status(models.Model):

    user = models.OneToOneField(User, verbose_name="ユーザー", on_delete=models.CASCADE)

    get_up = models.IntegerField(verbose_name="起床", default=0)
    sleep_time = models.IntegerField(verbose_name="睡眠時間", default=0)
    chew_well = models.IntegerField(verbose_name="咀嚼", default=0)
    stretch = models.IntegerField(verbose_name="ストレッチ", default=0)
    exercise = models.IntegerField(verbose_name="運動", default=0)
    good_day = models.IntegerField(verbose_name="幸福感", default=0)
    daily_login = models.IntegerField(verbose_name="ログイン日数", default=0)

    # メソッドにするとソートが厳しくなる・・・mybucketの方も同様に。
    # basic_total = models.IntegerField(verbose_name="基礎点", default=0)



class MyBucket(models.Model):

    # ステータスと同じようにユーザーと一対一のリレーション組む感じで平気か？
    # user = models.OneToOneField(User, verbose_name="ユーザー", on_delete=models.CASCADE)

    name1 = models.CharField(verbose_name="マイバケット１", max_length=255, null=True)
    score1 = models.IntegerField(verbose_name="１の点数", default=0)
    name2 = models.CharField(verbose_name="マイバケット２", max_length=255, null=True)
    score2 = models.IntegerField(verbose_name="２の点数", default=0)
    name3 = models.CharField(verbose_name="マイバケット３", max_length=255, null=True)
    score3 = models.IntegerField(verbose_name="３の点数", default=0)

    # 