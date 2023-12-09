from django.contrib.auth.decorators import user_passes_test


def group_required(*groups):
    """Проверка принадлежности пользователя к указанным группам"""

    def check_user_groups(user):
        if bool(user.groups.filter(name__in=groups)):
            return True
        return False

    return user_passes_test(check_user_groups)