from django import forms
from .models import Post, Comment, Email

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        '''widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }'''


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        '''widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }'''

#Email Form in About

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('name','email',)
