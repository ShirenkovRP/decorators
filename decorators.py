from datetime import datetime


def log_decor(path):

    def decor(old_function):

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log = (f"дата и время вызова фун-ции-{datetime.now()}, имя фун-ции-{old_function.__name__}, "
                   f"параметры фун_ции-{args}, {kwargs}, возвращаемое значение = {result}")
            with open(path, "a", encoding="utf-8") as f:
                f.write(log + "\n")
            return result

        return new_function

    return decor
