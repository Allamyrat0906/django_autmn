from django import forms
from .models import ReviewsM

# class Reviews(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
#         "required": "Please enter your name",
#         "max_length": "your name must be at least 10 characters"
#     })
#     comment = forms.CharField(
#         label="Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Rating", max_value=10, min_value=1)


class FormReview(forms.ModelForm):
    class Meta:
        model = ReviewsM
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Please enter your name",
                "max_length": "your name must be at least 10 characters"
            }
        }
