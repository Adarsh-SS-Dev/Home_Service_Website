from django.contrib import admin
from .models import (
    users, workers, Country, State, City,
    ServiceCatogarys, ServiceRequests, Response, Feedback, Profile
)

@admin.register(users)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('admin', 'contact_number', 'gender', 'created_at')
    search_fields = ('admin__username', 'contact_number')
    list_filter = ('gender', 'created_at')

@admin.register(workers)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('admin', 'contact_number', 'designation', 'city', 'acc_activation', 'avalability_status')
    search_fields = ('admin__username', 'designation', 'city')
    list_filter = ('acc_activation', 'avalability_status', 'city')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state__name')

@admin.register(ServiceCatogarys)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)

@admin.register(ServiceRequests)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'city', 'status', 'dateofrequest')
    search_fields = ('user__admin__username', 'service__Name', 'city__name')
    list_filter = ('status', 'city', 'dateofrequest')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('requests', 'assigned_worker', 'Date', 'status')
    search_fields = ('requests__user__admin__username', 'assigned_worker__admin__username')
    list_filter = ('status', 'Date')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('User', 'Employ', 'Rating', 'Date')
    search_fields = ('User__username', 'Employ__admin__username')
    list_filter = ('Rating', 'Date')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'forget_token')
    search_fields = ('user__username',)
