from django.contrib import admin
from les_15_users.models import User, UserInfo, Actor, Movie, Director

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ['age']
    list_display = ('first_name', 'last_name', 'country', 'rating')
    search_fields = ['country', 'last_name']
    list_filter = ['rating']
    fields = ['rating', 'country']
    list_per_page = 2

    def set_rating_to_0(self, request, queryset):       # request - добавлять обязательно! такой синтаксис.
        print(request)   # Покажет САМ запрос к БД, который начинается с "POST /admin... HTTP/1.1"

        queryset.update(rating=0)

    set_rating_to_0.short_description = 'Set users rating to 0'
    actions = [set_rating_to_0]


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 2

class DirectorAdmin(admin.ModelAdmin):
    inlines = [MovieInline]
admin.site.register(UserInfo)

# ////////////////   TO   LESSON  from 23-06-25, See Video Video 20, 52:00    //////////////////////
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director, DirectorAdmin)


