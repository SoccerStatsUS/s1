#!/usr/local/bin/python
# -*- coding: utf-8 -*-

mapping = {
    "FC Dallas": "Football Club Dallas",
    "Dallas Burn": "Football Club Dallas",
    "F.C. Dallas": "Football Club Dallas",
    "C.D. Chivas USA": "Club Deportivo Chivas USA",
    'Chicago Fire': 'Chicago Fire S.C.',
    "Chivas USA": "Club Deportivo Chivas USA",
    "Red Bull New York": "New York Red Bulls",
    "Metrostars": "New York Red Bulls",
    "MetroStars": "New York Red Bulls",
    "Miami Fusion": "Miami Fusion F.C.",
    "Seattle Sounders": "Seattle Sounders FC",
    "San Jose Clash": "San Jose Earthquakes",
    "New York/New Jersey MetroStars": "New York Red Bulls",
    'Kansas City Wiz': "Sporting Kansas City",
    "Kansas City Wizards": "Sporting Kansas City",
    "Houston 1836": "Houston Dynamo",
    }

CNNSI_MAPPING = {
    "Manchester United": "Manchester United F.C.",
    "MLS": "MLS All-Stars",
    "Houston": "Houston Dynamo",
    "D.C.": "D.C. United",
    "Portland": "Portland Timbers",
    "Seattle": "Seattle Sounders FC",
    "Columbus": "Columbus Crew",
    "San Jose": "San Jose Earthquakes",
    "Vancouver": "Vancouver Whitecaps FC",
    "Vancouver Whitecaps": "Vancouver Whitecaps FC",
    "Chicago": "Chicago Fire S.C.",
    "Colorado": "Colorado Rapids",
    "Sporting KC": "Sporting Kansas City",
    "Los Angeles": "Los Angeles Galaxy",
    "New York": "New York Red Bulls",
    "Philadelphia": "Philadelphia Union",
    "New England": "New England Revolution",
    }

CNNSI_BUNDESLIGA_MAPPING = {
    "M&ouml;nchen": "Borussia Mönchengladbach",
    "FC Schalke 04": "Fußball-Club Gelsenkirchen-Schalke 04",
    "FSV Mainz 05": "1. Fußball- und Sportverein Mainz 05 e. V",
    "Hannover 96": "Hannoverscher Sportverein von 1896",
    "Borussia Dortmund": "Ballspielverein Borussia (BVB) Dortmund",
    "Bayer Leverkusen": "Bayer 04 Leverkusen",
    "Werder Bremen": "SV Werder Bremen",
    "1899 Hoffenheim": "TSG 1899 Hoffenheim",
    "1. FC N&uuml;rnberg": "1. FC Nuremberg",
    "Bayern M&uuml;nchen": "FC Bayern Munich",
    "Kaiserslautern": "1. FC Kaiserslautern",
    "1. FC Koln": "1. FC Köln",
    "Hamburger SV": "Hamburger Sport-Verein",
    "SC Freiburg": "Sport-Club Freiburg",
    "VfB Stuttgart": "Verein für Bewegungsspiele Stuttgart 1893 e. V.",
    "Hertha BSC Berlin": "Hertha Berliner Sport-Club von 1892",
    }
    

mapping.update(CNNSI_MAPPING)
mapping.update(CNNSI_BUNDESLIGA_MAPPING)

