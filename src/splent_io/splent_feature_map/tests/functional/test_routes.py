"""
Functional tests for splent_feature_map.

The feature exposes no routes of its own; the embed renders through the
contact.map slot (see test_hooks.py).
"""


def test_the_feature_claims_no_page(test_client):
    response = test_client.get("/map")
    assert response.status_code == 404
