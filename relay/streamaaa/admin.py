from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.admin import GroupAdmin as AuthGroupAdmin


class UserProfileInline(admin.StackedInline):
    model = StreamUser
    max_num = 1
    can_delete = False
    can_view_details = True
    can_edit = False
    readonly_fields = ('guid', 'quick')
    fieldsets = (
        ("Details", {'fields': ("handle", 'guid', 'quick')}),
    )
    empty_value_display = "-empty-"


class StreamKeyInline(admin.StackedInline):
    model = StreamKey
    can_view_details = True
    can_edit = False
    readonly_fields = ('guid', 'quick','user',)
    fieldsets = (
        ("Details", {'fields': ("enabled","key",)}),
        ("Extra", {'fields': ('guid', 'quick')}),
    )
    empty_value_display = "-empty-"

class UserAdmin(AuthUserAdmin):
    inlines = [
        UserProfileInline,
        StreamKeyInline,
    ]
    list_display = ["handle", "username", "first_name", "last_name", "email"]

    def handle(self, obj):
        return obj.streamuser.handle

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)


class GroupProfileInline(admin.StackedInline):
    model = StreamGroup
    max_num = 1
    can_delete = False
    can_edit = False
    can_view_details = True
    readonly_fields = ('guid', 'quick')
    fieldsets = (
        ("Details", {'fields': ("handle", 'guid', 'quick')}),
    )
    empty_value_display = "-empty-"


class GroupAdmin(AuthGroupAdmin):
    inlines = [GroupProfileInline]


# unregister old user admin
admin.site.unregister(Group)
# register new user admin
admin.site.register(Group, GroupAdmin)


class RelayPullInline(admin.StackedInline):
    model = GroupRelayAccess.relays_pull.through
    can_view_details = True
    empty_value_display = "-empty-"
    verbose_name = "Pull Relay Access"
    verbose_name_plural = "Pull Relay Access"


class RelayPushInline(admin.StackedInline):
    model = GroupRelayAccess.relays_push.through
    can_view_details = True
    empty_value_display = "-empty-"
    verbose_name = "Push Relay Access"
    verbose_name_plural = "Push Relay Access"


@admin.register(GroupRelayAccess)
class GroupRelayAccessAdmin(admin.ModelAdmin):
    readonly_fields = ('guid', 'quick')
    fieldsets = (
        ('Details', {'fields': ('group',)}),
        ("Extra", {'fields': ('guid', 'quick')}),
    )
    empty_value_display = "-empty-"
    list_display = ["group", "quick"]
    inlines = [
        RelayPushInline,
        RelayPullInline,
    ]
    exclude = (
        'relay_pull',
        'relay_push',
    )


class GroupRelayAccessPushInline(admin.StackedInline):
    model = Relay.with_push.through
    verbose_name = "Push Relay Access"
    verbose_name_plural = "Push Relay Access"
    # readonly_fields = ('guid', 'quick')
    fieldsets = (
        # ('Details', {'fields': ('group',)}),
        # ("Extra", {'fields': ('guid', 'quick')}),
    )
    empty_value_display = "-empty-"
    list_display = ["group", "quick"]
    exclude = (
        'relay_pull',
        'relay_push',
    )
    can_view_details = True


class GroupRelayAccessPullInline(admin.StackedInline):
    model = Relay.with_pull.through
    verbose_name = "Pull Relay Access"
    verbose_name_plural = "Pull Relay Access"
    empty_value_display = "-empty-"
    list_display = ["group", "quick"]
    exclude = (
        'relay_pull',
        'relay_push',
    )
    can_view_details = True

@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):
    readonly_fields = ('guid', 'quick')
    fieldsets = (
        ("Details", {'fields': ('name',)}),
        ("Extra", {'fields': ('guid', 'quick')}),
    )
    empty_value_display = "-empty-"
    list_display = ["name", "quick"]
    inlines = [
        GroupRelayAccessPushInline,
        GroupRelayAccessPullInline,
    ]
