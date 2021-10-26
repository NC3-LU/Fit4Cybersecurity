# -*- coding: utf-8 -*-

from django.contrib import admin

from survey.models import (
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyQuestionServiceCategory,
    SurveySection,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
    TranslationKey,
    SurveyUserFeedback,
)

from csskp.settings import HASH_KEY
from cryptography.fernet import Fernet


class InputFilter(admin.SimpleListFilter):
    template = "admin/find_user_by_hash.html"

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)


class FindUserByHashFilter(InputFilter):
    parameter_name = "user_id"
    title = "Find user by hash"

    def queryset(self, request, queryset):
        if self.value() is not None:
            crypter = Fernet(HASH_KEY)
            hash_user_id = self.value()[2:-1].encode("utf-8")
            user_id = str(crypter.decrypt(hash_user_id))

            return queryset.filter(user_id=user_id[2:-1])

    def choices(self, cl):
        return []


@admin.register(SurveyUser)
class SurveyUserAdmin(admin.ModelAdmin):
    list_filter = (FindUserByHashFilter,)
    list_display = [
        "id",
        "user_id",
        "status",
        "country_code",
        "choosen_lang",
        "created_at",
        "updated_at",
    ]


@admin.register(SurveyUserFeedback)
class SurveyUserFeedbackAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    list_display = ["id", "user", "feedback"]


@admin.register(TranslationKey)
class TranslationKeyAdmin(admin.ModelAdmin):
    list_filter = ["key"]
    list_display = ["key", "lang", "ttype", "text"]


admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAnswer)
admin.site.register(SurveyQuestionServiceCategory)
admin.site.register(SurveySection)
admin.site.register(SurveyUserAnswer)
admin.site.register(Recommendations)
