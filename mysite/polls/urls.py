from django.conf.urls import url
from . import views # . means from the same directory



urlpatterns = [
url (r'^$',views.hello , name ='list'),
url (r'^(?P<slug>[\w-]+)/$',views.article_detail, name="detail"),]
#capture url bitsto the veiw fun
