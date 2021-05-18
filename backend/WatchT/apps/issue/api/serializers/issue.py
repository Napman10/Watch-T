from rest_framework import serializers

from ....abstract.functional import convert_last_seen, string_or_empty
from ...models import Issue, IssueType


class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = ('typo',)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

    author = serializers.SerializerMethodField()
    executor = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    typo = serializers.SerializerMethodField()

    def get_typo(self, obj: Issue) -> str:
        return str(obj.typo.typo)

    def get_created(self, obj: Issue) -> str:
        return convert_last_seen(obj.created)

    def get_parent(self, obj: Issue) -> str:
        return string_or_empty(obj.parent)

    def get_status(self, obj: Issue) -> str:
        statuses = ['Новая', 'Требуется уточнение', 'Назначена', 'В работе', 'Проверка', 'Готово']
        return statuses[obj.status]

    def get_author(self, obj: Issue) -> str:
        return str(obj.author)

    def get_executor(self, obj: Issue) -> str:
        return string_or_empty(obj.executor)

    def get_project(self, obj: Issue) -> dict:
        return {'name': str(obj.project), 'id': str(obj.project.id)}

    def get_priority(self, obj: Issue) -> str:
        priorities = ['Низкий', 'Обычный', 'Серьёзный', 'Критический']
        return priorities[obj.priority]
