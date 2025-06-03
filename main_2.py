from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import dash
from dash import html

app = FastAPI()

dash_app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

dash_app.layout = html.Div([
    html.H1("Tableau de bord avec Dash"),
    html.P("Dash fonctionne dans FastAPI 🎉")
])

app.mount("/dashboard", WSGIMiddleware(dash_app.server))

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API FastAPI"}
