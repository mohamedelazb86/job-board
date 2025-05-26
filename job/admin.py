from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category,Job,Loction,Apply


class JobAdmin(SummernoteModelAdmin):
    list_display=['title','category','publish_date']
    list_filter=['category']
    search_fields=['title','descriptions']

    summernote_fields=('descriptions')
    


admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Loction)
admin.site.register(Apply)