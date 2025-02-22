from nicholascooks.app import app
from mangum import Mangum
import os
import sys

sys.path.append(os.path.abspath("."))
handler = Mangum(app=app)
