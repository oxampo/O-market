
#Django
from django.contrib import admin

#Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user','cedula')

    list_display_links = ('pk','user')

    #list_editable = ('address',)

    search_fields = ('user__email','user__first_name',
     'user__last_name',)

    list_filter = (
         'created','modified','user__is_staff')

    fieldsets = (
        ('Profile', {
           'fields': ('user',)

        }
        ),
        ('Info user:',{
            'fields':('cedula',)
        }
        ),
        ('Metadata:',{
            'fields': (('created','modified'))
        })


    )

    readonly_fields = ('created','modified')
    

