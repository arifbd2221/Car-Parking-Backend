# Car-Parking-Backend

This application is based django rest framework.  
This applicaion has several rest endpoints  that works on GET/POST request
From any client site if there is a call to the rest endpoint then this application
will response accordingly. This application has customised django admin site.
Admin can register a parking plot into the system.
By providing necessary information and pick the parking plot location
from the map, admin registers a parking plot.    

This application is now live on pythonanywhere server

Endpoint.... 
 
http://arifdiu.pythonanywhere.com/slots/

when an application invoke this url will consume all the slots information that are available
in the system.


http://arifdiu.pythonanywhere.com/slots/1(random id)

This is parameterized url to see a particular slot.  

http://arifdiu.pythonanywhere.com/booking/

This url return all the booking records that are exists in the system

http://arifdiu.pythonanywhere.com/booking/1233(random booking id)

This is parameterized url to see a particular booking details. 


   
