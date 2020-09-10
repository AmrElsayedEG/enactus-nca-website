from django.contrib import admin
from .models import Season_board_1, Season_board_2, Event, event_reservation, Gallery, recruitment, open_recruitment, \
    summary, qr_code, sponsers

# Register your models here.
admin.site.register(Season_board_1)
admin.site.register(Season_board_2)
admin.site.register(Event)
admin.site.register(event_reservation)
admin.site.register(Gallery)
admin.site.register(recruitment)
admin.site.register(open_recruitment)
admin.site.register(summary)
admin.site.register(qr_code)
admin.site.register(sponsers)

admin.site.site_header = 'Enactus NCA Administration'
