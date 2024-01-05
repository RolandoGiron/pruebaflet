FROM docker.io/library/python
WORKDIR /
COPY prueba1web.py  /
COPY requeriments.txt  /
RUN pip install -r /requeriments.txt
CMD ["python3", "/prueba1web.py"]
EXPOSE 8550