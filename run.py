import uvicorn

if __name__ == "__main__":
    print("\n" + "=" * 45)
    print(" KassaKoll is running!")
    print(" Main App:   http://localhost:5001")
    print(" Swagger UI: http://localhost:5001/docs")
    print(" ReDoc:      http://localhost:5001/redoc")
    print("=" * 45 + "\n")

    uvicorn.run("app.server:app", host="127.0.0.1", port=5001, reload=True)