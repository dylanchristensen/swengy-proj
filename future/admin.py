from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Track, Path, Video, Resource, Project


# Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'track', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'track')
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'track')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


# Inline for Videos
class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


# Inline for Resources
class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1


# Inline for Projects
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


# Path Admin
@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('name', 'track', 'description')
    search_fields = ('name', 'description')
    list_filter = ('track',)
    inlines = [VideoInline, ResourceInline, ProjectInline]


# Registering Track
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register other models directly
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title', 'description')
