from nose.tools import *
from app import app

app.config["TESTING"] = True
web = app.test_client()


def test_index():
    rv = web.get("/", follow_redirects=True)
    assert (rv.status_code, 200)

    rv = web.get("/game", follow_redirects=True)
    assert (rv.status_code, 200)
