from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Student,Teacher,Group


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["id", "username", "first_name", "last_name", "email", "is_staff"]

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



# Register Student with a custom admin class
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'comment')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')


# Correct Group Admin Registration
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name')
    filter_horizontal = ('students',)  # Enables multi-selection UI