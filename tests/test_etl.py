# tests/test_etl.py
# Import the function directly to avoid name/attribute issues

from etl.transform import summarize

def test_summarize():
    out = summarize()
    assert isinstance(out, dict)
    assert out["rows"] >= 0