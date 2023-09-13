#!/usr/bin/env ruby

full_team_to_abbrev = {
    "ATL" => "Atlanta", 
    "BUF" => "Buffalo", 
    "CHI" => "Chicago", 
    "CIN" => "Cincinatti", 
    "CLE" => "Cleveland", 
    "DAL" => "Dallas", 
    "DEN" => "Denver", 
    "GRB" => "Green Bay",
    "TEN" => "Tennessee", 
    "IND" => "Indianapolis", 
    "KAC" => "Kansas City",
    "LAV" => "Las Vegas",
    "LAR" => "Los Angeles Rams", 
    "MIA" => "Miami", 
    "MIN" => "Minnesota", 
    "NEE" => "New England",
    "NEO" => "New Orleans",
    "NYG" => "New York Giants", 
    "NYJ" => "New York Jets", 
    "PHI" => "Philadelphia", 
    "ARI" => "Arizona", 
    "PIT" => "Pittsburgh", 
    "LAC" => "Los Angeles Chargers", 
    "SAF" => "San Francisco",
    "SEA" => "Seattle", 
    "TAB" => "Tampa Bay",
    "WSH" => "Washington", 
    "CAR" => "Carolina", 
    "JAX" => "Jacksonville", 
    "BAL" => "Baltimore", 
    "HOU"  => "Houston" 
}

Abbreviation_addition = {"KC"=>"KAC","SF"=>"SAF","NE"=>"NEE", "NO"=>"NEO", "TB"=>"TAB", "LV"=>"LAV", "GB"=>"GRB"}

atlanta_season_hash = {"ATL1" => -179, "ATL2" => -125,"ATL3" => 180, "ATL4" => 170, "ATL5" => -175, "ATL6" => -130, "ATL7" => -115, "ATL8" => -105, "ATL9" => -105, "ATL10" => -142, "ATL12" => -110, "ATL13" => -220, "ATL14" => -162, "ATL15" => -105, "ATL16" => -148, "ATL17" => 110, "ATL18" => 124}

