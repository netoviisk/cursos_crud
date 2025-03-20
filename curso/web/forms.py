from django import forms
from .models import Curso, Aluno, Inscricao

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'carga_horaria', 'instrutor']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'telefone']

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['aluno', 'curso']

    def __init__(self, *args, **kwargs):
        super(InscricaoForm, self).__init__(*args, **kwargs)
        self.fields['aluno'].queryset = Aluno.objects.all()
        self.fields['curso'].queryset = Curso.objects.all()

class CursoPesquisaForm(forms.Form):
    nome = forms.CharField(max_length=255, required=False, label='Nome do Curso')
    instrutor = forms.CharField(max_length=255, required=False, label='Instrutor')

class AlunoPesquisaForm(forms.Form):
    aluno_nome = forms.CharField(required=False, label="Nome do Aluno", max_length=255)
    aluno_email = forms.EmailField(required=False, label="Email do Aluno")

class InscricaoPesquisaForm(forms.Form):
    inscricao_aluno = forms.CharField(required=False, label="Nome do Aluno", max_length=255)
    inscricao_curso = forms.CharField(required=False, label="Nome do Curso", max_length=255)
