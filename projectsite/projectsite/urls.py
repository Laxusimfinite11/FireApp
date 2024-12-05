from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView, ChartView, PieCountbySeverity,LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),

    path('firestation_list', FireStationList.as_view(), name='firestation-list'),
    path('firestation_list/add', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FireStationDeleteView.as_view(), name='firestation-delete'),
]
