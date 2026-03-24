from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse   # 👈 ADD THIS

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f"Server received: {message}")
    except WebSocketDisconnect:
        print("Client disconnected")

# 👇 ADD THIS PART (DO NOT REMOVE ABOVE CODE)
@app.get("/")
def get():
    with open("client.html") as f:
        return HTMLResponse(f.read())