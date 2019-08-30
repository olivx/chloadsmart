sudo apt install gdal-bin libgdal-dev
sudo apt install python3-gdal
sudo apt install binutils libproj-dev


docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4


