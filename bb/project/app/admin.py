from django.contrib import admin
from django.conf import settings

from .models import Blood_stock,BloodDonor_hospitals,BloodDonor_organisation,Admin_login

class Blood_stockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blood_stock, Blood_stockAdmin)



class BloodDonor_hospitalsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BloodDonor_hospitals,BloodDonor_hospitalsAdmin)


class BloodDonor_organisationAdmin(admin.ModelAdmin):
    pass
admin.site.register(BloodDonor_organisation,BloodDonor_organisationAdmin)

class Admin_loginAdmin(admin.ModelAdmin):
    pass
admin.site.register(Admin_login,Admin_loginAdmin)