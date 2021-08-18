---
Title: Importing Garmin 245 Watch GPX File into Openstreetmap as Traces
Date: 2021-06-10
Tags: OpenStreetMap(OSM), Garmin
Author: Joe
Keywords: Garmin 245, OpenStreetMap, OSM, GPX, gps
---

I have a Garmin 245 watch that I use for trail running. What I wanted to do was update/add trails in [OpenStreetMap](https://www.openstreetmap.org/) based on the gps data of where I ran. This post will document the procedures for downloading a [gpx file](https://en.wikipedia.org/wiki/GPS_Exchange_Format) file created by the Garmin watch and importing it into OpenStreetMap (OSM).

### Create GPX File

I'm not going to go to far into this first topic. I'm going to assume you know how to create and save an "activity" on your watch. For Garmin, [specifically my 245](https://www8.garmin.com/manuals/webhelp/forerunner245/EN-US/GUID-2AE86593-AC85-4368-907C-9C6EEE28FD11.html), I record my run. 

### Download GPX File from Garmin Connect

On your computer browse to [https://connect.garmin.com/](https://connect.garmin.com/) and sign into your account. Open the left-side panel and under the ‘Activities’ section select ‘All Activities’.

![garmin_01](/images/2021/garmin_01.png)

Select the “Activity” or the run that you want to export.

![garmin_02](/images/2021/garmin_02.png)

After opening the run you see a map and the trace. To download, click the gear icon in the upper-right and select “Export to GPX”. Save the file somewhere on your computer. 

![garmin_03](/images/2021/garmin_03.png)

#### Importing GPX into OSM

The easiest way to see the gpx file in OSM is to simply drag and drop the file. Open [OpenStreetMap](https://www.openstreetmap.org/) in your browser. Click the edit button which opens the iD Editor. 

![garmin_04](/images/2021/garmin_04.png)

From here, simply (and literally) drag the .gpx file into the browser window. The run will show as a pink trace. 

![garmin_05](/images/2021/garmin_05.png)

Another method is to upload the trace into the OSM database for everyone to view and use. From the iD Editor click on "GPS Traces". 

![garmin_06](/images/2021/garmin_06.png)

This will take you to the OSM Trace Upload page. Click “Upload a trace”

![garmin_07](/images/2021/garmin_07.png)

Then select your gpx file and enter the details as appropriate.

![garmin_08](/images/2021/garmin_08a.png)

After uploading, you'll need to wait 1-2 minutes, at the most, for the system to enter the trace into the database.

![garmin_09](/images/2021/garmin_09a.png)

Refresh the webpage and you'll see a list of all your uploaded traces. Select “Edit Map” to open the trace in OSM.

![garmin_10](/images/2021/garmin_10.png)

The results are the same as drag and dropping but now if someone turns on the GPS Trace layer they will see your traces. One thing you can do is draw over your gpx trace and create a path or trail. 

![garmin_11](/images/2021/garmin_11.png)