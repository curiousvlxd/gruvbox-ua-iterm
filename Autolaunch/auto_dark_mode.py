#!/usr/bin/env python3.

"""Sets the Color Preset on all sessions and profiles when changed in the System Preferences"""

import asyncio
import iterm2

# This script works in the "basic" iTerm environment.

# The themes to use:
#   The options are (at time of writing):
#    - 'Dark Background'
#    - 'Tango Light'
#    - 'Smoooooth'
#    - 'Light Background'
#    - 'Pastel (Dark Background)'
#    - 'Solarized Dark'
#    - 'Tango Dark'
#    - 'Solarized Light'
THEME_DARK = "gruvbox-ua-dark"
THEME_LIGHT = "gruvbo-ua-light"


async def set_color_preset_on_all_profiles(connection, color_preset):
    profiles = await iterm2.PartialProfile.async_query(connection)
    for partial in profiles:
        # Fetch the full profile and then set the color color_preset in it.
        profile = await partial.async_get_full_profile()
        print(profile.all_properties)
        await profile.async_set_color_preset(color_preset)


async def set_color_preset_on_all_sessions(app, color_preset):
    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                profile = await session.async_get_profile()
                await profile.async_set_color_preset(color_preset)


async def get_preset_for_theme(connection, theme):
    """Updates the Color Preset for all profiles and across all sessions."""
    theme_to_use = THEME_DARK if "dark" in theme else THEME_LIGHT

    try:
        color_preset = await iterm2.ColorPreset.async_get(connection, theme_to_use)
    except:
        available_themes = await iterm2.ColorPreset.async_get_list(connection)
        print(
            f"Failed to set theme to '{theme_to_use}', available are: {available_themes}"
        )
        raise
    return color_preset


async def set_theme_everywhere(app, connection, cur_osx_theme):
    """Updates the Color Preset for all profiles and across all sessions."""
    color_preset = await get_preset_for_theme(connection, cur_osx_theme)
    await set_color_preset_on_all_profiles(connection, color_preset)
    await set_color_preset_on_all_sessions(app, color_preset)


async def main(connection):
    """Updates the current theme on load, and monitors os-level theme changes.

    Updates *all* sessions and profiles to match one of the given themes."""

    # First set the Color Preset when we load iTerm
    app = await iterm2.async_get_app(connection)
    initial_theme = await app.async_get_theme()
    await set_theme_everywhere(app, connection, initial_theme)

    # Now monitor for system-level events (e.g. manual System Preferences changes or
    # Automator-triggered changes) and update the Color Preset.
    async with iterm2.VariableMonitor(
        connection, iterm2.VariableScopes.APP, "effectiveTheme", None
    ) as mon:
        while True:
            # Block until theme changes
            theme = await mon.async_get()
            await set_theme_everywhere(app, connection, theme)


iterm2.run_forever(main)
