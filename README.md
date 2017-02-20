# Nest_Emoncms
Pyhon script to pull data from Nest thermstat API, push to emoncms for storage and visualization.

Before using, you'll need to register as a developer with Nest and create a product to obtain  your product ID and product secret.
Use this to obtain a PIN code and the PIN code to obtain an Auth token for the API.

Also, an emoncms account is needed to push for cloud storage at emoncms.org.  Alternatively, you can host your own emoncms server.

See below for more information:

https://emoncms.org/

https://openenergymonitor.org/

I run the script from /usr/local/bin as a cron job every 3 minutes, running it more frequently than once every few seconds may produce unexpected behavior.
