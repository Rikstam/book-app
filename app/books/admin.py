from django.contrib import admin

from .models import Book, CustomUser, Author, Address, Publisher, Country

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
    list_filter = ("author", "rating",)



admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Publisher)
admin.site.register(Country)