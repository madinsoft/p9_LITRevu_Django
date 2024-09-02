from django.contrib import admin
from litreview_app.models import Review, Ticket

# Register your models here.
"""class UserAdmin(admin.ModelAdmin):
    list_display=('pseudo', 'literary_taste')"""

admin.site.register(Review)
admin.site.register(Ticket)
#admin.site.register(User, UserAdmin)
