from jupyter/minimal-notebook:latest

WORKDIR /cards
COPY . .
RUN pip install .

WORKDIR /home/jovyan
COPY cards.ipynb .
