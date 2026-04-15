from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include("order.urls")),
    path('payment/', include("payment.urls")),
    path('product/', include("product.urls")),
    path('review/', include("review.urls")),
    path('cart/', include("cart.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)