from fastapi import FastAPI, UploadFile, File
app = FastAPI()
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        return {"message": "파일이 존재하지 않음"}
    else:
        upload_folder = "C:\minju\MySQL"
        file_path = f"{upload_folder}/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"filename": file.filename, "saved_path": file_path}