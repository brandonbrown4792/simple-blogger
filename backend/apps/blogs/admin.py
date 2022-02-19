from django.contrib import admin
from apps.blogs.models import Post, PostLike, PostComment, CommentLike

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostAdmin)
admin.site.register(PostComment, PostAdmin)
admin.site.register(CommentLike, PostAdmin)
