FROM jupyter/scipy-notebook:4d19a9839c05

WORKDIR /home/jovyan

RUN rm -rf work

RUN conda install -c conda-forge\
 wordcloud=1.4.1\
 beautifulsoup4=4.6.0\
 lxml=4.2.1\
 sqlalchemy=1.2.8\
 psycopg2=2.7.5

RUN conda install flask=1.0.2


RUN git clone https://github.com/stanfordnlp/GloVe && \
 cd GloVe && \
 make

#RUN wget `an s3 url with my full repo`
