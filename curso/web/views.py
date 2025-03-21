from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Aluno, Inscricao
from .forms import CursoForm, AlunoForm, InscricaoForm, CursoPesquisaForm, AlunoPesquisaForm, InscricaoPesquisaForm


def home(request):
    return render(request, 'home.html')

# Cadastrar Curso
def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cadastrar_curso.html', {'form': form})

# Cadastrar Aluno
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})

# Inscrever Aluno
def inscrever_aluno(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscricoes')
    else:
        form = InscricaoForm()
    return render(request, 'inscrever_aluno.html', {'form': form})

# Consultar Cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

# Consultar Alunos
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

# Consultar Inscrições
def listar_inscricoes(request):
    inscricoes = Inscricao.objects.all()
    return render(request, 'lista_inscricoes.html', {'inscricoes': inscricoes})

# Editar Curso
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'editar_curso.html', {'form': form})

# Editar Aluno
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'editar_aluno.html', {'form': form})

# Excluir Curso
def excluir_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('lista_cursos')

# Excluir Aluno
def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('lista_alunos')

def consultas(request):
    cursos = None
    alunos = None
    inscricoes = None

    # Inicializando os formulários com os dados GET
    curso_form = CursoPesquisaForm(request.GET)
    aluno_form = AlunoPesquisaForm(request.GET)
    inscricao_form = InscricaoPesquisaForm(request.GET)

    # Consulta de cursos
    if curso_form.is_valid():  # Verificando se o formulário de curso é válido
        nome = curso_form.cleaned_data.get('curso_nome')  # Corrigido o campo
        instrutor = curso_form.cleaned_data.get('curso_instrutor')  # Corrigido o campo
        cursos = Curso.objects.all()  # Buscando todos os cursos

        if nome:  # Se o nome foi fornecido, aplica o filtro
            cursos = cursos.filter(nome__icontains=nome)

        if instrutor:  # Se o instrutor foi fornecido, aplica o filtro
            cursos = cursos.filter(instrutor__icontains=instrutor)

    # Consulta de alunos
    if aluno_form.is_valid():
        nome = aluno_form.cleaned_data.get('aluno_nome')
        email = aluno_form.cleaned_data.get('aluno_email')
        alunos = Aluno.objects.all()

        if nome:
            alunos = alunos.filter(nome__icontains=nome)
        if email:
            alunos = alunos.filter(email__icontains=email)

    # Consulta de inscrições
    if inscricao_form.is_valid():
        aluno_nome = inscricao_form.cleaned_data.get('inscricao_aluno')
        curso_nome = inscricao_form.cleaned_data.get('inscricao_curso')
        inscricoes = Inscricao.objects.all()

        if aluno_nome:
            inscricoes = inscricoes.filter(aluno__nome__icontains=aluno_nome)
        if curso_nome:
            inscricoes = inscricoes.filter(curso__nome__icontains=curso_nome)

    # Retorna o render com os resultados das consultas
    return render(request, 'consultas.html', {
        'cursos': cursos,
        'alunos': alunos,
        'inscricoes': inscricoes,
        'curso_form': curso_form,
        'aluno_form': aluno_form,
        'inscricao_form': inscricao_form,
    })

def cancelar_inscricao(request, inscricao_id):
    inscricao = get_object_or_404(Inscricao, id=inscricao_id)

    # Verificar se o usuário atual é o aluno associado à inscrição
    if request.user == inscricao.aluno.user:  # Isso assume que você tem um campo `user` em Aluno, caso contrário, adapte a condição
        inscricao.delete()  # Exclui a inscrição do banco de dados
        return redirect('listar_inscricoes')  # Redireciona para a página de inscrições após o cancelamento
    else:
        return redirect('consultar_cursos')  # Redireciona para a consulta de cursos se não for o aluno correto