from rest_framework import serializers
from ...models import Post,Category
from accounts.models import Profile

# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializers(serializers.ModelSerializer):
    snipet = serializers.ReadOnlyField(source='get_snippet')
    url = serializers.SerializerMethodField()



    class Meta:
        model = Post
        fields = ["id","title","image","category","content","snipet","status","category",'published_date','url']
        read_only_fields = ['author']

    def get_url(self,obj):
        return "test"
    
    def to_representation(self, instance):
        request = self.context.get('request')
        # print(request.__dict__)
        rep = super().to_representation(instance)
        
        rep['state']="list"
        
        if request.parser_context.get('kwargs').get('pk'):
            rep['state']= "single"
        
        rep["category"]= CategorySerializers(instance.category,context={'request':request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)