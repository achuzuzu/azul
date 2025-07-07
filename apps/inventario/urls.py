from django.urls import path
from .views import CategoriaActualizarView, CategoriaCrearView, CategoriaEliminarView, CategoriaListaView, ProductoActualizarView, ProductoEliminarView, ProductoListaView, ProductoCrearView

app_name = "inventario"
urlpatterns = [ 
    path('producto/crear/', ProductoCrearView.as_view(), name='Producto_crear'),
    path('producto/<int:pk>/eliminar/', ProductoEliminarView.as_view(), name='Producto_eliminar'),
    path('producto/<int:pk>/actualizar/', ProductoActualizarView.as_view(), name='Producto_actualizar'),
    path('producto/listar/', ProductoListaView.as_view(), name='Producto_lista'),
    path('categoria/crear/', CategoriaCrearView.as_view(), name='Categoria_crear'),
    path('categoria/eliminar/', CategoriaEliminarView.as_view(), name='Categoria_eliminar'),
    path('categoria/<int:pk>/actualizar/', CategoriaActualizarView.as_view(), name='Categoria_actualizar'),
    path('categoria/<int:pk>/listar/', CategoriaListaView.as_view(), name='Categoria_lista')
]