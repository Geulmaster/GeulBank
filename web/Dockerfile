FROM python:3
WORKDIR /GeulBank
COPY requirements.txt ./
ENV PYTHONPATH /GeulBank
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]