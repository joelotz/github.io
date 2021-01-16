Title: Creating a Launch Shortcut for Anaconda on Ubuntu
Date: 2021-01-16
Tags: Ubuntu, Anaconda
Keywords: ubuntu 20.4, Anaconda, shortcut, launch
Version: OS, Ubuntu 20.04.01, Anaconda, 4.9.2, Python, 3.7



When you install Anaconda on Ubuntu, for some reason, it doesn’t create a launching shortcut. First, install per instructions: [https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/](https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/)

Next, create a desktop file in your applications directory.
```bash
gedit ~/.local/share/applications/anaconda.desktop
```
Enter this data, it's pretty straight forward.
```bash
[Desktop Entry]
Version=1.0
Type=Application
Name=Anaconda
Exec=/home/joe/anaconda3/bin/anaconda-navigator
Icon=/home/joe/anaconda3/lib/python3.7/site-packages/anaconda_navigator/app/icons/Icon1024.png
Terminal=false
```
The two important items are `Exec` and `Icon` paths. `Exec` is where anaconda was installed. More than likely you will only need to replace "joe" with your userpath. I recommend verifying the `Icons` path, for example you may be more up to date and are using python3.8. In which case your path would be slightly different. 

That's it! Now you can press Windows Key and activate the Application Launcher and start typing anaconda. You should see your shortcut there.
![anaconda-launcher](/images/2021/anaconda-launcher.png)