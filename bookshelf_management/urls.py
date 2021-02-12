"""bookshelf_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from bookshelf_management.apps.mgmt import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelves', views.bookshelfList, name='detail'),
    path('bookshelves/<int:bookshelfId>/search', views.searchBooks, name='detail'),
    path('bookshelves/<int:bookshelfId>', views.booksInBookshelf, name='detail')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# class CustomAdminSite(admin.AdminSite):      
#     def get_urls(self):        
#         urls = super(CustomAdminSite, self).get_urls() 
#         custom_urls = [            
#             url('admin/bookshelves$', 
#             self.admin_view(organization_admin.preview), name="preview"),        
#         ]        
#         return urls + custom_urls