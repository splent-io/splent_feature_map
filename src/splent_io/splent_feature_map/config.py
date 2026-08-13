"""
map feature configuration.

Reads this feature's environment variables into Flask app.config, which is
what templates and services see. Every variable read here belongs under
[tool.splent.config] in pyproject.toml as well, with the same default.
"""

import os


def inject_config(app):
    app.config.update(
        {
            # Which embed the map renders. "google" needs only MAP_QUERY (a
            # free-text place search, no API key); "openstreetmap" needs
            # MAP_LAT and MAP_LNG. Swapping provider is a config change,
            # no template touches it.
            "MAP_PROVIDER": os.getenv("MAP_PROVIDER", "google").strip().lower(),
            # The place, as the provider's search understands it.
            "MAP_QUERY": os.getenv("MAP_QUERY", "").strip(),
            # Coordinates, for providers that embed by position.
            "MAP_LAT": os.getenv("MAP_LAT", "").strip(),
            "MAP_LNG": os.getenv("MAP_LNG", "").strip(),
            "MAP_ZOOM": os.getenv("MAP_ZOOM", "16").strip(),
            # The address line shown under the map. Empty shows none.
            "MAP_ADDRESS": os.getenv("MAP_ADDRESS", "").strip(),
        }
    )
