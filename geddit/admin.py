from django.contrib import admin

from geddit.models import LikesDislikes, Post, Comments, SubGeddit, SubGedditPost

admin.site.register(LikesDislikes)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(SubGeddit)
admin.site.register(SubGedditPost)