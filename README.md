
# pihole-blocklists
Custom PiHole blocklists

I create this GitHub entry to share my new knowledge with you. 
Here I do not claim to be complete.

Here you can also find an overview of useful blocklists for the Pi-hole, which can be installed additionally. Under the descriptions you will find the URLs that must be included under blocklist. There is a good selection so that everyone can pick out what he needs.



## Standard blocklists for PiHole

https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts <br>
https://sysctl.org/cameleon/hosts (ohne SSL) <br>
https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt <br>
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt <br>


## Advertisements

These advertising lists block any advertising on the vast majority of websites. 
This is at least the case for me on the sites I visit.

https://adaway.org/hosts.txt <br>
https://v.firebog.net/hosts/AdguardDNS.txt <br>
https://v.firebog.net/hosts/Admiral.txt <br>
https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt <br>
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt <br>
https://v.firebog.net/hosts/Easylist.txt <br>
https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext <br>
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts <br>
https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts <br>
https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts <br> 
https://raw.githubusercontent.com/w13d/adblockListABP-PiHole/master/Spotify.txt <br>
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileAds.txt <br>
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileSpyware.txt <br>
https://raw.githubusercontent.com/anudeepND/youtubeadsblacklist/master/domainlist.txt <br>


## More exotic websites

With the help of this blocklist, some exotic advertising domains are blocked.
These providers are characterized by "Windows Needs Updates" pop-ups and unserious things

https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Sonstiges/exotischer.txt <br>


## FireTV Block Ads

Using this block list to block ads from an Amazon Fire TV Stick

https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Sonstiges/firetv.txt <br>


## Tracking of different telemetry lists

https://v.firebog.net/hosts/Easyprivacy.txt <br>
https://v.firebog.net/hosts/Prigent-Ads.txt <br>
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt <br>
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts <br>
https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt <br>
https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt <br>
https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt <br>
https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt <br>
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt <br>
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt <br>
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt <br>


## Win10Telemetry

The Win10Telemetry list blocks the domains to which Windows 10 sends its data. It ensures that Microsoft receives less data about you. And without any noticeable restrictions. The list is provided by the YouTube channel SemperVideo.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry <br>


## MS Office Telemetry

This list blocks the telemetry domains of Microsoft Office.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/MS-Office-Telemetry <br>


## Samsung Telemetry

The Samsungblocklist blocks domains that are used to retrieve statistics, for example. It is therefore comparable with the Win10Telemetry list.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/samsung <br>


## Suspicious pages

This block list is used to block suspicious pages that pretend to be another website or that have been detected with viruses.

https://www.technoy.de/lists/Suspicious.txt <br> 
https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts_without_controversies.txt <br>
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts <br>
https://v.firebog.net/hosts/static/w3kbl.txt <br>
https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt <br>
https://someonewhocares.org/hosts/zero/hosts <br>
https://raw.githubusercontent.com/vokins/yhosts/master/hosts <br>
https://winhelp2002.mvps.org/hosts.txt <br>
https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt <br>
https://v.firebog.net/hosts/BillStearns.txt <br>
https://hostsfile.org/Downloads/hosts.txt <br>
https://www.joewein.net/dl/bl/dom-bl-base.txt <br>
https://www.stopforumspam.com/downloads/toxic_domains_whole.txt <br>
https://raw.githubusercontent.com/CamelCase11/UnifiedHosts/master/hosts.all <br>
https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/hosts <br>
https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list <br>
https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt <br>


## Fake streaming and debt collection

This blocklist blocks streaming services that supposedly provide movies after you have registered. A few days later, a payment demand follows with reference to debt collection companies. This is so legally but not tenable.

https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Sonstiges/fakestreaming.txt <br>
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming <br>



## Malware Blocklists

https://www.technoy.de/lists/malware2.txt <br>
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware <br>
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomainlist.com/list.txt <br>
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt <br>
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt <br>
https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt <br>


## Ransomeware

https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt <br>


## Streaming Blocklisten

The Streaming List blocks dubious streaming services, including subscription traps.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming <br>


## Porno Blocklisten

https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Jugendschutz/porno.txt <br>


## Fake-Science

Under the Fake Science list, websites of Predatory Publishers a.k.a Fake Science are blocked. Predatory publishing is a fraudulent business model used by certain open access publishers. 

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science <br>


## CORONA Blocklisten

This blocklist blocks some pages that contain, for example, false information.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails <br>


## Phishing-Angriffe

Phising is the attempt to obtain data by forging a registration page, for example. Known phishing domains are blocked with this list.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe <br>
https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt <br>
https://phishing.army/download/phishing_army_blocklist_extended.txt <br>
https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt <br>


## Social media advertising block lists

https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Jugendschutz/porno.txt <br>


# Whitelists 

https://www.technoy.de/lists/whitelist.txt <br>
https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Whitelisten/fullwhitelist.txt <br>
https://raw.githubusercontent.com/TheBlackDragon4/pihole-blocklisten/main/Whitelisten/personalwhitelist.txt <br>


