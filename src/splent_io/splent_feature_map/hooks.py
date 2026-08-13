"""
Template hooks for splent_feature_map.

The map renders wherever a page leaves a slot for it. Today that is the
contact page (`contact.map`); any feature can open another slot and this
feature can register into it without either knowing the other's internals.

The provider is configuration, not markup: templates/map/embed.html decides
what to draw from MAP_PROVIDER, so a product moves from the Google embed to
OpenStreetMap (or whatever comes next) without touching a template.
"""

from flask import current_app, render_template

from splent_framework.hooks.template_hooks import register_template_hook


def contact_map():
    """The configured location, embedded under the contact form.

    Renders nothing when the product configures no place, so installing the
    feature without configuring it changes nothing.
    """
    cfg = current_app.config
    if not (cfg.get("MAP_QUERY") or (cfg.get("MAP_LAT") and cfg.get("MAP_LNG"))):
        return ""
    return render_template("map/embed.html")


register_template_hook("contact.map", contact_map)
