from django.contrib import admin

from core.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text',)
    list_filter = ('user',)

admin.site.register(Comment, CommentAdmin)
