import os

# Read the current settings
with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Check if imports are at the top
lines = content.split('\n')

# Find where imports should go
import_section_end = 0
for i, line in enumerate(lines):
    if not line.startswith(('import ', 'from ', '#', '"', "'")) and line.strip():
        import_section_end = i
        break

# Ensure dj_database_url is imported
if 'import dj_database_url' not in content:
    lines.insert(import_section_end, 'import dj_database_url')
    print("Added dj_database_url import")

# Write back
with open('amr_project/settings.py', 'w') as f:
    f.write('\n'.join(lines))

print("Settings file updated")
