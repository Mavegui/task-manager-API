from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from .models import Task
from .serializers import RegisterSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    # Boas prátacas - User autenticado e Rate limit na API.
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    #Filtros
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields =  ['completed', 'priority']
    search_fields = ['title']
    
    def get_queryset(self):
        #Boa prática sugerida pelo swagger-ui
        if getattr(self, "swagger_fake_view", False):
            return Task.objects.none()
        
        """ Somente o dono de cada tarefa que a ver e modifica, segurança. """
        return Task.objects.filter(user=self.request.user)
    
    
    def perform_create(self, serializer):
        """ Associando tarefa ao user logado no momento, segurança. """
        serializer.save(user=self.request.user)

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    #Permissão de acesso de todos os usuários a endpoint.
    permission_classes = [AllowAny]