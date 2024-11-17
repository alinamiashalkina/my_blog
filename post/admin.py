from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2
    readonly_fields = ("create_date",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date",)
    fieldsets = (
        ("Post Description", {
            "fields": ("title", "author", "publication_date",)
        }),
        ("More Details", {
            "fields": ("post_text",)
        })
    )
    readonly_fields = ("publication_date",)
    search_fields = ("title", "post_text",)
    ordering = ("title",)
    list_filter = ("publication_date", "author",)
    inlines = [CommentInline]