List_of_every_spread = ["ARI1 210", "ARI10 120", "ARI11 120", "ARI12 110", "ARI13 210", "ARI14 0", "ARI15 235", "ARI16 164", "ARI17 400", "ARI18 170", "ARI2 165", "ARI3 225", "ARI4 330", "ARI5 280", "ARI6 160", "ARI7 250", "ARI8 210", "ARI9 260", "ATL1 -150", "ATL10 -142", "ATL11 0", "ATL12 -110", "ATL13 220", "ATL14 -162", "ATL15 -105", "ATL16 -148", "ATL17 110", "ATL18 124", "ATL2 -115", "ATL3 180", "ATL4 168", "ATL5 -165", "ATL6 -130", "ATL7 -115", "ATL8 -105", "ATL9 -105", "BAL1 -420", "BAL10 -148", "BAL11 -105", "BAL12 105", "BAL13 0", "BAL14 -310", "BAL15 -105", "BAL16 130", "BAL17 -122", "BAL18 -175", "BAL2 155", "BAL3 -325", "BAL4 -105", "BAL5 -115", "BAL6 -215", "BAL7 -150", "BAL8 -258", "BAL9 -162", "BUF1 -120", "BUF10 -245", "BUF11 -185", "BUF12 110", "BUF13 0", "BUF14 145", "BUF15 -192", "BUF16 -115", "BUF17 -270", "BUF18 102", "BUF2 -360", "BUF3 -195", "BUF4 -175", "BUF5 -168", "BUF6 -305", "BUF7 -175", "BUF8 -440", "BUF9 -105", "CAR1 140", "CAR10 105", "CAR11 150", "CAR12 -105", "CAR13 -105", "CAR14 150", "CAR15 -115", "CAR16 -105", "CAR17 170", "CAR18 -130", "CAR2 -105", "CAR3 160", "CAR4 100", "CAR5 180", "CAR6 255", "CAR7 0", "CAR8 -148", "CAR9 -130", "CHI1 -140", "CHI10 -125", "CHI11 170", "CHI12 150", "CHI13 0", "CHI14 100", "CHI15 145", "CHI16 -198", "CHI17 -130", "CHI18 105", "CHI2 -120", "CHI3 330", "CHI4 100", "CHI5 100", "CHI6 -110", "CHI7 -115", "CHI8 190", "CHI9 120", "CIN1 -130", "CIN10 -395", "CIN11 -115", "CIN12 -198", "CIN13 -115", "CIN14 -395", "CIN15 -218", "CIN16 -130", "CIN17 148", "CIN18 -175", "CIN2 -180", "CIN3 -345", "CIN4 -195", "CIN5 -340", "CIN6 -205", "CIN7 0", "CIN8 -105", "CIN9 -115", "CLE1 115", "CLE10 124", "CLE11 -120", "CLE12 -105", "CLE13 -142", "CLE14 -122", "CLE15 -175", "CLE16 -192", "CLE17 -102", "CLE18 145", "CLE2 -105", "CLE3 -195", "CLE4 -115", "CLE5 0", "CLE6 -105", "CLE7 -150", "CLE8 105", "CLE9 -325", "DAL1 -160", "DAL10 -218", "DAL11 -180", "DAL12 -230", "DAL13 -180", "DAL14 -115", "DAL15 160", "DAL16 100", "DAL17 -175", "DAL18 -155", "DAL2 -135", "DAL3 -305", "DAL4 -205", "DAL5 110", "DAL6 -105", "DAL7 0", "DAL8 -298", "DAL9 130", "DEN1 -180", "DEN10 200", "DEN11 -125", "DEN12 -115", "DEN13 -180", "DEN14 124", "DEN15 105", "DEN16 -125", "DEN17 -115", "DEN18 -115", "DEN2 -170", "DEN3 145", "DEN4 -120", "DEN5 -105", "DEN6 260", "DEN7 -170", "DEN8 145", "DEN9 0", "DET1 250", "DET10 136", "DET11 -205", "DET12 -185", "DET13 -108", "DET14 -120", "DET15 -125", "DET16 -105", "DET17 145", "DET18 -135", "DET2 -140", "DET3 -210", "DET4 -120", "DET5 -210", "DET6 -180", "DET7 130", "DET8 -198", "DET9 0", "GB1 122", "GB10 124", "GB11 110", "GB12 154", "GB13 180", "GB14 110", "GB15 -175", "GB16 -115", "GB17 136", "GB18 -125", "GB2 -105", "GB3 -115", "GB4 100", "GB5 100", "GB6 0", "GB7 145", "GB8 -105", "GB9 -142", "HOU1 340", "HOU10 310", "HOU11 -142", "HOU12 164", "HOU13 150", "HOU14 285", "HOU15 124", "HOU16 160", "HOU17 -105", "HOU18 102", "HOU2 -115", "HOU3 250", "HOU4 150", "HOU5 140", "HOU6 130", "HOU7 0", "HOU8 124", "HOU9 -115", "IND1 150", "IND10 176", "IND11 0", "IND12 -115", "IND13 120", "IND14 310", "IND15 110", "IND16 124", "IND17 105", "IND18 -122", "IND2 -105", "IND3 270", "IND4 -105", "IND5 -115", "IND6 220", "IND7 130", "IND8 102", "IND9 110", "JAX1 -165", "JAX10 -105", "JAX11 -205", "JAX12 -198", "JAX13 -105", "JAX14 102", "JAX15 -115", "JAX16 -175", "JAX17 -205", "JAX18 -130", "JAX2 130", "JAX3 -300", "JAX4 -180", "JAX5 145", "JAX6 -260", "JAX7 -105", "JAX8 -102", "JAX9 0", "KC1 -275", "KC10 0", "KC11 -148", "KC12 -205", "KC13 -218", "KC14 -175", "KC15 -218", "KC16 -395", "KC17 -155", "KC18 -125", "KC2 -150", "KC3 -410", "KC4 -115", "KC5 -190", "KC6 -325", "KC7 -215", "KC8 -175", "KC9 -205", "LAC1 -138", "LAC10 -162", "LAC11 -130", "LAC12 -125", "LAC13 -120", "LAC14 -148", "LAC15 -130", "LAC16 -105", "LAC17 -105", "LAC18 105", "LAC2 -180", "LAC3 -120", "LAC4 -205", "LAC5 0", "LAC6 -115", "LAC7 185", "LAC8 -230", "LAC9 105", "LAR1 210", "LAR10 0", "LAR11 105", "LAR12 -130", "LAR13 120", "LAR14 250", "LAR15 -115", "LAR16 -102", "LAR17 140", "LAR18 240", "LAR2 175", "LAR3 285", "LAR4 -115", "LAR5 190", "LAR6 -190", "LAR7 110", "LAR8 240", "LAR9 120", "LV1 172", "LV10 110", "LV11 185", "LV12 170", "LV13 0", "LV14 100", "LV15 110", "LV16 350", "LV17 -125", "LV18 -105", "LV2 295", "LV3 -105", "LV4 175", "LV5 -120", "LV6 -115", "LV7 -105", "LV8 164", "LV9 -120", "MIA1 120", "MIA10 0", "MIA11 -225", "MIA11 0", "MIA12 114", "MIA13 -175", "MIA14 -298", "MIA15 -120", "MIA16 -120", "MIA17 102", "MIA18 -122", "MIA2 -130", "MIA3 -170", "MIA4 150", "MIA5 -200", "MIA6 -305", "MIA7 160", "MIA8 -185", "MIA9 188", "MIN1 -270", "MIN10 -135", "MIN11 105", "MIN12 -180", "MIN13 0", "MIN14 -120", "MIN15 180", "MIN16 -115", "MIN17 -162", "MIN18 114", "MIN2 210", "MIN3 100", "MIN4 -120", "MIN5 160", "MIN6 -110", "MIN7 110", "MIN8 -115", "MIN9 -115", "NE1 188", "NE10 -192", "NE12 100", "NE13 100", "NE14 114", "NE15 180", "NE16 105", "NE17 220", "NE18 -105", "NE2 110", "NE3 150", "NE4 175", "NE5 -140", "NE6 -105", "NE7 150", "NE8 154", "NE9 -175", "NO1 -172", "NO10 114", "NO11 0", "NO12 -110", "NO13 -112", "NO14 -180", "NO15 -130", "NO16 -118", "NO17 -122", "NO18 -148", "NO2 -115", "NO3 -105", "NO4 -190", "NO5 120", "NO6 -150", "NO7 -115", "NO8 -122", "NO9 -142", "NYG1 140", "NYG10 180", "NYG11 -122", "NYG12 -120", "NYG13 0", "NYG14 -130", "NYG15 110", "NYG16 285", "NYG17 -166", "NYG18 130", "NYG2 -195", "NYG3 175", "NYG4 -115", "NYG5 170", "NYG6 255", "NYG7 -135", "NYG8 102", "NYG9 100", "NYJ1 106", "NYJ10 -130", "NYJ11 154", "NYJ12 -130", "NYJ13 -270", "NYJ14 -360", "NYJ15 100", "NYJ16 -218", "NYJ17 -118", "NYJ18 -115", "NYJ2 115", "NYJ3 -175", "NYJ4 -105", "NYJ5 -115", "NYJ6 -105", "NYJ7 0", "NYJ8 -122", "NYJ9 -125", "PHI1 -200", "PHI10 0", "PHI11 142", "PHI12 -130", "PHI13 -134", "PHI14 -105", "PHI15 -125", "PHI16 -298", "PHI17 -535", "PHI18 -155", "PHI2 -250", "PHI3 -265", "PHI4 -330", "PHI5 -225", "PHI6 -115", "PHI7 -190", "PHI8 -185", "PHI9 -155", "PIT1 130", "PIT10 -148", "PIT11 100", "PIT12 164", "PIT13 -258", "PIT14 -135", "PIT15 -130", "PIT16 110", "PIT17 114", "PIT18 145", "PIT2 -115", "PIT3 -115", "PIT4 -175", "PIT5 -115", "PIT6 0", "PIT7 -130", "PIT8 -118", "PIT9 -180", "SEA1 -240", "SEA10 -185", "SEA11 -125", "SEA12 100", "SEA13 150", "SEA14 154", "SEA15 105", "SEA16 -125", "SEA17 -135", "SEA18 -205", "SEA2 120", "SEA3 -190", "SEA4 -105", "SEA5 0", "SEA6 175", "SEA7 -300", "SEA8 -125", "SEA9 136", "SF1 -146", "SF10 -115", "SF11 -340", "SF12 -120", "SF13 114", "SF14 -185", "SF15 -290", "SF16 -155", "SF17 -170", "SF18 -298", "SF2 -205", "SF3 -205", "SF4 -410", "SF5 -130", "SF6 -115", "SF7 -130", "SF8 -115", "SF9 0", "TB1 235", "TB10 -105", "TB11 270", "TB12 -105", "TB13 -115", "TB14 136", "TB15 145", "TB16 145", "TB17 102", "TB18 110", "TB2 100", "TB3 225", "TB4 160", "TB5 0", "TB6 155", "TB7 -105", "TB8 340", "TB9 -105", "TEN1 160", "TEN10 -115", "TEN11 170", "TEN12 -115", "TEN13 -142", "TEN14 240", "TEN15 -148", "TEN16 105", "TEN17 -115", "TEN18 110", "TEN2 155", "TEN3 165", "TEN4 165", "TEN5 -105", "TEN6 190", "TEN7 0", "TEN8 -115", "TEN9 150", "WSH1 -230", "WSH10 154", "WSH11 102", "WSH12 190", "WSH13 145", "WSH14 0", "WSH15 -105", "WSH16 180", "WSH17 142", "WSH18 130", "WSH2 145", "WSH3 165", "WSH4 275", "WSH5 -120", "WSH6 110", "WSH7 115", "WSH8 154", "WSH9 145"]

new_list = []

for item in List_of_every_spread do
    new_list << item.split(" ")
end

new_hash = new_list.to_h()

final_hash = {}

for team, odds in new_hash
    odds = odds.to_i()
    final_hash.store(team,odds)
    #puts team, odds
end

#puts final_hash

