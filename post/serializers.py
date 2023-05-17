from rest_framework import serializers
from report.models import Question
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    report_cnt = serializers.IntegerField()
    is_deleted = serializers.SerializerMethodField()

    def get_is_deleted(self, instance):
        if instance.deleted_at:
            return True
        return False

    def get_title(self, instance):
        if instance.type == "COMMON":
            return instance.content[:20]
        elif instance.type == "NEMO":
            return instance.created_at.strftime("%Y-%m-%d %p %I시 %M분") + " 니모"

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "type",
            "is_student",
            "created_at",
            "is_deleted",
            "title",
            "report_cnt",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "type", "is_student", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    question = serializers.IntegerField(write_only=True)
    answer = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "password",
            "question",
            "answer",
            "post_num",
        ]

    def validate(self, data):
        question_id = data.pop("question")
        answer = data.pop("answer")
        try:
            question_instance = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question instance does not exist")
        data["is_student"] = question_instance.answer == answer
        return data

    def create(self, validated_data):
        validated_data["filtered_content"] = validated_data["content"]
        return super().create(validated_data)
