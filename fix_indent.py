import os

with open('photoprompt/settings.py', 'r') as f:
    content = f.read()

# Purana kharab code hatana
if '# -- Added by Hacker Script --' in content:
    content = content.split('# -- Added by Hacker Script --')[0]

# Ekdum fresh aur clean code lagana (Bina allauth ke)
clean_code = """# -- Added by Hacker Script --
import os
from pathlib import Path

if 'store' not in INSTALLED_APPS:
    INSTALLED_APPS += ['store', 'crispy_forms', 'bootstrap5']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
"""

with open('photoprompt/settings.py', 'w') as f:
    f.write(content + clean_code)

print("✅ Settings.py ekdum fresh aur error-free ho gaya!")
