from django.db import models

class Employee(models.Model):
    # emplidはプライマリキーとして定義
    emplid = models.CharField(primary_key=True, max_length=50)
    # 新たに追加するemplnmフィールド（従業員名）
    emplnm = models.CharField(max_length=100)

    class Meta:
        db_table = 'employees'
        managed = False  # 既存のテーブルなのでDjangoで管理しない