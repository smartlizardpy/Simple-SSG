# Simple SSG

Simple SSG is a lightweight static site generator written in Python. It transforms Markdown files into HTML pages using Jinja2 templates.

## Features

- Converts Markdown files from the `pages` and `posts` directories to HTML
- Supports YAML front matter for metadata (title, date, description)
- Utilizes Jinja2 templates for layouts and blog posts
- Copies static assets to the output directory
- Serves the generated site locally with an HTTP server

## Usage

1. **Install dependencies:**
    ```sh
    pip install markdown jinja2 pyyaml
    ```

2. **Prepare your content:**
    - Place Markdown files in the `pages` and `posts` folders.
    - Add your templates to the `templates/blog` directory.
    - Store static files (CSS, JS, images) in the `static` directory.
    - Configure site settings in `config.json`.

3. **Generate the site:**
    ```sh
    python ssg.py
    ```

4. **View your site:**
    - The generated site will be in the `output` directory and served at [http://localhost:8000](http://localhost:8000).

## Project Structure

```
.
├── config.json
├── pages/
├── posts/
├── static/
├── templates/
│   └── blog/
│       ├── main.html
│       ├── page.html
│       └── post.html
├── ssg.py
└── output/
```