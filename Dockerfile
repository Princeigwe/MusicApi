FROM python:3.8
ENV PYTHONUNBUFFERED=1

# creating the code directory in Docker 
RUN mkdir /code 
WORKDIR /code

RUN pip install --upgrade pip

# copy and install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system


# Copy project
COPY . /code/
