from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('admin-login',views.admin_login, name='admin_login'),
    path('lesson-audio/<int:lesson_id>/', views.lesson_audio, name='lesson_audio'),
    path('islamic-calender/', views.islamic_calender, name='islamic-calender'),
    path('news/', views.news_list, name='news_list'),
    path('add/', views.add_event, name='add_event'),  # URL for adding new event
    path('upload-qur/', views.upload_qur, name='upload-qur'),
    path('qur-list/', views.qur_list, name='qur_list'),
    path('suras/', views.sura_list, name='sura_list'),
    path('play-audio/<int:audio_id>/', views.play_audio, name='play_audio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
