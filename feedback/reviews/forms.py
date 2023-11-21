from django import forms


class Reviews(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
        "required": "Please enter your name",
        "max_length": "your name must be at least 10 characters"
    })
    comment = forms.CharField(
        label="Feedback", max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", max_value=10, min_value=1)
