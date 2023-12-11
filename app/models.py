from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    deptno=models.ForeignKey(Dept('deptno'),on_delete=models.CASCADE)
    sal=models.IntegerField(null=True)
class SalGrade(models.Model):
    empno=models.ForeignKey(Emp('empno'),on_delete=models.CASCADE)
    sal=models.IntegerField()
    comm=models.IntegerField()
class Bonus(models.Model):
    empno=models.ForeignKey(Emp('empno'),on_delete=models.CASCADE)
    bonus=models.IntegerField()