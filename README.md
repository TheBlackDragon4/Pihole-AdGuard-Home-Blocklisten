
# pihole-blocklists
Custom PiHole blocklists

I create this GitHub entry to share my new knowledge with you. 
Here I do not claim to be complete.

Here you can also find an overview of useful blocklists for the Pi-hole, which can be installed additionally. Under the descriptions you will find the URLs that must be included under blocklist. There is a good selection so that everyone can pick out what he needs.



## Standard blocklists for PiHole

https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
https://mirror1.malwaredomains.com/files/justdomains - does not work
https://sysctl.org/cameleon/hosts (ohne SSL)
https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist - does not work
https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://hosts-file.net/ad_servers.txt - does not work



## Advertisements

These advertising lists block any advertising on the vast majority of websites. 
This is at least the case for me on the sites I visit.

https://adaway.org/hosts.txt
https://v.firebog.net/hosts/AdguardDNS.txt
https://v.firebog.net/hosts/Admiral.txt
https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://v.firebog.net/hosts/Easylist.txt
https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts
https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts
https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts
https://raw.githubusercontent.com/w13d/adblockListABP-PiHole/master/Spotify.txt
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileAds.txt
https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileSpyware.txt
https://raw.githubusercontent.com/anudeepND/youtubeadsblacklist/master/domainlist.txt



## More exotic websites

With the help of this blocklist, some exotic advertising domains are blocked.
These providers are characterized by "Windows Needs Updates" pop-ups and unserious things

https://github.com/TheBlackDragon4/pihole-blocklisten/blob/main/Sonstiges/exotischer.txt



## FireTV Block Ads

Using this block list to block ads from an Amazon Fire TV Stick

https://github.com/TheBlackDragon4/Sonstiges/firetv.txt



## Tracking of different telemetry lists

https://v.firebog.net/hosts/Easyprivacy.txt
https://v.firebog.net/hosts/Prigent-Ads.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts
https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt
https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt
https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt


## Win10Telemetry

The Win10Telemetry list blocks the domains to which Windows 10 sends its data. It ensures that Microsoft receives less data about you. And without any noticeable restrictions. The list is provided by the YouTube channel SemperVideo.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry



## MS Office Telemetry

This list blocks the telemetry domains of Microsoft Office.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/MS-Office-Telemetry



## Samsung Telemetry

The Samsungblocklist blocks domains that are used to retrieve statistics, for example. It is therefore comparable with the Win10Telemetry list.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/samsung



## Suspicious pages

This block list is used to block suspicious pages that pretend to be another website or that have been detected with viruses.

https://www.technoy.de/lists/Suspicious.txt
https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts_without_controversies.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts
https://v.firebog.net/hosts/static/w3kbl.txt
https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt
https://someonewhocares.org/hosts/zero/hosts
https://raw.githubusercontent.com/vokins/yhosts/master/hosts
https://winhelp2002.mvps.org/hosts.txt
https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt
https://v.firebog.net/hosts/BillStearns.txt
https://hostsfile.org/Downloads/hosts.txt
https://www.joewein.net/dl/bl/dom-bl-base.txt
https://v.firebog.net/hosts/Kowabit.txt
https://adblock.mahakala.is
https://www.stopforumspam.com/downloads/toxic_domains_whole.txt
https://raw.githubusercontent.com/CamelCase11/UnifiedHosts/master/hosts.all
https://raw.githubusercontent.com/mitchellkrogza/Badd-Boyz-Hosts/master/hosts
https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list
https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt



## Fake streaming and debt collection

This blocklist blocks streaming services that supposedly provide movies after you have registered. A few days later, a payment demand follows with reference to debt collection companies. This is so legally but not tenable.

https://github.com/TheBlackDragon4/Sonstiges/fakestreaming.txt
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming



## Malware Blocklists

https://www.technoy.de/lists/malware2.txt
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malvertising/list.txt - does not work
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malware/list.txt - does not work
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomainlist.com/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt - does not work
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-justdomains/list.txt - does not work
https://raw.githubusercontent.com/hectorm/hmirror/master/data/ransomwaretracker.abuse.ch/list.txt - does not work
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt
https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt



## Ransomeware

https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt




## Streaming Blocklisten

The Streaming List blocks dubious streaming services, including subscription traps.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming



## Porno Blocklisten

https://github.com/TheBlackDragon4/Jugendschutz/porno.txt



## Fake-Science

Under the Fake Science list, websites of Predatory Publishers a.k.a Fake Science are blocked. Predatory publishing is a fraudulent business model used by certain open access publishers. 

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science



## CORONA Blocklisten

This blocklist blocks some pages that contain, for example, false information.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails



## Phishing-Angriffe

Phising is the attempt to obtain data by forging a registration page, for example. Known phishing domains are blocked with this list.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe
https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt
https://phishing.army/download/phishing_army_blocklist_extended.txt
http://phishing.mailscanner.info/phishing.bad.sites.conf
https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt



## Social media advertising block lists

https://github.com/TheBlackDragon4/Jugendschutz/porno.txt



# Whitelists 

https://www.technoy.de/lists/whitelist.txt
https://github.com/TheBlackDragon4/Whitelisten/fullwhitelist.txt



