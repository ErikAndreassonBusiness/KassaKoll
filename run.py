# Responsibility: Application entry point

import uvicorn
if __name__ == "__main__":
    print("\033[93m" + " Running on: http://127.0.0.1:5001")
    uvicorn.run("app.server.main:app", host="127.0.0.1", port=5001, reload=True)