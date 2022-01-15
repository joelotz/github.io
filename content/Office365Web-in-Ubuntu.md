---
Title: Office365 Web Desktop on Ubunutu
Date: 2021-10-20
Tags: Ubuntu
Author: Joe
Keywords: Office365, Ubuntu 20.04, CSU, Colorado State University
---

My university provides Office 365 desktop and web for the students. Which is the least they could do with the amount of tuition we are paying! My class team collaboratively authors office files synced to our online accounts, so I want to use M$ but I also want to use my linux box. 

### Options

Many years ago, over a decade, I ran MS Office on a paid WINE instance named Codeweavers CrossOver. I see there is a free version named PlayOnLinux that looks very similar but is not so straightforward. I could also run Office “naively” in a VirtualMachine but I don’t want to start a VM every time I want an office app nor keep it running. So, the option I am going with is to run online apps. Being a little old school online apps seemed odd to me, but with Google Docs and so many other examples it is pretty common place. 

I can run Office from a browser but this is distracting to have tabs open and such, so I’m installing [Office365WebDesktop](https://snapcraft.io/install/office365webdesktop/ubuntu#install) to emulate a desktop app.

### Installation

1. First, install the desktop wrapper from [github](https://github.com/rafgui12/Office365WebDesktop), or more easily, as a snap.

![office_00](/images/2021/Office365_AA.png)

- You can see the wrapper is now installed. Run it to add your login credentials.

![garmin_03](/images/2021/Office365_00.png)

2. Select “Sign in”

![garmin_03](/images/2021/Office365_01.png)

3. Add your email address.

![garmin_03](/images/2021/Office365_02.png)

4. Add your password. For CSU this is your eID password.

![garmin_03](/images/2021/Office365_03.png)

5. You might as well save these credentials.

![garmin_03](/images/2021/Office365_04.png)

6. And as of Oct 01, 2021 you must have 2FA setup. So you will need to authorize with Duo. 

![garmin_03](/images/2021/Office365_05.png)

Now you have a convenient Ubuntu desktop web-app wrapper for MS Office 365. 





