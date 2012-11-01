User Tracking for VikeFans.com
=============

The VikeFans site is hosted on a fairly restricted domain, so we don't have the capability of updating 
the back end code to show which users were recently logged in.

This script is included in an iframe, the source of which includes a parameter that has the end users login
name.

When called, the user is added to an array of active users (no duplicates). 

If a login name is not present, the IP address is tracked as a lurker.

The script outputs a basic html page with a list of users logged in since the script started running.

The script will track users for as long as it is actively running.  This is typically a day because
there is no activity in the early hours of the morning.  Sometimes it will live for a few days.

The script runs on Google App Engine.

The code that does all the work is in Main.py.

It's placed here publicly so that it can be reviewed by anybody to ensure we are not doing anything 
nefarious with end user information.