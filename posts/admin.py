from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'user')
    list_display_links = ('title',)
    list_filter = ('created_at', 'updated_at')

    search_fields = (
        'title',
        'user__username',
        'user__first_name',
        'user__last_name'
    )
