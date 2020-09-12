import crafatar
import pytest


# First Test - Check if crafatar.CrafatarAPIWrapper() is instantiable
def is_Crafatar_Instanced():
    '''
    Check if crafatar.CrafatarAPIWrapper() is instantiable
    '''
    assert crafatar.CrafatarAPIWrapper() is not None

