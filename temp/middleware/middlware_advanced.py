from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from collections import defaultdict
from typing import Dict


app = FastAPI()


class MyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limit_records : Dict[str, float] = defaultdict(float)

        async def log_message(self, message :str):
            print (message)
        
        async def dispatch(self, request: Request, call_next):
            client_ip = request.client.host
            current_time = time.time()
            if current_time - self.rate_limit_records[client_ip] < 1:
                return Response (content= "rate limit exceeded", status_code=429)
            
            self.rate_limit_records[client_ip] = current_time
            path = request.url.path
            await self.log_message(f"Request to {path}")

            start_time = time.time()                                                        #processing request
            response = await call_next(request)
            process_time = time.time() - start_time

            custom_headers = {"X-process-time" : str(process_time)}                         #custom headers
            for header , value in custom_headers.items():
                response.headers.append(header, value)


            await self.log_message(f"Response for {path} took {process_time} seconds")


            return response



app.add_middleware(MyMiddleware)


@app.get("/")
async def main():
    return {"message" : "Hello"}