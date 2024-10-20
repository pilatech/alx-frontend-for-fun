#!/usr/bin/python3
"""Script that converts markdown to html"""


if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)

    content = ""
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            num = line.count('#')
            content += f"<h{num}>{line[num + 1:-1]}</h{num}>\n"

    with open(sys.argv[2], 'w') as file:
        file.write(content)
    sys.exit(0)
