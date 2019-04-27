# Hand Rolled Ad Blocker for Chromium Browsers

I started using Vivaldi, but its lack of a built-in ad blocker made it seem to be so much slower than Opera or Brave. Not wanting to use a 3rd party ad blocker, I was inspired to make my own after reading [this post by Adrian Stoll](https://www.adrianstoll.com/dyi-adblocker/)

To run this, download the files and run the Python script. You can install the required modules using the command below.

`pip install -r requirements.txt`
 

Then, simply go to [vivaldi://extensions](vivaldi://extensions) or [chrome://extensions/](chrome://extensions/), etc., turn on Developer mode, click Load unpacked, and choose the directory that you saved these files in. 

As long as you didn't get any errors, you should be good to go! Go vist a site with a ton of ads and notice the difference.

This is a work in progress, so please feel free to send me any feedback. This list of URLs that get fed into this is **~37K long** as of this writing, so it might break a few things. Whitelisting and a few other features will be worked on in the future (or feel free to contribute).

Thanks :)
