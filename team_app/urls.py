from django.urls import path, include
from . import views


urlpatterns = [
    path('team-generator/', views.team_generator, name='team_generator'),
    path('reroll/', views.reroll, name='reroll'),
    path('cointoss/', views.cointoss, name='cointoss'),
    path('random_pass/', views.random_pass, name='random_pass')
]