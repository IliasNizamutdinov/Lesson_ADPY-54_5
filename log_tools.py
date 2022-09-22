from datetime import datetime

def track_log(log_patch):
    def _track_log(some_function):

        def function_log(*args, **kwargs):
            result = some_function(*args, **kwargs)
            if len(args) == 0:
                txt_arg = 'аргументов нет'
            else:
                txt_arg = f'аргументы: {args}'
            if len(kwargs) == 0:
                txt_kwargs = ''
            else:
                txt_kwargs = f', именованные аргументы: {kwargs}'

            with open(log_patch,'a',encoding = 'utf-8') as file:
                file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}; функция {some_function.__name__}, {txt_arg}{txt_kwargs}, вернула {result} \n')
            return result
        return function_log
    return _track_log