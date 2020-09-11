from django.contrib import admin
from .models import Season_board_1, Season_board_2, Event, event_reservation, recruitment, open_recruitment, \
    summary, qr_code, sponsers, all_seasons_board

# Register your models here.
admin.site.register(Season_board_1)
admin.site.register(Season_board_2)
admin.site.register(Event)
admin.site.register(event_reservation)
admin.site.register(recruitment)
admin.site.register(open_recruitment)
admin.site.register(summary)
admin.site.register(qr_code)
admin.site.register(sponsers)
admin.site.register(all_seasons_board)

admin.site.site_header = 'Enactus NCA Administration'
