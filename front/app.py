import streamlit as st
import json
import time

st.title("나만의 운동 종목 추천 시스템")
st.markdown("---")

JSON_PATH = "./recommend.json"

level = st.selectbox("1. 본인의 운동 숙련도를 골라주세요", ["초급", "중급", "상급"])
method = st.radio("2. 선호하는 종목 스타일을 골라주세요", ["구기종목", "라켓·기타종목"])
location = st.radio("3. 운동할 때 선호하는 환경을 골라주세요", ["실내", "실외"])
requirement = st.selectbox("4. 원하는 운동 강도를 골라주세요", ["고강도", "저강도"])

st.markdown("---")

if st.button("나에게 맞는 운동 종목 추천받기"):
    input_data = {
        "level" : level,
        "method" : method,
        "location" : location,
        "requirement" : requirement,
        "recommend_sport" : None,
        "message" : None
    }
    
    try:
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(input_data, f, ensure_ascii=False, indent=4)

        result_data = {}
        with st.spinner("백엔드 서버에서 추천 종목을 계산 중입니다..."):
            for _ in range(6):
                time.sleep(0.5)
                try:
                    with open(JSON_PATH, "r", encoding="utf-8") as f:
                        temp_data = json.load(f)
                        if temp_data.get("recommended_sport") is not None:
                            result_data = temp_data
                            break
                except Exception:
                    continue

        if result_data.get("recommended_sport"):
            st.success("추천 결과 분석이 완료되었습니다")
            st.metric(label="추천 종목", value=result_data.get("recommended_sport"))
            st.info(f"가이드 메시지: {result_data.get('message')}")
        else:
            st.error("응답을 받지 못했습니다. 다시 시도해주세요.")
            
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")