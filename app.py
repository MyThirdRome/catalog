from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Configuration
BASE_DIR = os.path.abspath("data/classified")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Fashion Catalogue</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        .breadcrumb { margin-bottom: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }
        .card { border: 1px solid #ddd; padding: 10px; border-radius: 5px; text-align: center; }
        .card img { max-width: 100%; height: auto; }
        .folder { background: #f9f9f9; padding: 20px; text-align: center; border: 1px solid #eee; cursor: pointer; }
        .folder a { text-decoration: none; color: #333; font-weight: bold; font-size: 1.2em; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="breadcrumb">
        <a href="/">Home</a> 
        {% for part in path_parts %}
            / <a href="/browse/{{ part.path }}">{{ part.name }}</a>
        {% endfor %}
    </div>

    <h1>{{ title }}</h1>

    <div class="grid">
        {% for item in items %}
            {% if item.type == 'folder' %}
                <div class="folder">
                    <a href="/browse/{{ current_path }}/{{ item.name }}">{{ item.name }}</a>
                </div>
            {% else %}
                <div class="card">
                    <img src="/image/{{ current_path }}/{{ item.name }}" loading="lazy">
                    <p>{{ item.name }}</p>
                </div>
            {% endif %}
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return browse("")

@app.route('/browse/', defaults={'subpath': ''})
@app.route('/browse/<path:subpath>')
def browse(subpath):
    # Security check to prevent directory traversal
    if '..' in subpath:
        return "Invalid path", 400
        
    abs_path = os.path.join(BASE_DIR, subpath)
    
    if not os.path.exists(abs_path):
        return "Path not found (Did you run the classification script?)", 404

    items = []
    try:
        with os.scandir(abs_path) as it:
            for entry in it:
                if entry.is_dir():
                    items.append({'name': entry.name, 'type': 'folder'})
                elif entry.is_file() and entry.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    items.append({'name': entry.name, 'type': 'file'})
    except OSError as e:
        return str(e), 500

    # Sort: folders first, then files
    items.sort(key=lambda x: (x['type'] != 'folder', x['name']))

    # Breadcrumbs
    path_parts = []
    current = ""
    if subpath:
        for part in subpath.strip('/').split('/'):
            current = f"{current}/{part}" if current else part
            path_parts.append({'name': part, 'path': current})

    return render_template_string(HTML_TEMPLATE, 
                                  items=items, 
                                  current_path=subpath.strip('/'), 
                                  title=subpath if subpath else "Catalogue Root",
                                  path_parts=path_parts)

@app.route('/image/<path:filepath>')
def serve_image(filepath):
    return send_from_directory(BASE_DIR, filepath)

if __name__ == '__main__':
    # Run on 0.0.0.0 to be accessible externally if needed (be careful with security)
    app.run(host='0.0.0.0', port=5000)
