from django.urls import path, include
from . import views
from django.conf import settings # new
from django.conf.urls.static import static # new

app_name = 'posts'


urlpatterns = [
	path('',views.PostList.as_view(),name='all'),
	path('new/',views.CreatePost.as_view(),name='create'),
	path('by/(?P<username>[-\w]+)/',views.UserPosts.as_view(),name='for_user'),
	path('by/(?P<username>[-\w]+)/(?P<pk>\d+)/',views.PostDetail.as_view(),name='single'),
	path('delete/(?P<pk>\d+)/',views.DeletePost.as_view(),name='delete')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
