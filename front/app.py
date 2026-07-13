import streamlit as st
import requests

st.title("🎯 나만의 운동 종목 추천 시스템")
st.markdown("---")

level = st.selectbox("1. 본인의 운동 숙련도를 골라주세요", ["초급", "중급", "상급"])
method = st.radio("2. 선호하는 종목 스타일을 골라주세요", ["구기종목", "라켓·기타종목"])
location = st.radio("3. 운동할 때 선호하는 환경을 골라주세요", ["실내", "실외"])
requirement = st.selectbox("4. 원하는 운동 강도를 골라주세요", ["고강도", "저강도"])

st.markdown("---")

if st.button("나에게 맞는 운동 종목 추천받기"):
    payload = {
        "method": method,
        "requirement": requirement,
        "location": location,
        "level": level
    }

    BACKEND_URL = "http://localhost:8000/recommend"
    
    with st.spinner("백엔드 서버(FastAPI)와 통신하여 추천 결과를 가져오는 중..."):
        try:
            response = requests.post(BACKEND_URL, json=payload, timeout=5)

            if response.status_code == 200:
                result_data = response.json()
                st.success("추천 결과가 도착했습니다!")
                st.metric(label="🎯 추천 운동 종목", value=result_data.get("recommended_sport"))
                st.info(result_data.get("message"))
            else:
                st.error(f"백엔드 서버 에러 (상태 코드: {response.status_code})")
                
        except requests.exceptions.RequestException as e:
            st.error(f"백엔드 서버와 연결할 수 없습니다. \n에러 내용: {e}")