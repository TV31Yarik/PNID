from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

RATES = {"USD": 1.0, "EUR": 0.85, "PLN": 3.62, "UAH": 43.95}

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"rates": RATES} 
    )

@app.post("/")
def convert(request: Request, amount: float = Form(...), from_curr: str = Form(...), to_curr: str = Form(...)):
    result = (amount / RATES[from_curr]) * RATES[to_curr]
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "result": round(result, 2),
            "amount": amount,
            "from_curr": from_curr,
            "to_curr": to_curr,
            "rates": RATES
        }
    )