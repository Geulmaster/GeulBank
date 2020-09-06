FROM python:3
WORKDIR /usr/src/GeulBank
COPY requirements.txt ./
RUN export PYTHONPATH=$PYTHONPATH:/usr/src/GeulBank
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]