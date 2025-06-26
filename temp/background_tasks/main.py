from typing import Annotated
import time
from fastapi import BackgroundTasks, Depends, FastAPI


app = FastAPI()

# def write_notification(email: str, message=""):
#     with open ("log.txt", mode="w")as email_file:
#         content = f"notif for: {email}:{message}"
#         time.sleep(5)
#         email_file.write(content)


# @app.post("/send-notif/{email}", status_code=202, detail="accepted")
# async def send_notif(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notif")
#     return {"message" : "notif sent in background"}


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notif/{email}", status_code=202)
async def send_notif(
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "message sent", "query": q}
