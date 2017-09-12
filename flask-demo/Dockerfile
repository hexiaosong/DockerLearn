FROM python:2.7

# Add and install Python mudules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Add Resource
ADD . /src

# Expose
EXPOSE 5000

#Run
CMD ["python", "/src/application.py"]

