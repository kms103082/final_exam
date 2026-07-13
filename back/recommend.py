from fastapi import APIRouter
from model import UserInput
import json

recommend_router = APIRouter()
JSON_PATH = "./recommend.json"

@recommend_router.post("/recommend")
async def calculate_recommendation():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        user_data = UserInput.model_validate(raw_data)
        
        level = user_data.level
        method = user_data.method
        location = user_data.location
        requirement = user_data.requirement

        sport_result = "전 운동을 싫어해요"
        if method == "구기종목":
            if location == "실외":
                sport_result = "축구⚽" if requirement == "고강도" else "야구⚾"
            else:
                sport_result = "농구🏀" if requirement == "고강도" else "피구🤾"
        else:
            sport_result = "배드민턴 🏸"

        result_payload = {
            "level": level,
            "method": method,
            "location": location,
            "requirement": requirement,
            "recommended_sport": sport_result,
            "message": f"숙련도 {level} 단계에 맞춘 최적의 종목은 [{sport_result}]입니다."
        }

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(result_payload, f, ensure_ascii=False, indent=4)
            
        return {"status": "success"}
        
    except Exception as e:
        return {"status": "error", "detail": str(e)}