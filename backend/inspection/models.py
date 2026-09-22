from django.db import models


class Inspection(models.Model):
    aid_code = models.CharField("航标编号", max_length=40)
    measured_cd = models.FloatField("实测光强")
    required_cd = models.FloatField("要求光强")
    bearing_error_deg = models.FloatField("方位偏差")
    verdict = models.CharField("结论", max_length=20)
    note = models.CharField("说明", max_length=200)
    created_by = models.CharField("登记人", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]


class RejectedAttempt(models.Model):
    """同一灯号同一自然日重复登记、被拦下未写入的尝试。"""

    aid_code = models.CharField("航标编号", max_length=40)
    attempted_by = models.CharField("操作者", max_length=64)
    attempted_at = models.DateTimeField("发生时刻", auto_now_add=True)
    conflicting_inspection = models.ForeignKey(
        Inspection,
        verbose_name="撞上的实测",
        on_delete=models.CASCADE,
        related_name="rejected_attempts",
    )

    class Meta:
        ordering = ["-id"]
