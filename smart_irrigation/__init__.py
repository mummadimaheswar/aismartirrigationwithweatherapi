"""
Smart Irrigation System - AI-Powered Decision Engine
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Smart Irrigation Team"

from . import data
from . import weather
from . import et
from . import models
from . import decision
from . import advisory

__all__ = ['data', 'weather', 'et', 'models', 'decision', 'advisory']