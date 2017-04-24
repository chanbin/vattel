from django.conf.urls import url
from . import views

# define action
urlpatterns = [
	url(r'^$', views.base_index, name='base_index'),
	
	url(r'^index.html$', views.base_index, name='base_index'),
	url(r'^charts.html$', views.base_charts, name='base_charts'),
	url(r'^tables.html$', views.base_tables, name='base_tables'),
	url(r'^forms.html$', views.base_forms, name='base_forms'),
	url(r'^bootstrap-elements.html$', views.base_bootstrap_elements, name='base_bootstrap_elements'),
	url(r'^bootstrap-grid.html$', views.base_bootstrap_grid, name='base_bootstrap_grid'),
	url(r'^dropdown.html$', views.base_dropdown, name='base_dropdown'),
	url(r'^blank-page.html$', views.base_blank_page, name='base_blank_page'),
	url(r'^index-rtl.html$', views.base_index_rtl, name='base_index_rtl'),
]