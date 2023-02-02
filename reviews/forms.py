from django import forms

class MyForm(forms.Form):
    user_name = forms.CharField(label="Input Your Name :", max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Name too long",
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=500)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)