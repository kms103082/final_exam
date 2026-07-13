from fastapi import APIRouter
from model import UserInput

recommend_router = APIRouter()

@recommend_router.post("/recommend")
async def calculate_recommendation(user_data: UserInput):
    level = user_data.level
    method = user_data.method
    location = user_data.location
    requirement = user_data.requirement

    sport_result = "걷기"
    if method == "구기종목":
        if location == "실외":
            sport_result = "축구⚽" if requirement == "고강도" else "야구⚾"
        else:
            sport_result = "농구🏀" if requirement == "고강도" else "피구🤾"
    else:
        if location == "실내":
            sport_result = "배드민턴🏸" if requirement == "저강도" else "스쿼시🎾"
        else:
            sport_result = "테니스🎾"

    return {
        "recommended_sport": sport_result,
        "message": f"숙련도 [{level}] 단계에 맞춘 최적의 종목은 [{sport_result}]입니다."
    }