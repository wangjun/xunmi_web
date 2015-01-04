import os
import sys
app_root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(app_root, 'beautifulsoup4-4.3.2'))
sys.path.insert(0, os.path.join(app_root, 'requests-2.5.1'))
import sae
from myapp import app

application = sae.create_wsgi_app(app)