from django.contrib import admin
from .models import Boat, MembershipType, Membership, EmailList


class BoatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Boat, BoatAdmin)

class MembershipTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(MembershipType, MembershipTypeAdmin)

class MembershipAdmin(admin.ModelAdmin):
    pass
admin.site.register(Membership, MembershipAdmin)

class EmailListAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmailList, EmailListAdmin)

