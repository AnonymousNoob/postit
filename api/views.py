from rest_framework.response import Response
from rest_framework import generics
from notes.models import Note,NoteHistory
from api.serializers import NoteSerializer,NoteHistorySerializer,NoteCreateUpdateSerializer


class NoteList(generics.ListCreateAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveDestroyAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	lookup_field = 'pk'
	

class NoteUpdate(generics.RetrieveUpdateAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteCreateUpdateSerializer
	lookup_field = 'pk'


class NoteCreate(generics.ListCreateAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteCreateUpdateSerializer


class NoteHistory(generics.RetrieveDestroyAPIView):
	queryset = NoteHistory.objects.all()
	serializer_class = NoteHistorySerializer
	lookup_field = 'pk'
