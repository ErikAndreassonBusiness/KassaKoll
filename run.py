import uvicorn

if __name__ == "__main__":
  print("\n" + "=" * 45)
  print(" KassaKoll is running!")
  print(" Main App:   http://127.0.0.1:8000")
  print(" Swagger UI: http://127.0.0.1:8000/docs")
  print(" ReDoc:      http://127.0.0.1:8000/redoc")
  print("=" * 45 + "\n")

  uvicorn.run("app.server:app", host="127.0.0.1", port=8000, reload=True)