import os

password = os.environ.get('POSTGRES_PASSWORD')

with open('/usr/local/lib/python3.10/site-packages/psycopg2/extensions.py', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'Convert a set of keywords into a connection strings.' in line:
            lines.insert(i+1, f'    kwargs[\'password\'] = \'{password}\'\n')
            break
    f.seek(0)
    f.write(''.join(lines))