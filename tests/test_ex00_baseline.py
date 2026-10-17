from exercises.ex00_baseline.runner import run_sequential


def test_returns_results_in_order():
    assert run_sequential(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


def test_empty_input_gives_empty_list():
    assert run_sequential(lambda x: x, []) == []


def test_calls_func_once_per_item_in_order():
    calls = []
    run_sequential(calls.append, ["a", "b", "c"])
    assert calls == ["a", "b", "c"]


def test_returns_a_list():
    assert isinstance(run_sequential(str, range(3)), list)
