from django.urls import path
from web import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cadastrar-curso/', views.cadastrar_curso, name='cadastrar_curso'),
    path('cadastrar-aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('inscrever-aluno/', views.inscrever_aluno, name='inscrever_aluno'),
    path('lista-cursos/', views.listar_cursos, name='lista_cursos'),
    path('lista-alunos/', views.listar_alunos, name='lista_alunos'),
    path('lista-inscricoes/', views.listar_inscricoes, name='lista_inscricoes'),
    path('editar-curso/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('editar-aluno/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('excluir-curso/<int:pk>/', views.excluir_curso, name='excluir_curso'),
    path('excluir-aluno/<int:pk>/', views.excluir_aluno, name='excluir_aluno'),
    path('cancelar-inscricao/<int:inscricao_id>/', views.cancelar_inscricao, name='cancelar_inscricao'),
    path('consultas/', views.consultas, name='consultas'),
]
