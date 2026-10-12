from .elements import create_air as create_air

__all__ = ["create_air"]

# !! Answer to the subject question !!
# (its really so i dont forger)
# This file is the package's gateway. It only decides which names exist in
# the 'alchemy' namespace: create_air is re-exported, create_earth is not,
# so 'alchemy.create_earth()' raises an AttributeError.
# Nothing is private: create_earth still lives in alchemy/elements.py and
# can be reached with 'alchemy.elements.create_earth()'
# __init__.py curates the package's top-level names, it doesn't enforce privacy
# :)
