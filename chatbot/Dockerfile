FROM python:3.11-slim

WORKDIR /app 

COPY bot.py .

COPY htmlTemplates.py .

COPY requeriments.txt .

RUN pip3 install -r requeriments.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "bot.py", "--server.port=8501", "--server.address=0.0.0.0"]

