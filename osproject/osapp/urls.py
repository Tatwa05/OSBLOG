from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.racefn, name=""),
    path('racecondition', views.racefn, name="racecondition"),
    path('criticalsection',views.criticalfn,name="criticalsection"),
    path('mutualexclusion', views.mutualfn, name="mutualexclusion"),
    path('petersonssolution', views.peterfn, name="petersonssolution"),
    path('semaphores', views.semaphoresfn, name="semaphores"),


]