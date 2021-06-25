from django.db import models

# Create your models here.


class User(models.Model):
    # id int primary_key auto_increment
    id = models.AutoField(primary_key=True,verbose_name='主键')
    # username varchar(32)
    username = models.CharField(max_length=32,verbose_name='用户名')
    """
    CharField必须要指定max_length参数 不指定会直接报错
    verbose_name该参数是所有字段都有的 就是用来对字段的解释
    """
    # password int
    # password = models.IntegerField(verbose_name='密码')
    password = models.CharField(verbose_name='密码',max_length=64)
    # age = models.IntegerField(verbose_name='年龄')
    # # 该字段可以为空
    # info = models.CharField(max_length=32,verbose_name='个人简介',null=True)
    # # 直接给字段设置默认值
    # hobby = models.CharField(max_length=32,verbose_name='兴趣爱好',default='study')

    def __str__(self):
        return '%s'%self.username


class Author(models.Model):
    # 由于一张表中必须要有一个主键字段 并且一般情况下都叫id字段
    # 所以orm当你不定义主键字段的时候 orm会自动帮你创建一个名为id主键字段
    # 也就意味着 后续我们在创建模型表的时候如果主键字段名没有额外的叫法 那么主键字段可以省略不写
    # username varchar(32)
    username = models.CharField(max_length=32)
    # password int
    password = models.IntegerField()

