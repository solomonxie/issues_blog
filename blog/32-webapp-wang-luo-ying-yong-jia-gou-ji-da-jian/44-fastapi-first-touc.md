# FastAPI First Touch


## Hello World

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

How to run:
```sh
$ uvicorn main:app --reload
```

## Basic Validation: Request / Response Models

```py

```


## Bigger App: Project Layout with APIRouter

Refer to Bigger Applications - Multiple Files: https://fastapi.tiangolo.com/tutorial/bigger-applications

```
project/
    - application/
        - app.py
    - models/
        - request_models.py
    - middlewares/
    - routers
        - myrouter.py
```


## Middleware

The Starlette middleware deals with both Request / Response at the same `dispatch()` function, which matches the `before_request` and `after_request` functions of Flask middleware.

Refer to: https://fastapi.tiangolo.com/tutorial/middleware/
Refer to: https://www.starlette.io/middleware/#basehttpmiddleware

```py
#application/middlewares/demo.py

from logging import getLogger
from starlette.middleware.base import BaseHTTPMiddleware

logger = getLogger(__name__)

class DemoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.critical('[MID] Recieved request in DemoMiddleware...')
        response = await call_next(request)
        logger.critical('[MID] Got respoonse in DemoMiddleware...')
        response.headers['X-my-demo-header'] = 'Example'
        return response
```

```py
#application/app.py

from fastapi import FastAPI
from application.routers import myrouter
from application.middlewares.log import DemoMiddleware

def create_app(*args, **kwargs):
    app = FastAPI(debug=True, title='aa-atq-service')
    # Middlewares
    app.add_middleware(DemoMiddleware)
    # Routers
    app.include_router(myrouter.router)
    return app

app = create_app()
```

## Handling Post Request Body

```py
import json

@app.post('/endpoint')
def endpoint(body: PostBody):
    payload = body.dict()
    assert json.loads(body.json()) == payload
```

## Directly Using Request Object

```py
@app.post('/endpoint')
def endpoint(request: Request):
    headers = request.headers
    print(headers.get('Content-Type'))
```

## Directly Using Response Object

```py

```
