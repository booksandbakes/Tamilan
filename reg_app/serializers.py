from rest_framework import serializers

from .models import publish,Userdata

class userdataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = publish
        fields = ('tittle', 'contend')
class createDateBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model=Userdata
       fields =('Username','Email','Password1','Password2','City')