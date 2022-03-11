
# pihole-blocklisten
Eigene PiHole-Blocklisten

Diesen GitHub Eintrag erstelle ich, um meine neuen Kenntnisse mit euch zu teilen. 
Hier erhebe ich keine Anspruch auf Vollständigkeit.

Hier findet sich außerdem eine Übersichliche Auflistung nützlicher Blocklisten für den Pi-hole, die noch zusätzlich installiert werden können. Unter den Beschreibungen finden sich die URLs die Unter Blocklist eingebunden werden muss. Es gibt eine gute Auswahl sodass sich jeder das herrausuchen kann, was er benötigt.



## Standard Blocklisten für PiHole

https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
https://mirror1.malwaredomains.com/files/justdomains
https://sysctl.org/cameleon/hosts (ohne SSL)
https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist 
https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://hosts-file.net/ad_servers.txt



## Werbungen

Diese Werbelisten sperren soweit jegliche Werbung auf den allermeisten Websites. 
Ist zu mindest bei mir auf meinen besuchten Seiten erfolgt.

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



## Exotischere Webseiten

Mithilfe dieser Blockliste werden einige exotischern Werbe Domains blockiert.
Diese Anbieter zeichnen sich durch "Windows Needs Updates" Popups und Unseriösen dingen aus

https://github.com/TheBlackDragon4/Sonstiges/exotischer.txt



## FireTV Werbung Blockieren

Mithilfe dieser Blockliste werden Werbungen von einem Amazon Fire TV Stick blockiert

https://github.com/TheBlackDragon4/Sonstiges/firetv.txt



## Tracking von verschiedenen Telemetry Listen

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

Die Win10Telemetry Liste sperrt die Domains an die Windows 10 ihre Daten sendet. Sie sorgt dafür das Microsoft weniger Daten über Sie erhält. Und das Ohne spürbare Einschränkungen. Die Liste wird von dem YouTube Kanal SemperVideo zur Verfügung gestellt.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry



## MS Office Telemetry

Diese Liste Blockt die Telemetrie Domains von Microsoft Office.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/MS-Office-Telemetry



## Samsung Telemetry

Die Samsungblocklist blockt Domains über die z.B. Statistiken abgerufen werden. Sie ist also mit der Win10Telemetry Liste zu vergleichen.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/samsung



## Verdächtige Seiten

Mit dieser Blockliste werden Verdächtige Seiten Blockiert, die vorgeben eine andere Webseite zu sein, oder welche bei der Viren entdeckt wurden.

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



## Fake Streaming und Inkasso

Diese Blocklist sperrt Streaming Dienste die vermeindlich Filme zur verfügung stellen nach dem man sich regestriert hat. Einige Tage später folgt eine Zahlungforderung mit verweis auf Inkasso Unternehmen. Diese ist so rechtlich aber nicht haltbar.

https://github.com/TheBlackDragon4/Sonstiges/fakestreaming.txt
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming



## Malware Blocklisten

https://www.technoy.de/lists/malware2.txt
https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malvertising/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/disconnect.me-malware/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomainlist.com/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-justdomains/list.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/ransomwaretracker.abuse.ch/list.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
https://raw.githubusercontent.com/hectorm/hmirror/master/data/malwaredomains.com-immortaldomains/list.txt
https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt



## Ransomeware

https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt




## Streaming Blocklisten

Die Streaming Liste sperrt unseriöse Streaming-Diensten, inkl. Abo-Falle.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Streaming



## Porno Blocklisten

https://github.com/TheBlackDragon4/Jugendschutz/porno.txt



## Fake-Science

Unter der Fake-Science Liste werden Websites von Predatory Publishers a.k.a Fake Science geblockt. Predatory Publishing, deutsch etwa „räuberisches Veröffentlichen“, ist ein betrügerisches Geschäftsmodell bestimmter Open-Access-Verlage. 

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Fake-Science



## CORONA Blocklisten

Diese Blocklist sperrt einige Seiten die z.B. Falschinformationen beinhalten.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/spam.mails



## Phishing-Angriffe

Unter Phising versteht man den versuch an Daten zu kommen in dem man z.B. eine Anmelde-Seite fälscht. Bekannte Phishing Domains werden mit dieser Liste gesperrt.

https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe
https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt
https://phishing.army/download/phishing_army_blocklist_extended.txt
http://phishing.mailscanner.info/phishing.bad.sites.conf
https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt



## Social Media Werbung Blocklisten

https://github.com/TheBlackDragon4/Jugendschutz/porno.txt



# Whitelists 

https://www.technoy.de/lists/whitelist.txt
https://github.com/TheBlackDragon4/Whitelisten/fullwhitelist.txt



