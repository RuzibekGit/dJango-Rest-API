from rest_framework import serializers
from comments.models import CommentsModel
from posts.serializers import UserSerializer



class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CommentSerializer, self).__init__(*args,**kwargs)
        self.fields['parent'] = serializers.CharField(required=False, write_only=True)

    user = UserSerializer(read_only=True)
    me_liked = serializers.SerializerMethodField('get_me_liked')
    replies = serializers.SerializerMethodField('get_replies')

    class Meta:
        model = CommentsModel
        fields = ['id', 'uuid', 'comment', 'created_at', 'me_liked', 'user', 'replies']
    
    
    def validate(self, attrs):
        parent = attrs.get('parent', None)
        parent_comment = CommentsModel.objects.filter(id=parent)
        if not parent_comment.exists():
            raise serializers.ValidationError(f"Parent {parent} does not exist")
        else:
            attrs['parent'] = parent_comment
        return attrs



    def get_me_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False

    def get_replies(self, obj):
        serializer = self.__class__(
            obj.child.all(), many=True, context=self.context)
        return serializer.data
