from django.db import models

# Employee モデルは、既存の "employees" テーブルに対応します
class Employee(models.Model):
    # 従業員IDをプライマリキーとして定義（最大50文字）
    emplid = models.CharField(primary_key=True, max_length=50)
    # 従業員名を格納するフィールド（最大100文字）
    emplnm = models.CharField(max_length=100)

    class Meta:
        db_table = 'employees'  # 対応するテーブル名
        managed = False         # 既存のテーブルを Django による自動管理（マイグレーション）から除外
