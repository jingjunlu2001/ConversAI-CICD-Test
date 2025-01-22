from typing import Union
import uvicorn
import json
import base64
import os
from fastapi import FastAPI, UploadFile, File, HTTPException, Form, Depends
from pydantic import BaseModel
# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
# import io

app = FastAPI()

# ocr = PaddleOCR(use_angle_cls=True, lang='en')

# # 文件保存路径
# SAVE_DIR = "./saved_results"
# os.makedirs(SAVE_DIR, exist_ok=True)  # 确保保存目录存在


# class OCRRequest(BaseModel):
#     base64_image: str = None  # Base64 编码的图像数据
#     file_path: str = None  # 本地文件路径

@app.get("/")
async def read_root():
    return "ConversAI Backend Testing."


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/healthy")
async def healthy():
    return "Healthy"

@app.post("/items/")
async def create_item(item: Item):
    # The item parameter will automatically be parsed from the request body using the Item Pydantic model
    return {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}


# @app.post("/ocr/")
# async def extract_chat_messages(
#     file: UploadFile = File(None),  
#     base64_image: str = Form(None),
#     file_path: str = Form(None)
# ):
#     try:
#         # # 图像处理逻辑
#         # image = None

#         # # Process file upload
#         # if file:
#         #     contents = await file.read()
#         #     if not contents:
#         #         raise HTTPException(status_code=400, detail="Uploaded file is empty.")
#         #     image = Image.open(io.BytesIO(contents)).convert("RGB")

#         # # Process base64-encoded image
#         # elif base64_image:
#         #     try:
#         #         base64_data = base64.b64decode(base64_image)
#         #         image = Image.open(io.BytesIO(base64_data)).convert("RGB")
#         #     except Exception:
#         #         raise HTTPException(status_code=400, detail="Invalid base64 image data.")

#         # # Process file path
#         # elif file_path:
#         #     if not os.path.isfile(file_path):
#         #         raise HTTPException(status_code=400, detail="File path does not exist.")
#         #     image = Image.open(file_path).convert("RGB")

#         # # 如果未提供任何图像数据
#         # if image is None:
#         #     raise HTTPException(status_code=400, detail="No valid image data provided.")

#         # # 转换为 NumPy 数组
#         # image_np = np.array(image)

#         # # OCR 识别
#         # result = ocr.ocr(image_np)

#         # # 初始化分组逻辑
#         # messages = []
#         # current_message = {"text": "", "sender": None}
#         # prev_bottom = None
#         # prev_left = None

#         # for line in result[0]:
#         #     text = line[1][0]
#         #     confidence = line[1][1]
#         #     box = line[0]

#         #     # 获取文字块的位置信息
#         #     top = min(box[0][1], box[1][1])
#         #     bottom = max(box[2][1], box[3][1])
#         #     left = min(box[0][0], box[3][0])
#         #     right = max(box[1][0], box[2][0])
#         #     center_x = (left + right) / 2  # 中心点

#         #     # 判断是否属于同一个气泡
#         #     if prev_bottom is not None and (top - prev_bottom > 20 or abs(left - prev_left) > 50):
#         #         # 保存上一条消息
#         #         messages.append(current_message)
#         #         current_message = {"text": "", "sender": None}

#         #     # 根据水平位置判断发信人或收信人
#         #     sender = "friend" if center_x < image_np.shape[1] * 0.5 else "me"
#         #     if current_message["sender"] is None:
#         #         current_message["sender"] = sender

#         #     # 累加当前文字块内容
#         #     current_message["text"] += text + " "
#         #     prev_bottom = bottom
#         #     prev_left = left

#         # # 保存最后一条消息
#         # if current_message["text"].strip():
#         #     messages.append(current_message)

#         # # 保存为 JSON 文件
#         # json_file_path = os.path.join(SAVE_DIR, "chat_result.json")
#         # with open(json_file_path, "w", encoding="utf-8") as json_file:
#         #     json.dump({"success": True, "messages": messages}, json_file, ensure_ascii=False, indent=4)
            
#         # return {
#         #     "success": True,
#         #     "messages": messages,
#         #     "json_path": json_file_path
#         # }

#         return {
#             "success": True,
#             "messages": "Testing",
#             "json_path": "/None"
#         }
        
#     except Exception as e:
#         return {"success": False, "error": str(e)}
    

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
