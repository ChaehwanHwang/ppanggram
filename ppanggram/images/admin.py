from django.contrib import admin
from . import models
# Register your models here.
# . 은 같은 폴더 내 모두

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'caption',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment) # 꼭 이자리에 써야함
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

