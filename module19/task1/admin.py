from django.contrib import admin
from .models import Buyer, Game, News


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance', 'age')
    list_filter = ('balance', 'age')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'size')
    list_filter = ('size', 'cost')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20


admin.site.register(News)
