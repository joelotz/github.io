---
Title: Converting .heic image to .jpg with ImageMagick
Date: 2023-01-08
Tags: ImageMagick
Author: Joe
Keywords: convert heic, imagemagick, ubuntu
Version: Ubuntu, 22.04.01 LTS, ImageMagick, 7.1.0-39
---

This is a quick followup to my post [Building Imagemagick 7.1 with HEIC Support from Source](https://www.joelotz.com/blog/2022/building-imagemagick-71-with-heic-support-from-source.html). 

It’s been about 6 months since converted my Apple .heic images to .jpg and I forgotten what seemed so trivial at the time. I searched my blog posts, as being a repository of notes and actions is by far the main purpose of my blog, and I didn’t find anything so I had to Google it. So… time to write a quick post to remind myself the next time I forget.

```bash
magick Input.heic -quality 95% Output.jpg
```

Many on the inter-tubes say quality should be 90-95% because 100% is much larger file size with little benefit.

All the metadata and EXIF is carried over, you can check with:

```bash
identify -verbose Output.jpg
identify -verbose Output.jpg | grep "exif"
```

