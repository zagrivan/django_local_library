from django.contrib import admin

from .models import Author, Book, BookInstance, Language, Genre

# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(Author)
admin.site.register(Language)
# admin.site.register(BookInstance)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            "fields": (
                'book', 'imprint', 'id'
            ),
        }),
        ('Availability', {
            'fields': (
                'status', 'due_back', 'borrower'
            ),
        }),
    )
    