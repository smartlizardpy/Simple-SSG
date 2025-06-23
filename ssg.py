import os
import markdown
import json
from jinja2 import Template
import yaml
import sys
import shutil
# Load config
config = json.load(open("config.json"))

# Load template
with open("templates/blog/main.html") as f:
    template = Template(f.read())
with open("templates/blog/post.html") as f:
    blog = Template(f.read())

with open("templates/blog/page.html") as f:
    page = Template(f.read())
# Ensure output dir exists
os.makedirs("output", exist_ok=True)
def getmeta(file):
    with open(file) as f:
                md = f.read()
                # Extract front matter between --- and ---
                if md.startswith('---'):
                    end = md.find('---', 3)
                    if end != -1:
                        front_matter = md[3:end].strip()
                    else:
                        front_matter = ""
                else:
                    front_matter = ""

                # Parse YAML front matter if present
                if front_matter:
                    meta = yaml.safe_load(front_matter)
                    title = meta.get("title", "")
                    date = meta.get("date", "")
                    desc = meta.get("desc", "")

                    return title, date ,desc
def getblogposts():
    posts = []
    for filename in os.listdir("posts"):
        if filename.endswith(".md"):
            filepath = os.path.join("posts", filename)
            title, date, desc = getmeta(filepath)
            post = {
                "title": title,
                "date": date,
                "summary": desc,
                "url": f"../posts/{filename.replace('.md', '.html')}",
                "filepath": filepath
            }
            posts.append(post)
    return posts
                   



# Iterate over markdown files
for filename in os.listdir("pages"):
    if filename.endswith(".md"):
        filepath = os.path.join("pages", filename)
        if filename.startswith("index"):
            filepath = os.path.join("pages", filename)
            with open(filepath) as f:
                md = f.read()
                html_body = markdown.markdown('\n'.join(md.split('\n')[1:]))
                title = md.split('\n')[0].replace("#", "").strip()
                posts = getblogposts()
                
                rendered = template.render(title=title, content=html_body, posts=posts ,nav=config["navbar"], desc=config["author_Description"])

                outname = filename.replace(".md", ".html")
                with open(os.path.join("output", outname), "w") as outf:
                    outf.write(rendered)
        else:
            with open(filepath) as f:
                md = f.read()
                html_body = markdown.markdown('\n'.join(md.split('\n')[1:]))
                title = md.split('\n')[0].replace("#", "").strip()
                rendered = page.render(title=title, content=html_body, nav=config["navbar"])
                outname = filename.replace(".md", ".html")
                with open(os.path.join("output", outname), "w") as outf:
                    outf.write(rendered)
        posts = getblogposts()
        for post in posts:
             with open(post["filepath"]) as f:
                    md = f.read()
        for post in posts:
            with open(post["filepath"]) as f:
                md = f.read()
                title, date, desc = getmeta(post["filepath"])
                # Remove front matter between --- and ---
                if md.startswith('---'):
                    end = md.find('---', 3)
                    if end != -1:
                        md = md[end+3:].lstrip()
                html_body = markdown.markdown(md)
                rendered = blog.render(title=title, date=date, content=html_body, post=post)
                outname = os.path.basename(post["filepath"]).replace(".md", ".html")
                os.makedirs(os.path.join("output", "posts"), exist_ok=True)
                with open(os.path.join("output/posts", outname), "w") as outf:
                    outf.write(rendered)
                # Copy static files to output/static

                src_static = os.path.join(os.getcwd(), "static")
                dst_static = os.path.join("output", "static")
                if os.path.exists(src_static):
                    if os.path.exists(dst_static):
                        shutil.rmtree(dst_static)
                    shutil.copytree(src_static, dst_static)
           
