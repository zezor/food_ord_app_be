# import os
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ord_app_be.settings')

# app = get_wsgi_application()     # 👈 REQUIRED BY VERCEL
# handler = app                   # 👈 ALSO SAFE

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_ord_app_be.settings")

app = get_wsgi_application()
handler = app   # 👈 THIS LINE IS THE FIX
