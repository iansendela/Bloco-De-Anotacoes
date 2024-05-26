from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlocoNota, Tema
from django.views import generic
from .forms import Criar_bloco, Criar_Tema
from django.db.models import Q


class HomeListView(generic.ListView):
    model = BlocoNota
    template_name = 'home.html'
    context_object_name = 'bloco_list'
    paginate_by = 3 # numero de elementos exibidos por paginas
    
    def get_queryset(self):
        return BlocoNota.objects.order_by('-data_criada')
    
    
    

class BlocosListView(generic.ListView):
    model = BlocoNota
    template_name = 'blocos.html'
    context_object_name = 'bloco_list'
    paginate_by = 8 # numero de elementos exibidos por paginas
    
    
    def get_queryset(self):
        query = self.request.GET.get('tema')
        if query:
            return BlocoNota.objects.filter(Q(tema=query)).order_by('-data_criada')
        else:
            return BlocoNota.objects.order_by('-data_criada')



class SearchResultsView(generic.ListView):
    model = BlocoNota
    template_name = 'search_results.html'
    context_object_name = 'bloco_list'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return BlocoNota.objects.filter(
                Q(titulo__icontains=query) | Q(conclusao__icontains=query)
            ).order_by('-data_criada')
        else:
            return BlocoNota.objects.none()  # Retorna uma queryset vazia se não houver consulta    




def criar_bloco(request):
    if request.method == 'POST':
        form = Criar_bloco(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Criar_bloco()            

    return render(request, 'forms/criar_bloco.html', {'form': form})



def ler_bloco(request, bloco_id):
    bloco = get_object_or_404(BlocoNota, pk=bloco_id)
    return render(request, 'detalhes.html', {'bloco': bloco})
    



def editar_bloco(request, bloco_id):
    bloco = get_object_or_404(BlocoNota, pk=bloco_id)
    
    if request.method == "POST":
        form = Criar_bloco(request.POST, instance=bloco)
        if form.is_valid():
            form.save()
            return redirect('detalhes', bloco_id=bloco_id)
    else:
        form = Criar_bloco(instance=bloco)
        
    return render(request, 'forms/update/update_bloco.html', {'form': form})



def deletar_bloco(request, bloco_id):
    bloco = get_object_or_404(BlocoNota, pk=bloco_id)
    bloco.delete()
    return redirect('home')




def criar_tema(request):
    if request.method == 'POST':
        form = Criar_Tema(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Criar_Tema()
        
    return render(request, 'forms/criar_tema.html', {'form': form})




def temas(request):
    temas = Tema.objects.all()
    return render(request, 'temas.html', {"temas": temas})


def ler_tema(request, tema_id):
    pass




def editar_tema(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)

    if request.method == 'POST':
        form = Criar_Tema(request.POST, instance=tema)
        if form.is_valid():
            form.save()
            return redirect('temas')
    else:
        form = Criar_Tema(instance=tema)
    
    return render(request, 'forms/update/update_tema.html', {'form': form})




#Criar um modal para verficar se usuario quer mudar sim ou não
def deletar_tema(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    tema.delete()
    return redirect('temas')




'''class BlocosListView(generic.ListView):
    model = BlocoNota
    template_name = 'blocos.html'
    context_object_name = 'bloco_list'
    paginate_by = 8 # numero de elementos exibidos por paginas
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return BlocoNota.objects.filter(Q(tema__icontains=query)).order_by('-data_criada')
        else:
            return BlocoNota.objects.none()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temas = Tema.objects.all()
        context = {'temas': temas}
        return context'''