from django.forms import ModelForm, TextInput
from .models import Poll, EditPoll, DeletePoll, DeleteAll


class CreateForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['poll_question', 'poll_option1', 'poll_option2', 'poll_option3']
        widgets = {
            'poll_question': TextInput(attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Poll Question'}),
            'poll_option1': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 1'}),
            'poll_option2': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 2'}),
            'poll_option3': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 3'}),
        }


class EditForm(ModelForm):
    class Meta:
        model = EditPoll
        fields = ['poll_question', 'poll_option1', 'poll_option2', 'poll_option3']
        widgets = {
            'poll_question': TextInput(attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Enter Poll Question Again'}),
            'poll_option1': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 1 Again'}),
            'poll_option2': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 2 Again'}),
            'poll_option3': TextInput(attrs={
                'style': 'border-color: green;',
                'placeholder': 'Enter Option 3 Again'}),
        }


class DeleteForm(ModelForm):
    class Meta:
        model = DeletePoll
        fields = ['yes', 'no']


class DeleteAllForm(ModelForm):
    class Meta:
        model = DeleteAll
        fields = ['yes', 'no']
