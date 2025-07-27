import functools
from typing import Any, Callable, Optional, TextIO


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования выполнения функций."""

    def write_log(message: str, file: Optional[TextIO] = None) -> None:
        """Пишет лог в файл или выводит в консоль."""
        if file:
            file.write(message + '\n')
        else:
            print(message)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        write_log(log_message, f)
                else:
                    write_log(log_message)

        return wrapper

    return decorator
