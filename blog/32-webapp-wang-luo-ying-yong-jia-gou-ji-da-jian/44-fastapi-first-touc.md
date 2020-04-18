# FastAPI First Touch


## Hello World

```py

```


## Basic Validation: Request / Response Models

```py

```


## Bigger App: Project Layout with APIRouter

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
