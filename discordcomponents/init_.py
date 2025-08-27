# discord_components/__init__.py

from .http_patch import setup_http_patch
from .components import __all__ as _components

def setup(bot):
    # Monkey‐patch the internal HTTPClient.create_message
    setup_http_patch()
    # Add all component classes as bot.ComponentsV2
    bot.ComponentsV2 = {name: globals()[name] for name in _components}
