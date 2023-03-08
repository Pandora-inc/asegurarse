from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from django.utils import timezone
from django.db import connection

from .forms import ClientesPolizasForm, CompaniaForm, LibrosRubricadosForm, VencimientoPolizasForm
from .models import Clientes, Companias, Secciones, Productores, Ordenes, Polizas


# Create your views here.

