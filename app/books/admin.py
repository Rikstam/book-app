from django.contrib import admin

from .models import Book, CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    list_display = (
        "id",
        "title",
        "author",
        "rating",
        "is_bestselling",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            )
    }



admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser)