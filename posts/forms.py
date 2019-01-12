from django import forms

from posts.models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    photo = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ('title', 'photo')
