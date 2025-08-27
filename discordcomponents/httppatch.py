# discord_components/http_patch.py

import discord
from discord.http import HTTPClient as _HTTPClient

_original = _HTTPClient.create_message

async def _patched_create_message(self, channel_id, data=None, **kwargs):
    if data and "components_v2" in data:
        comps = data.pop("components_v2")
        data.setdefault("flags", 0)
        data["flags"] |= (1 << 15)  # IS_COMPONENTS_V2
        data["components"] = [
            c.to_dict() if hasattr(c, "to_dict") else c
            for c in comps
        ]
    return await _original(self, channel_id, data=data, **kwargs)

def setup_http_patch():
    _HTTPClient.create_message = _patched_create_message
