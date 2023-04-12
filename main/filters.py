import django_filters
from django_filters import CharFilter
from .models import Todo


class TodoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user', 'createdAt']


class CompletedTodoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user', 'createdAt', 'is_completed']
