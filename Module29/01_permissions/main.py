import functools
from typing import Optional, Callable


# def check_permission(user_permissions: str) -> Callable:  # с обязательным параметром!
#     def super_wrapped(func: Callable) -> Callable:
#         @functools.wraps(func)
#         def wrapped(*args, **kwargs):
#             if user_permissions != 'admin':
#                 raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
#             result = func(*args, **kwargs)
#             return result
#         return wrapped
#     return super_wrapped
#
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
#
# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')


def check_permission(_func: Optional[Callable] = None, *, user_permissions: str = 'admin') -> Callable:
    def super_wrapped(func: Callable) -> Callable:  # с необязательным параметром!
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if user_permissions != 'admin':
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            result = func(*args, **kwargs)
            return result
        return wrapped
    if _func is None:
        return super_wrapped
    return super_wrapped(_func)


@check_permission
def delete_site():
    print('Удаляем сайт')


@check_permission(user_permissions='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
