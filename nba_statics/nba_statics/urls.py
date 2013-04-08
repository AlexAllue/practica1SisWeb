from django.conf.urls import patterns, include, url
from statics.views import*

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nba_statics.views.home', name='home'),
    # url(r'^nba_statics/', include('nba_statics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',mainpage),
    url(r'^players/$', players),
    url(r'^players/(?P<player_name>\w+)/$', playerdetail),
    url(r'^teams/$', teams),
    url(r'^teams/(?P<team_name>\w+)/$', teaminfo),
    url(r'^games/$', games),
    url(r'^games/(?P<game_id>\d+)/$', gameinfo),
    url(r'^leagues/$', leagues),
    url(r'^leagues/(?P<league_id>\d+)/$', leagueinfo)
)
