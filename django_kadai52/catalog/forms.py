from django import forms
class SearchSortForm(forms.Form):
    q = forms.CharField(label='キーワード', required=False, widget=forms.TextInput(attrs={'placeholder':'例: Python 東野圭吾'}))
    SORT_CHOICES = [('new','新着順'),('old','古い順'),('title','タイトル A→Z'),('author','著者 A→Z')]
    sort = forms.ChoiceField(label='並び順', required=False, choices=SORT_CHOICES, initial='new')
