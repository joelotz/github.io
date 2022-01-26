---
Title: Importing a GPX Course into Garmin 245 Watch
Date: 2021-08-18
Tags: Garmin
Author: Joe
Keywords: Garmin, brouter, brouter-web, garmin 245
Version: BRouter-Web, 0.16.0, Garmin Express, 7.7.1.0
---

In this post I am documenting how I imported a defined run path into my Garmin 245 watch. This is nearly the opposite of my [earlier post](https://www.joelotz.com/blog/2021/importing-garmin-245-watch-gpx-file-into-openstreetmap-as-traces.html) where I exported a path (GPX Trace) out of the Garmin. Why do I want to do this? Say I have a specific run path I want to take or I’m hiking in a new area and want turn-by-turn directions on my wrist. This will do it.

## BRouter-Web

The first item you need to complete this mission is a GPX file representing the desired path. There are many places you can download a popular trail hike or run. The pro-version of www.alltrails.com let you do this or I believe the paid-version of www.strava.com does as well. Another option is to create your own custom path using a router. Again, several apps and websites offer this but the one I currently like is https://brouter.de/brouter-web/. I believe it stands for “Bike Router” but it has different settings to optimize the automatic routing. 

To make a “route” or “path” you click the pencil icon and start click on the map at waypoints. The web app will then route a path between the waypoints. In the example image below the flags are my waypoints and the pink line is the route. 

![route_01](/images/2021/route_01.png)

You can use BRouter for other use-cases as well. Like plan a drive route and import it into [OSMAnd](https://osmand.net/).

Once the route is made, click the “Export” button, name the route, select “GPX” format, and “Export route”.

![route_02](/images/2021/route_02.png)



### Garmin Connect

Now you have a GPX file with your planned route. Next you need to import that route into your Garmin watch. Open [Garmin Connect](https://connect.garmin.com/) and login. On the left-hand pane click “Training” and “Courses”. Then way down low in little print click “Import”.

![route_03](/images/2021/route_03.png)

This will bring up a standard file upload window. Select your GPX file. 

<img src="/images/2021/route_04.png" alt="route_04" style="zoom:50%;" />

It will ask you the course type. I’m not sure why this is important, but it probably has different available metrics. I checked and regardless of the “course type” I was able to access and use it in different activities. For example, if I saved it as “Trail Running” I could still use it in a Bike activity... so maybe it isn’t too important what you choose.

<img src="/images/2021/route_05.png" alt="route_05" style="zoom:50%;" />

Once the route/path/course - whatever you call it is imported, Connect will ask for some settings. Like if it is a loop you can go clockwise or counter, if it isn’t a loop you can tell it to go to the end and back, or just to the end. 

![route_06](/images/2021/route_06.png)

Once it’s saved you can also play around with some of the other features if you wish. Like if you are running for a specific time or want to define a pace strategy. 

![route_07](/images/2021/route_07.png)

When you are all done click “Send to Device”.  Assuming you’ve already have been using and syncing the watch, everything is installed and configured correctly - this will open the Garmin Express app and synchronize. All new data, including the course will be uploaded to the watch. 

<img src="/images/2021/route_08.png" alt="route_08" style="zoom:80%;" />

<img src="/images/2021/route_09.png" alt="route_09" style="zoom:50%;" />

When completed, on your watch when you select an activity, like Trail Run, you can select “Options” by pressing up and select “Courses”. Now select the name of your course. From there the GPS will lock on and you are given directions on your watch with a arrow. It will also buzz when there is a change in direction. 

![route_10](/images/2021/route_10.png)