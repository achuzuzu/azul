from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.views import View, generic
from django.shortcuts import get_list_or_404, redirect, render
from apps.inventario.models import Categoria, Producto
from django.urls import reverse_lazy

class CategoriaCrearView(generic.CreateView):
    model = Categoria 
    fields = '__all__' 
    template_name = 'Categoria/crear.html' 
    success_url = reverse_lazy('evaluacion:list-categoria')

class CategoriaActualizarView(generic.CreateView):
    model = Categoria 
    fields = '__all__' 
    template_name = 'Categoria/actualizar.html' 
    success_url = reverse_lazy('evaluacion:list-categoria')

class CategoriaEliminarView(generic.CreateView):
    model = Categoria 
    fields = '__all__' 
    template_name = 'Categoria/eliminar.html' 
    success_url = reverse_lazy('evaluacion:list-categoria')

class CategoriaListaView(generic.CreateView):
    model = Categoria 
    fields = '__all__' 
    template_name = 'Categoria/lista.html' 
    success_url = reverse_lazy('evaluacion:list-categoria')

class ProductoCrearView(generic.CreateView):
    model = Producto 
    fields = '__all__' 
    template_name = 'Producto/crear.html' 
    success_url = reverse_lazy('inventario:Producto_lista')

class ProductoActualizarView(generic.UpdateView):
    model = Producto 
    fields = '__all__' 
    template_name = 'Producto/actualizar.html' 
    success_url = reverse_lazy('inventario:Producto_lista')

class ProductoEliminarView(DeleteView):
    model = Producto  
    template_name = 'Producto/eliminar.html' 
    success_url = reverse_lazy('inventario:Producto_lista')

class ProductoListaView(generic.ListView):
    model = Producto 
    fields = '__all__' 
    template_name = 'Producto/lista.html' 
    context_object_name = 'productos'
