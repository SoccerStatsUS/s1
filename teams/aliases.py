#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

mapping = {}

NASL_MAPPING = {
    "Carolina RailHawks": 'Carolina RailHawks FC',
    "Carolina Railhawks": 'Carolina RailHawks FC',
    "Fort Lauderdale Strikers": 'Fort Lauderdale Strikers (2011)',
}


MLSSOCCER_MAPPING = {
    "Miami": 'Miami Fusion F.C.',
    'Tampa Bay': 'Tampa Bay Mutiny',
    'Richmond': 'Richmond Kickers',
    'Puerto Rico': 'Puerto Rico Islanders',
    'Municipal': 'Club Social y Deportivo Municipal',
    'Harrisburg': 'Harrisburg City Islanders',
    'Metapan': 'Asociación Deportiva Isidro Metapán',
    'Arabe Unido': 'Club Deportivo Árabe Unido',
    'Saprissa': 'Deportivo Saprissa S.A.D.',
    'Joe Public FC': 'Joe Public Football Club',
    'Santos Laguna': 'Club Santos Laguna',
    'CD Guadalajara': 'Club Deportivo Guadalajara',
    'Charleston': 'Charleston Battery',
    'Portugal': 'Portugal national team',
    'Brazil': 'Brazil national team',
    'North Korea': 'North Korea national team',
    'Portugal': 'Portugal national team',
    'Slovakia': 'Slovakia national team',
    'Mexico': 'Mexico national team',
    'Uruguay': 'Uruguay national team',
    'France': 'France national team',
    'Nigeria': 'Nigeria national team',
    'Spain': 'Spain national team',
    'Denmark': 'Denmark national team',
    'Japan': 'Japan national team',
    'New Zealand': 'New Zealand national team',
    'Slovakia': 'Slovakia national team',
    'Italy': 'Italy national team',
    'Paraguay': 'Paraguay national team',
    'Cameroon': 'Cameroon national team',
    'Netherlands': 'Netherlands national team',
    'CD Motagua':  'Club Deportivo Motagua',
    'Ghana': 'Ghana national team',
    'Greece': 'Greece national team',
    'Australia': 'Australia national team',
    'Germany': 'Germany national team',
    'Argentina': 'Argentina national team',
    'South Korea': 'South Korea national team',
    'USA': 'United States national team',
    'Algeria': 'Algeria national team',
    'Slovenia': 'Slovenia national team',
    'Serbia': 'Serbia national team',
    'Rochester': 'Rochester Rhinos',
    'Marathon': 'Club Deportivo Marathón',
    'Chile': 'Chile national team',
    'Switzerland': 'Switzerland national team',
    'Honduras': 'Honduras national team',
    'Bolton': 'Bolton Wanderers Football Club',
    'St. Louis': 'Athletic Club of St. Louis',
    'South Africa': 'South Africa national team',
    'England': 'England national team',
    'Ivory Coast': 'Côte d\'Ivoire national team',
    'Tottenham': 'Tottenham Hotspur F.C.',
    'Portsmouth FC': 'Portsmouth Football Club',
    'Man City': 'Manchester City Football Club',
    

}


