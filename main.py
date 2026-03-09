from fastapi import FastAPI, Request

app = FastAPI()

users_db = {}
next_id = 1
welcome_message= {"welxome " : "Ahmed"}

@app.post("/users", status_code=201)
async def create_user(request: Request):
    global next_id
    body = await request.json()
    new_user = {"id": next_id, "name": body["name"], "email": body["email"]}
    users_db[next_id] = new_user
    next_id += 1
    return new_user


@app.get("/users")
def get_users():
    return list(users_db.values())

@app.get("/")
def Welcome_Home():
    return (welcome_message)

@app.post("/admin")
def admin_home(name: str):
    if name == "Ahmedd":
        return True
    else:
        return False
