from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from .views import logout_view, search_view, DataManipulationView

# API Packages
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    # path('product-detail', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('logout/', logout_view, name='logout'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/',views.laptop, name="laptop"),
    path('laptop/<slug:datas>', views.laptop, name='laptopdata'),

    path('topwear/',views.topwear, name="topwear"),
    path('topwear/<slug:datas>', views.topwear, name='topweardata'),

    path('bottomwear/',views.bottomwear, name="bottomwear"),
    path('bottomwear/<slug:datas>', views.bottomwear, name='bottomweardata'),

    path('payment/',views.payment,name="payment"),
    path('excel/',views.excel,name="excel"),

     path('search/', search_view, name='search'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),

    # API Urls

    path('api/',DataManipulationView.as_view(),name="api"),
    path('api/int:cid/',DataManipulationView.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
