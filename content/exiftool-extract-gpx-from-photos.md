Title: Extract gpx Trace from Geotagged Photos
Date: 2020-06-11
Tags: Bash
Author: Joe
Keywords: pelican, pelican static site generator, ubuntu 20.4, x
Version: OS, Ubuntu 20.04 LTS, x
Status: draft

On an Android the photos taken from the Mapillary app are stored in the app data directory. 

Most likely you are storing the photos on an external SD Card, if so the storage location is: `SAMSUNG Android/Card/Android/data/app.mapillary/files/CAMERA2_0/<dirs>/`

Otherwise :`SAMSUNG Android/Phone/Android/data/app.mapillary/files/CAMERA2_0/<dirs>/`

A gpx file is automatically created by the Mapillary app and is stored in the directory under file name 

Photos are names in this format:
`2020_06_06_14_06_41_856_+0530.jpg`
YYY\_MM\_DD\_HH\_MM\_SS\_xxx\_UTCOffset
I thought xxx would be the subseconds but it does not match the subseconds data field.


Adding geotags to images 

- https://exiftool.org/geotag.html
- https://exiftool.org/geotag.html#Inverse%20Geotagging

Some useful options:

- if makes exiftool only process files with a gps tag,
- fileOrder allows processing in a forced order,
- d allows formatting the datatime string.

For example:
```bash
exiftool -if '$gpsdatetime' -fileOrder gpsdatetime -p ./gpx.fmt -d %Y-%m-%dT%H:%M:%SZ *JPG > output.gpx
```

`exiftool -s -G -a file.jpg`

- **-s** means instead of showing the "friendly" names  like "Create Date", show the names you need to use when you write  ExifTool commands. So instead of "Create Date" you see "CreateDate". 
- **-G** means also show the metadata Group to which the metadata tag belongs.
- **-a** means to show all tags, even if they are duplicates. 

This uses a custom format to create a csv of the subsecond creation date, latitude, and longitude of all photos.
`exiftool -p ./csv_original.fmt *.jpg > original.csv`

`exiftool -csv -filename -imagesize -gps:GPSLatitude -gps:GPSLongitude ./ > long.csv`

`exiftool -ee -n -p "$gpslatitude,$gpslongitude,$gpsdatestamp,$gpstimestamp,$gpsspeed" FILE > out.csv`

This uses a gps logfile (.gpx) and interpolates photos based on CreateDate or SubSecCreateDate?
`exiftool -geotag log.gpx *jpg` 
`exiftool -geotag log.gpx "-GeoTime<SubSecDateTimeOriginal" *jpg`