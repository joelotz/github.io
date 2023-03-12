---
Title: OSM tags and method for mapping running track
Date: 2023-03-12
Tags: OpenStreetMap(OSM)
Author: Joe
Keywords: OSM, openstreetmap, running track, long jump
Version: Ubuntu, 22.04.02 LTS, JOSM, 
---

I recently tried to map a running track at a local high school and forgotten most of the tags and methods which required some research to remind myself again. I know I’ve done this before so wanted to write it down for next time. I didn’t think my [scratchpad/user page](https://wiki.openstreetmap.org/wiki/User:BubbleGuppies) on the [OSM Wiki ](https://wiki.openstreetmap.org/wiki/Main_Page) was sufficient. 

![By Martinvl - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=11628422](/images/2023/2880px-Piste_athlétisme-en.svg.png)

I'm most often mapping in high school track and field areas/stadiums. 

### Track

Creating multipolygon relation in JOSM = [https://blog.mapbox.com/mapping-complex-features-in-josm-using-relations-b930a6aec2c7](https://blog.mapbox.com/mapping-complex-features-in-josm-using-relations-b930a6aec2c7)

Track Wikipage = [https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dtrack](https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dtrack)
```bash
leisure=track
sport=athletics
athletics=running
lanes=*
```

### Long Jump Track and Pit

Long Jump Wikipage = [https://wiki.openstreetmap.org/wiki/Tag:athletics%3Dlong_jump](https://wiki.openstreetmap.org/wiki/Tag:athletics%3Dlong_jump)

Map the track with an area and tag as:
```bash
leisure=track
sport=athletics
athletics=long_jump
surface=tartan
lanes=1
area=yes
oneway=no (two pits)
```
Map the pit(s) with an area and tag as:
```bash
leisure=pitch
sport=athletics
athletics=long_jump
surface=sand
```