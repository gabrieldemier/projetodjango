from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})


def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos:lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'aluno_form.html', {'form': form})

def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno_detalhe.html', {'aluno': aluno})

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos:lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno_form.html', {'form': form})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos:lista_alunos')
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})
