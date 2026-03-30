from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Jay Vishnu",
        "title": "Vindago is awesome",
        "content": "Best companu to work with",
        "date_posted": "April 3, 2026"
    },
    {
        "id": 2,
        "author": "Abhinav Sosa",
        "title": "Vindago Is fun to work with",
        "content": "Fun Starup",
        "date_posted": "April 3, 2026"
    },
    {
        "id": 3,
        "author": "Rakshitha",
        "title": "Vindago helped me",
        "content": "Vindago helped me understand how to be a Frontend developer",
        "date_posted": "April 4, 2026"
    }
]

@app.get("/",include_in_schema=False)
@app.get("/api/posts",include_in_schema=False)

def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"Home"})

@app.get("/api/posts")
def get_posts():
    return 