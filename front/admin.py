from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
	list_display = list_display_links = ['index_no', 'title', 'notice_content', 'context_img', 'reg_date', ]


