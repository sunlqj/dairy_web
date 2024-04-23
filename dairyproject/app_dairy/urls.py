from django.urls import path
from .views import * 


urlpatterns = [    
    #path('user/', api_task_user),
    path('cs/', api_csss),
    path('list/', api_getdairy),
    path('create_dairy/', api_create_dairy),
    path('get_dairy/', api_get_dairy),
] 