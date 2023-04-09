from django.contrib import admin
from .models import TrainingWay, Test, Variant, Question, Answer, TestResult, User, Form


class InlineQuestion(admin.StackedInline):
    model = Question


class InlineAnswer(admin.StackedInline):
    model = Answer


class InlineVariant(admin.StackedInline):
    model = Variant


@admin.register(TrainingWay)
class TrainingWayAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestaAdmin(admin.ModelAdmin):
    inlines = [InlineQuestion]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [InlineVariant ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_right')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    inlines = [InlineAnswer]
    list_display = ('get_test', 'get_is_right', 'date')

    @admin.display(description='right')
    def get_is_right(self, obj):
        answers = list(map(lambda x: x.is_right, obj.answers.all()))
        return round(answers.count(True) / len(answers), 2)

    @admin.display(description='test')
    def get_test(self, obj):
        return obj.answers.all()[0].question.test


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'date')


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('user', 'training_way')
