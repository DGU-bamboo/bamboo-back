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
        if instance.deleted_at:
            return "삭제된/n제보입니다."
        return instance.title

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
    title = serializers.SerializerMethodField()
    is_deleted = serializers.SerializerMethodField()

    def get_is_deleted(self, instance):
        if instance.deleted_at:
            return True
        return False

    def get_title(self, instance):
        if instance.deleted_at:
            return "삭제된/n제보입니다."
        return instance.title

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "type",
            "is_student",
            "created_at",
            "is_deleted",
        ]


class CommentSerializer(serializers.ModelSerializer):
    question = serializers.IntegerField(write_only=True)
    answer = serializers.CharField(max_length=20, write_only=True)
    content = serializers.CharField()
    password = serializers.CharField(write_only=True)

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

    def get_content(self, instance):
        if instance.deleted_at:
            return "< 작성자의 요청에 의해 삭제된 댓글입니다. >"
        return instance.content

    def validate(self, data):
        question_id = data.pop("question")
        answer = data.pop("answer")
        try:
            question_instance = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question instance does not exist")
        data["is_student"] = question_instance.answer == answer

        post_num_digit = "".join(filter(str.isdigit, data["post_num"]))
        try:
            data["post"] = Post.objects.get(id=post_num_digit)
        except Post.DoesNotExist:
            data["post"] = None
        return data

    def create(self, validated_data):
        validated_data["filtered_content"] = validated_data["content"]
        return super().create(validated_data)