MLS_MAPPING = {
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

CNNSI_USA_MAPPING = {
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

CNNSI_GERMANY_MAPPING = {
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

CNNSI_SPAIN_MAPPING = {
    'Espanyol': 'Reial Club Deportiu Espanyol de Barcelona',
    'Granada CF': 'Granada Club de Fútbol',
    'Levante': 'Levante Unión Deportiva, S.A.D.',
    'Real Zaragoza': 'Real Zaragoza, S.A.D.',
    'Villarreal': 'Villarreal Club de Fútbol, S.A.D.',
    'Real Sporting de Gij&oacute;n': 'Real Sporting de Gijón, S.A.D.',
    'Osasuna': 'Club Atlético Osasuna',
    'Valencia': 'Valencia Club de Fútbol',
    'M&aacute;laga': 'Málaga Club de Fútbol',
    'Barcelona': 'Futbol Club Barcelona',
    'Rayo Vallecano': 'Rayo Vallecano de Madrid, S.A.D.',
    'Mallorca': 'Real Club Deportivo Mallorca',
    'Racing Santander': 'Real Racing Club de Santander, S.A.D.',
    'Getafe': 'Getafe Club de Fútbol',
    'Real Madrid': 'Real Madrid Club de Fútbol',
    'Athletic': 'Athletic Bilbao',
    'Real Betis': 'Real Betis Balompié S.A.D.',
    'Sevilla': 'Sevilla Fútbol Club S.A.D.',
    'Real Sociedad': 'Real Sociedad de Fútbol, S.A.D.',
    'Atl&eacute;tico Madrid': 'Club Atlético de Madrid, S.A.D.',
    'Sporting': 'Real Sporting de Gijón, S.A.D.',
}

CNNSI_HOLLAND_MAPPING = {
    'Excelsior': 'SBV Excelsior',
    'ADO Den Haag': 'Alles Door Oefening Den Haag',
    'Roda JC': 'Vereniging Roda Juliana Combinatie Kerkrade',
    'SC Heerenveen': 'Sportclub Heerenveen',
    'NEC Nijmegen': 'Nijmegen Eendracht Combinatie',
    'AZ Alkmaar': 'Alkmaar Zaanstreek',
    'PSV Eindhoven': 'Philips Sport Vereniging',
    'Ajax': 'Amsterdamsche Football Club Ajax',
    'Vitesse': 'Stichting Betaald Voetbal Vitesse',
    }

CNNSI_ITALY_MAPPING = {
    'Siena': 'Associazione Calcio Siena',
    'Fiorentina': 'ACF Fiorentina',
    'Cagliari': 'Cagliari Calcio',
    'AC Milan': 'Associazione Calcio Milan',
    'Napoli': 'Società Sportiva Calcio Napoli',
    'Genoa': 'Genoa Cricket and Football Club',
    'Atalanta': 'Atalanta Bergamasca Calcio',
    'Cesena': 'Associazione Calcio Cesena',
    'Bologna': 'Bologna Football Club 1909',
    'Roma': 'Associazione Sportiva Roma',
    'Inter Milan': 'Football Club Internazionale Milano',
    'Lecce': 'Unione Sportiva Lecce',
    'Lazio': 'Società Sportiva Lazio',
    'Chievo': 'Associazione Calcio Chievo Verona',
    'Parma': 'Parma Football Club',
    'Catania': 'Calcio Catania',
    'Udinese': 'Udinese Calcio',
    'Juventus': 'Juventus Football Club',
    'Novara': 'Novara Calcio',
    'Palermo': 'Unione Sportiva Città di Palermo',
}

CNNSI_SCOTLAND_MAPPING = {
    'Rangers': 'Rangers Football Club',
    'Kilmarnock': 'Kilmarnock Football Club',
    'Aberdeen': 'Aberdeen Football Club',
    'Celtic': 'Celtic Football Club',
    'Dunfermline': 'Dunfermline Athletic Football Club',
    'Inverness C.T.F.C': 'Inverness Caledonian Thistle Football Club',
    'Dundee United': 'Dundee United Football Club',
    'St. Mirren': 'St Mirren Football Club',
    'Hibernian': 'Hibernian Football Club',
    'St. Johnstone': 'St. Johnstone F.C.',
    'Motherwell': 'Motherwell Football & Athletic Club',
    'Hearts': 'Heart of Midlothian Football Club',
    }

CNNSI_MEXICO_MAPPING = {
    'Pachuca': 'Club de Fútbol Pachuca',
    'Cruz Azul': 'Club Deportivo, Social, y Cultural Cruz Azul',
    'Atlas': 'Club Social y Deportivo Atlas',
    'Toluca': 'Deportivo Toluca Fútbol Club',
    'Atlante': 'Atlante Fútbol Club',
    'Puebla': 'Puebla Futbol Club',
    'Pumas': 'Club Universidad Nacional A.C.',
    'Monterrey': 'Club de Futbol Monterrey',
    'Quer&eacute;taro': 'Querétaro Fútbol Club',
    'Guadalajara': 'Club Deportivo Guadalajara',
    'Santos': 'Club Santos Laguna',
    'Tijuana': 'Club de Fútbol Tijuana Xoloitzcuintles de Caliente',
    'Morelia': 'Club Atlético Monarcas Morelia',
    'Jaguares': 'Jaguares de Chiapas FC',
    'Toluca': 'Deportivo Toluca Fútbol Club',
    'Atlas': 'Club Social y Deportivo Atlas',
    'San Luis': 'San Luis Fútbol Club',
    'U. de N. Le&oacute;n': 'Tigres de la Universidad Autónoma de Nuevo León',
    'Am&eacute;rica': 'Club América',
    'Estudiantes': 'Club de Futbol Estudiantes',
    }

CNNSI_ENGLAND_MAPPING = {
    'Arsenal': 'Arsenal F.C.',
    'Aston Villa': 'Aston Villa Football Club',
    'Blackburn Rovers': 'Blackburn Rovers Football Club',
    'Bolton Wanderers': 'Bolton Wanderers Football Club',
    'Chelsea': 'Chelsea F.C.',
    'Everton': 'Everton Football Club',
    'Fulham': 'Fulham Football Club',
    'Liverpool': 'Liverpool Football Club',
    'Manchester City': 'Manchester City Football Club',
    'Manchester United': 'Manchester United F.C.',
    'Newcastle United': 'Newcastle United Football Club',
    'Norwich City': 'Norwich City Football Club',
    'Queens Park Rangers': 'Queens Park Rangers Football Club',
    'Stoke City': 'Stoke City Football Club',
    'Sunderland': 'Sunderland Association Football Club',
    'Swansea City': 'Swansea City Association Football Club',
    'Tottenham Hotspur': 'Tottenham Hotspur F.C.',
    'West Bromwich Albion': 'West Bromwich Albion Football Club',
    'Wigan Athletic': 'Wigan Athletic Football Club',
    'Wolves': 'Wolverhampton Wanderers Football Club',
    }

mapping.update(MLS_MAPPING)
mapping.update(MLSSOCCER_MAPPING)
mapping.update(NASL_MAPPING)

mapping.update(CNNSI_ENGLAND_MAPPING)
mapping.update(CNNSI_GERMANY_MAPPING)
mapping.update(CNNSI_HOLLAND_MAPPING)
mapping.update(CNNSI_ITALY_MAPPING)
mapping.update(CNNSI_MEXICO_MAPPING)
mapping.update(CNNSI_SCOTLAND_MAPPING)
mapping.update(CNNSI_SPAIN_MAPPING)
mapping.update(CNNSI_USA_MAPPING)



