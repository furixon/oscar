from django.db import models

# Create your models here.


class Notice(models.Model):
    index_no = models.IntegerField(default=0)
    title = models.CharField(max_length=500)
    notice_content = models.TextField(null=True, blank=True)
    context_img = models.ImageField(null=True, blank=True)
    reg_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항 관리"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('alpha:notice_detail', args=[str(self.id)])