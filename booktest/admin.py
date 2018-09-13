from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','bname','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcomment',]


# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)