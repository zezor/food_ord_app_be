# import os
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ord_app_be.settings')

# app = get_wsgi_application()     # 👈 REQUIRED BY VERCEL
# handler = app                   # 👈 ALSO SAFE

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_ord_app_be.settings")

app = get_asgi_application()
handler = app  # REQUIRED for Vercel
