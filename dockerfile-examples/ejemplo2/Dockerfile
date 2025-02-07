FROM httpd:2.4-alpine
RUN apk add git
WORKDIR ./web
RUN git clone https://github.com/Candiia/proyectoBarcelona.git .
RUN mv ./* /usr/local/apache2/htdocs/ 
#COPY index.html /usr/local/apache2/htdocs/