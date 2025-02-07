FROM node:20.18-alpine AS builder
RUN apk add git 
WORKDIR /web
RUN git clone https://github.com/alvarocastilla05/FilimuFy.git .
RUN npm install -g @angular/cli
RUN cd ./App-FilimuFy && npm install
RUN cd ./App-FilimuFy && ng build --configuration production --aot

FROM nginx:alpine
WORKDIR /web
COPY --from=builder /web/App-FilimuFy/dist/app-watch-now/* .
RUN mv ./* /usr/share/nginx/html 