from rest_framework import serializers
from notes.models import Note,NoteHistory

# Note History Serializer 
class NoteHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = NoteHistory		

# Nested Object Serializer
class NoteSerializer(serializers.ModelSerializer):
	history = NoteHistorySerializer(many=True,required=False)
	class Meta:
		model = Note

#Current Version Serializer 
class NoteCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note

		