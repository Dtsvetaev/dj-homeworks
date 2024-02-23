from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):  # Игнорируем формы на удаление
                if form.cleaned_data.get('is_main', False):
                    main_count += 1
        if main_count != 1:
            raise ValidationError('Должен быть ровно один основной раздел')
        super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
        list_display = ['name']
