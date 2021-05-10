import logging
from .config import VCR
from logging import NullHandler

__version__ = "9.9.9"

logging.getLogger(__name__).addHandler(NullHandler())


default_vcr = VCR()
use_cassette = default_vcr.use_cassette
