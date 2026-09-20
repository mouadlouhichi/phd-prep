"""Swap the template's green palette for a blue one.

The green lives entirely in the code palette: the template's raster art
(illustrations, logos, thesis figures) was measured at 0% green, so no
image recolouring is needed.

Why this is a module and not a constant override in the builder: ten
functions in tpl.py / layouts.py take the green as a *default argument*
(rrect, rect, line, table, card, chip, arrow, kpi, ...). Default values
are evaluated when the def runs, i.e. at import time, so assigning
``tpl.GREEN = BLUE`` afterwards changes nothing for those shapes. This
rewrites the bound defaults as well as the module globals.

Call ``apply(tpl, layouts)`` before ``from layouts import *``.
"""

# old green -> new blue. Same tonal role, comparable lightness.
SWAP = {
    "124944": "0E3B5E",   # GREEN        deep teal  -> deep navy
    "1E5F58": "1F5C99",   # GREEN mid    (14 uses)  -> medium blue
    "E6EEEA": "E4EBF4",   # GREEN_SOFT   pale tint  -> pale blue tint
    "DCE7E3": "D6E2EF",   # pale green text on dark fills
    "CFDAD6": "C9D8E6",   # paler green text on dark fills
}

# v13: match the reference viva deck. Its slides reference the theme colour
# accent1 2,160 times, and accent1 is 4472C4, so that is "the same blue".
# The companions are the standard Office tints/shades of 4472C4, and the
# orange accent becomes a deep teal so the categorical trios
# (Explain/Scale/Guide, Regimes A/B/C, Users/Items/Contexts) stay separable.
SWAP_V13 = {
    "124944": "4472C4",   # GREEN      -> reference accent1
    "1E5F58": "2F5597",   # mid green  -> Accent1, Darker 25%
    "E6EEEA": "D9E2F3",   # GREEN_SOFT -> Accent1, Lighter 80%
    "DCE7E3": "D6E4F7",   # pale text on dark fills
    "CFDAD6": "BDD0EA",   # paler text on dark fills
    "DF8330": "1F7A8C",   # ORANGE     -> deep teal
}

# v14: v13 plus a white slide background. BG is a bound default of
# Deck.new_slide(bg=BG), so this has to go through apply(), not a constant.
SWAP_V14 = dict(SWAP_V13, **{"FEF8F3": "FFFFFF"})


def _sw(v):
    """Swap a colour literal, recursing into tuples/lists of them."""
    if isinstance(v, str):
        return SWAP.get(v.upper(), v)
    if isinstance(v, tuple):
        return tuple(_sw(x) for x in v)
    if isinstance(v, list):
        return [_sw(x) for x in v]
    return v


def _reblue_callable(fn):
    if getattr(fn, "__defaults__", None):
        fn.__defaults__ = tuple(_sw(x) for x in fn.__defaults__)
    if getattr(fn, "__kwdefaults__", None):
        fn.__kwdefaults__ = {k: _sw(x) for k, x in fn.__kwdefaults__.items()}


def apply(*mods, swap=None):
    """Rewrite palette literals in each module's globals and bound defaults."""
    global SWAP
    if swap is not None:
        SWAP = swap
    for m in mods:
        for name, val in list(vars(m).items()):
            new = _sw(val)
            if new is not val and new != val:
                setattr(m, name, new)
        for val in list(vars(m).values()):
            if callable(val) and getattr(val, "__module__", None) == m.__name__:
                _reblue_callable(val)
            if isinstance(val, type):
                for attr in list(vars(val).values()):
                    if callable(attr):
                        _reblue_callable(attr)
    return SWAP
