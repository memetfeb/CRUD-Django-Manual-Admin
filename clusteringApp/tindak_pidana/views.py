from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . import models
from . import forms


def index(request):
    context={
        'totalUser':90,
        'averageTime': 512.23,
    }
    return render(request,'index.html', context)

def tindak_pidana(request):
    data_TP = models.Kategori.objects.all()
    context={
        'data':data_TP,
    }
    return render(request,'list_TP.html',context)

def create(request):
    if request.method=='POST':
        models.Kategori.objects.create(
            nama_TP = request.POST['nama_TP'],
            pasal_TP = request.POST['pasal_TP'],
            kategori_TP = request.POST['kategori_TP'],
        )
        messages.success(request,'Tambah Tindak Pidana Berhasil!')
    return redirect('tindak_pidana')

def edit(request):
    if request.method=='POST':
        kategori = models.Kategori.objects.get(id=request.POST['id'])
        kategori.nama_TP = request.POST['nama_TP']
        kategori.pasal_TP = request.POST['pasal_TP']
        kategori.kategori_TP = request.POST['kategori_TP']
        kategori.save()
        
        messages.success(request,'Edit Berhasil!')
    return redirect('tindak_pidana')

def delete(request, id_TP):
    models.Kategori.objects.get(id=id_TP).delete()
    messages.success(request,'Hapus Berhasil!')
    return redirect('tindak_pidana')
