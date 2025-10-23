from fastapi import FastAPI
from worker import add

app = FastAPI()


@app.get("/add")
def run_task(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id, "status": "Task submitted"}
