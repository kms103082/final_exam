FROM python:latest

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port 8501 --server.address 0.0.0.0