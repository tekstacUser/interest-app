from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/calculate")
def calculate(
        request: Request,
        principal: float = Form(...),
        rate: float = Form(...),
        time: float = Form(...)
    ):
    interest = (principal * rate * time) / 100
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "principal": principal,
            "rate": rate,
            "time": time,
            "interest": interest
        }
    )