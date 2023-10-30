from sphinxcontrib.test_reports.functions import tr_link


def test_tr_link_option_not_in_need():
    """
    Return an empty string when the specified test option is missing from the need.
    """
    assert tr_link(app=None, need={}, needs={}, test_option="a", target_option="b") == ""

def test_tr_link_no_target_option_in_needs():
    """
    Return an empty list when the target option is missing in all items of needs.
    """
    assert tr_link(app=None, need={"a": "1"}, needs={"x": {"id": "123"}}, test_option="a", target_option="b") == []

def test_tr_link_no_match():
    """
    Returns an empty list when no matching value for the test option is found in any of the target options within needs.
    """
    assert tr_link(app=None, need={"a": "1"}, needs={"x": {"b": "2", "id": "123"}}, test_option="a", target_option="b") == []

def test_tr_link_match():
    """
    Returns a list of ids when there is a matching value in both need and needs.
    """
    assert tr_link(app=None, need={"a": "1"}, needs={"x": {"b": "1", "id": "123"}}, test_option="a", target_option="b") == ["123"]

def test_tr_link_none_or_empty():
    """
    'None' and empty string values are not considered as valid matches.
    """
    need = {"a": None, "b": ""}
    needs = {"x": {"c": None, "id": "111"}, "y": {"c": "valid", "id": "222"}, "z": {"c": "", "id": "333"}}
    assert tr_link(app=None, need=need, needs=needs, test_option="b", target_option="c") == []
    assert tr_link(app=None, need=need, needs=needs, test_option="a", target_option="c") == []
