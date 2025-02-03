from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name", "is_staff"]

    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "dob",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("updated_at", "created_at", "last_login")}),
    )

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "username",
                "first_name",
                "last_name",
                "email",
                "phone_number",
                "dob",
                "password",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        },
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
