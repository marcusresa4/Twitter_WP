from django import forms

class TweetForm(forms.Form):
    text = forms.CharField(
        max_length=280,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insert tweet'
            }
        )
    )

    hashtag_in_tweet = forms.CharField(
        max_length=280,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-hashtag',
                'placeholder': 'Insert hashtag'
            }
        )
    )