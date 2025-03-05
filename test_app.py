def test_app_exists():
    import os
    assert os.path.exists('app.py'), "app.py not found"
