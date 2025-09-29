import re

# Read the current settings
with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Ensure dj_database_url is imported at the top
if 'import dj_database_url' not in content.split('\n')[:20]:
    # Find the first import section and add it there
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            continue
        elif line.strip() and not line.startswith('#'):
            # Insert dj_database_url import here
            lines.insert(i, 'import dj_database_url')
            break
    
    content = '\n'.join(lines)

# Write the fixed content back
with open('amr_project/settings.py', 'w') as f:
    f.write(content)

print("Settings file updated successfully!")
