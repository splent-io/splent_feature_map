from splent_framework.blueprints.base_blueprint import create_blueprint

map_bp = create_blueprint(__name__)


def init_feature(app):
    from splent_framework.settings.settings_schema import register_settings

    # Admin-configurable behaviour (framework renders the panel from this
    # schema). Values fall back to the MAP_* environment variables the
    # feature declares in [tool.splent.config].
    register_settings(
        "map",
        "Map",
        [
            {
                "key": "provider",
                "type": "select",
                "default": "google",
                "label": "Provider",
                "options": [
                    ("google", "Google Maps"),
                    ("openstreetmap", "OpenStreetMap"),
                ],
                "help": "Google embeds a keyless place search and needs only the place. OpenStreetMap embeds by coordinates and needs latitude and longitude.",
            },
            {
                "key": "query",
                "type": "text",
                "default": "",
                "label": "Place",
                "help": "The place as the Google search understands it, e.g. an organisation name and city.",
            },
            {
                "key": "lat",
                "type": "text",
                "default": "",
                "label": "Latitude",
                "help": "Decimal degrees, used by the OpenStreetMap embed.",
            },
            {
                "key": "lng",
                "type": "text",
                "default": "",
                "label": "Longitude",
                "help": "Decimal degrees, used by the OpenStreetMap embed.",
            },
            {
                "key": "zoom",
                "type": "int",
                "default": "16",
                "label": "Zoom",
                "help": "Map zoom level. 16 shows a neighbourhood.",
            },
            {
                "key": "address",
                "type": "text",
                "default": "",
                "label": "Address line",
                "help": "Shown under the map. Empty shows none.",
            },
        ],
        icon="map-pin",
    )


def inject_context_vars(app):
    return {}
