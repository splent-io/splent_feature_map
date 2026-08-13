"""
Functional tests for splent_feature_map.

The map has no pages of its own; it renders into the contact.map slot when
the product configures a place.
"""


def test_contact_page_embeds_the_configured_map(test_client):
    """The contact page carries the embed iframe when MAP_QUERY is set."""
    app = test_client.application
    if "contact" not in app.blueprints:
        return  # the product under test has no contact page to host the slot
    app.config["MAP_QUERY"] = "Escuela Tecnica Superior de Ingenieria Informatica"
    response = test_client.get("/contact")
    assert response.status_code == 200
    html = response.data.decode()
    assert "map-embed__frame" in html
    assert "output=embed" in html


def test_nothing_renders_without_a_place(test_client):
    app = test_client.application
    if "contact" not in app.blueprints:
        return
    for key in ("MAP_QUERY", "MAP_LAT", "MAP_LNG"):
        app.config[key] = ""
    response = test_client.get("/contact")
    assert response.status_code == 200
    assert "map-embed" not in response.data.decode()
