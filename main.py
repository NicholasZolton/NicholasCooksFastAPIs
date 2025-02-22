import uvicorn

if __name__ == "__main__":
    # print the current os path
    print(f"Starting server...")
    uvicorn.run("nicholascooks.app:app", port=8000)
