from django.views.generic import ListView
from django.db.models import Q
from .models import Book
from .forms import SearchSortForm

class BookList(ListView):
    model = Book
    paginate_by = 10
    template_name = 'catalog/book_list.html'

    SORT_MAP = {
        'new': ('-published_at','-id'),
        'old': ('published_at','id'),
        'title': ('title','id'),
        'author': ('author','id'),
    }

    def get_queryset(self):
        qs = Book.objects.all()
        self.form = SearchSortForm(self.request.GET or None)
        if self.form.is_valid():
            q = (self.form.cleaned_data.get('q') or '').strip()
            sort = self.form.cleaned_data.get('sort') or 'new'
            for w in [w for w in q.split() if w]:
                qs = qs.filter(
                    Q(title__icontains=w) |
                    Q(author__icontains=w) |
                    Q(genre__icontains=w) |
                    Q(summary__icontains=w)
                )
            qs = qs.order_by(*self.SORT_MAP.get(sort, self.SORT_MAP['new']))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = getattr(self,'form', SearchSortForm(self.request.GET or None))
        ctx['total_count'] = ctx['object_list'].count()
        qd = self.request.GET.copy(); qd.pop('page', True)  # 条件維持
        ctx['qparams'] = qd.urlencode()
        return ctx
