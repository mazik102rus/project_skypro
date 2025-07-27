from src.decorators import log


def test_log_to_file_success(tmp_path):
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def sample_func():
        return "Success"

    sample_func()

    with open(filename) as f:
        content = f.read().strip()
    assert content == "sample_func ok"


def test_log_to_file_error(tmp_path):
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def sample_func():
        raise ValueError("Error")

    try:
        sample_func()
    except ValueError:
        pass

    with open(filename) as f:
        content = f.read().strip()
    assert content.startswith("sample_func error: ValueError. Inputs: (), {}")


def test_log_to_console_success(capsys):
    @log()
    def sample_func():
        return "Success"

    sample_func()
    captured = capsys.readouterr()
    assert captured.out.strip() == "sample_func ok"


def test_log_to_console_error(capsys):
    @log()
    def sample_func():
        raise TypeError("Error")

    try:
        sample_func()
    except TypeError:
        pass

    captured = capsys.readouterr()
    assert captured.out.strip().startswith("sample_func error: TypeError. Inputs: (), {}")


def test_log_with_arguments(tmp_path):
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    add(3, b=4)

    with open(filename) as f:
        lines = f.readlines()
    assert lines[0].strip() == "add ok"
    assert lines[1].strip() == "add ok"
