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
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insert hashtags'
            }
        )
    )

class EditTweetForm(forms.Form):
    edit_text = forms.CharField(
        max_length=280,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insert new tweet'
            }
        )
    )
    edit_hashtag_in_tweet = forms.CharField(
        max_length=280,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insert new hashtags'
            }
        )
    )