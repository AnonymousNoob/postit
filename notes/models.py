from django.db import models
from django.utils import timezone


class Note(models.Model):

    title = models.CharField(max_length=100,blank=True,default="Title")
    content = models.TextField(blank=True,default="")
    created = models.DateTimeField(auto_now_add=True)

    def note_history(self):
        return NoteHistory.objects.filter(note=self).order_by('-version')

    def save(self, *args, **kwargs):

        super(Note, self).save(*args, **kwargs)
        # save note history
        note_history = self.note_history()
        if not note_history or self.content != note_history[0].content or self.title != note_history[0].title:
            newnote = NoteHistory(note=self, content=self.content,title = self.title)
            newnote.save()


    def __str__(self):
    	return self.title + self.content

    class Meta:
        ordering = ['-created']

class NoteHistory(models.Model):
    version = models.IntegerField(editable=False,blank=True,null=True)
    note = models.ForeignKey('Note',related_name = 'history',blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    title = models.CharField(max_length = 100,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('version', 'note',)
        ordering = ['-created']

    def save(self, *args, **kwargs):
        current_version = NoteHistory.objects.filter(note=self.note).order_by('-version')[:1]
        self.version = current_version[0].version + 1 if current_version else 1
        super(NoteHistory, self).save(*args, **kwargs)

