from django.contrib import admin

from api.models import User, Item


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model=User
    list_display = [
        "email",
        "last_login",
        "city",
    ]
    list_filter = [
        "city",
    ]
    fields = [
        "email",
        "city",
    ]
    readonly_fields = [
        "email",
        "city",
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = [
        "name",
        "price",
    ]
    list_filter = [
        "name",
        "color",
        "stuff_type",
        "stuff_size",
    ]
    fields = [
        "name",
        "description",
        "color",
        "stuff_type",
        "stuff_size",
        "price",
    ]