from typing import Optional

from fastapi import FastAPI

import requests

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/museum")
def read_museum():
	r = requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&q=&facet=date_start&facet=date_end&facet=address_name&facet=address_zipcode&facet=address_city&facet=deaf&facet=price_type&facet=access_type&facet=updated_at&facet=programs')
	return r.json()

@app.get("/museum/{museum_id}")
def read_museum_by_id(museum_id: str):
	r = requests.get(f'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&q=&facet=date_start&facet=date_end&facet=address_name&facet=address_zipcode&facet=address_city&facet=deaf&facet=price_type&facet=access_type&facet=updated_at&facet=programs&refine.recordid={museum_id}')
	return r.json()
