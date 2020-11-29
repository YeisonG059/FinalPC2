FROM jupyter/minimal-notebook

WORKDIR /jupyter-notebook

COPY app.py /jupyter-notebook
COPY requirementsNotebook.txt /jupyter-notebook

RUN pip install -r requirementsNotebook.txt
