"""
Template hooks for splent_feature_map.

The map renders wherever a page leaves a slot for it. Today that is the
contact page (`contact.map`); any feature can open another slot and this
feature can register into it without either knowing the other's internals.

The provider is configuration, not markup: templates/map/embed.html decides
what to draw from the provider setting, so a product moves from the Google
embed to OpenStreetMap (or whatever comes next) without touching a template.
Behaviour comes from the framework's declarative settings schema
(get_config("map")): the admin panel wins, the MAP_* environment variables
are the fallback.
"""

from flask import render_template

from splent_framework.hooks.template_hooks import register_template_hook


def contact_map():
    """The configured location, embedded under the contact form.

    Renders nothing when the product configures no place, so installing the
    feature without configuring it changes nothing.
    """
    from splent_framework.settings.settings_schema import get_config

    cfg = get_config("map")
    if not (cfg.get("query") or (cfg.get("lat") and cfg.get("lng"))):
        return ""
    return render_template("map/embed.html", cfg=cfg)


register_template_hook("contact.map", contact_map)
