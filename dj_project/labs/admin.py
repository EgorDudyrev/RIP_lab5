from django.contrib import admin

# Register your models here.
@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
