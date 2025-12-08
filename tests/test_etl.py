import etl
import etl.transform
import inspect
print("etl __file__:", getattr(etl, "__file__", None))
print("etl.transform __file__:", getattr(etl.transform, "__file__", None))
print("etl.transform attrs:", dir(etl.transform))
print("source snippet:\n", inspect.getsource(etl.transform))

def test_summarize():
    out = transform.summarize()
    assert isinstance(out, dict)
    assert out["rows"] >= 0