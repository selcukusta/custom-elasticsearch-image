FROM frolvlad/alpine-python3
ADD . /app
WORKDIR app
RUN pip install --no-cache-dir -r requirements.txt
CMD python main.py