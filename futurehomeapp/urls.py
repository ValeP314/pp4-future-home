from django.urls import path
from . import views
from .views import ListingList, ListingDetail, AddListingView
from .views import DeleteListingView, UpdateListingView


urlpatterns = [
    path('', ListingList.as_view(), name='home'),
    path('listing/<int:pk>', ListingDetail.as_view(), name='listing_detail'),
    path('add_listing/', AddListingView.as_view(), name='add_listing'),
    path('listing/edit/<int:pk>',
         UpdateListingView.as_view(), name='update_listing'),
    path('listing/<int:pk>/delete',
         DeleteListingView.as_view(), name='delete_listing'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('like/<slug:slug>', views.ListingLike.as_view(), name='listing_like'),
]
