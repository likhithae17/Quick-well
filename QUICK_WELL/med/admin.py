from django.contrib import admin
from .models import Medicine, Userlog, PurchaseItem, UserProfile, Order

admin.site.register(Medicine)
admin.site.register(Userlog)
admin.site.register(PurchaseItem)
admin.site.register(UserProfile)
admin.site.register(Order)