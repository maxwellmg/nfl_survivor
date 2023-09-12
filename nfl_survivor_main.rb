#!/usr/bin/env ruby

theoretical_hash = {"PHL1" => 100, "NYG1" => 150, "DAL1" => 300, "WSH1" => -150, "PHL2" => 101, "NYG2" => 151, "DAL2" => 301, "WSH2" => -151, "PHL3" => 102, "NYG3" => 152, "DAL3" => 302, "WSH3" => -152}

hash_final = {"ARI1"=>210,"ARI10"=>120, "ARI11"=>120, "ARI12"=>110,"ARI13"=>210, "ARI14"=>0, "ARI15"=>235, "ARI16"=>164, "ARI17"=>400, "ARI18"=>170, "ARI2"=>165, "ARI3"=>225, "ARI4"=>330, "ARI5"=>280, "ARI6"=>160, "ARI7"=>250, "ARI8"=>210, "ARI9"=>260, "ATL1"=>-150, "ATL10"=>-142, "ATL11"=>0, "ATL12"=>-110, "ATL13"=>220, "ATL14"=>-162, "ATL15"=>-105, "ATL16"=>-148, "ATL17"=>110, "ATL18"=>124, "ATL2"=>-115, "ATL3"=>180, "ATL4"=>168, "ATL5"=>-165, "ATL6"=>-130, "ATL7"=>-115, "ATL8"=>-105, "ATL9"=>-105, "BAL1"=>-420, "BAL10"=>-148, "BAL11"=>-105, "BAL12"=>105, "BAL13"=>0, "BAL14"=>-310, "BAL15"=>-105, "BAL16"=>130, "BAL17"=>-122, "BAL18"=>-175, "BAL2"=>155, "BAL3"=>-325, "BAL4"=>-105, "BAL5"=>-115, "BAL6"=>-215, "BAL7"=>-150, "BAL8"=>-258, "BAL9"=>-162, "BUF1"=>-120, "BUF10"=>-245, "BUF11"=>-185, "BUF12"=>110, "BUF13"=>0, "BUF14"=>145, "BUF15"=>-192, "BUF16"=>-115, "BUF17"=>-270, "BUF18"=>102, "BUF2"=>-360, "BUF3"=>-195, "BUF4"=>-175, "BUF5"=>-168, "BUF6"=>-305, "BUF7"=>-175, "BUF8"=>-440, "BUF9"=>-105, "CAR1"=>140, "CAR10"=>105, "CAR11"=>150, "CAR12"=>-105, "CAR13"=>-105, "CAR14"=>150, "CAR15"=>-115, "CAR16"=>-105, "CAR17"=>170, "CAR18"=>-130, "CAR2"=>-105, "CAR3"=>160, "CAR4"=>100, "CAR5"=>180, "CAR6"=>255, "CAR7"=>0, "CAR8"=>-148, "CAR9"=>-130, "CHI1"=>-140, "CHI10"=>-125, "CHI11"=>170, "CHI12"=>150, "CHI13"=>0, "CHI14"=>100, "CHI15"=>145, "CHI16"=>-198, "CHI17"=>-130, "CHI18"=>105, "CHI2"=>-120, "CHI3"=>330, "CHI4"=>100, "CHI5"=>100, "CHI6"=>-110, "CHI7"=>-115, "CHI8"=>190, "CHI9"=>120, "CIN1"=>-130, "CIN10"=>-395, "CIN11"=>-115, "CIN12"=>-198, "CIN13"=>-115, "CIN14"=>-395, "CIN15"=>-218, "CIN16"=>-130, "CIN17"=>148, "CIN18"=>-175, "CIN2"=>-180, "CIN3"=>-345, "CIN4"=>-195, "CIN5"=>-340, "CIN6"=>-205, "CIN7"=>0, "CIN8"=>-105, "CIN9"=>-115, "CLE1"=>115, "CLE10"=>124, "CLE11"=>-120, "CLE12"=>-105, "CLE13"=>-142, "CLE14"=>-122, "CLE15"=>-175, "CLE16"=>-192, "CLE17"=>-102, "CLE18"=>145, "CLE2"=>-105, "CLE3"=>-195, "CLE4"=>-115, "CLE5"=>0, "CLE6"=>-105, "CLE7"=>-150, "CLE8"=>105, "CLE9"=>-325, "DAL1"=>-160, "DAL10"=>-218, "DAL11"=>-180, "DAL12"=>-230, "DAL13"=>-180, "DAL14"=>-115, "DAL15"=>160, "DAL16"=>100, "DAL17"=>-175, "DAL18"=>-155, "DAL2"=>-135, "DAL3"=>-305, "DAL4"=>-205, "DAL5"=>110, "DAL6"=>-105, "DAL7"=>0, "DAL8"=>-298, "DAL9"=>130, "DEN1"=>-180, "DEN10"=>200, "DEN11"=>-125, "DEN12"=>-115, "DEN13"=>-180, "DEN14"=>124, "DEN15"=>105, "DEN16"=>-125, "DEN17"=>-115, "DEN18"=>-115, "DEN2"=>-170, "DEN3"=>145, "DEN4"=>-120, "DEN5"=>-105, "DEN6"=>260, "DEN7"=>-170, "DEN8"=>145, "DEN9"=>0, "DET1"=>250, "DET10"=>136, "DET11"=>-205, "DET12"=>-185, "DET13"=>-108, "DET14"=>-120, "DET15"=>-125, "DET16"=>-105, "DET17"=>145, "DET18"=>-135, "DET2"=>-140, "DET3"=>-210, "DET4"=>-120, "DET5"=>-210, "DET6"=>-180, "DET7"=>130, "DET8"=>-198, "DET9"=>0, "GRB1"=>122, "GRB10"=>124, "GRB11"=>110, "GRB12"=>154, "GRB13"=>180, "GRB14"=>110, "GRB15"=>-175, "GRB16"=>-115, "GRB17"=>136, "GRB18"=>-125, "GRB2"=>-105, "GRB3"=>-115, "GRB4"=>100, "GRB5"=>100, "GRB6"=>0, "GRB7"=>145, "GRB8"=>-105, "GRB9"=>-142, "HOU1"=>340, "HOU10"=>310, "HOU11"=>-142, "HOU12"=>164, "HOU13"=>150, "HOU14"=>285, "HOU15"=>124, "HOU16"=>160, "HOU17"=>-105, "HOU18"=>102, "HOU2"=>-115, "HOU3"=>250, "HOU4"=>150, "HOU5"=>140, "HOU6"=>130, "HOU7"=>0, "HOU8"=>124, "HOU9"=>-115, "IND1"=>150, "IND10"=>176, "IND11"=>0, "IND12"=>-115, "IND13"=>120, "IND14"=>310, "IND15"=>110, "IND16"=>124, "IND17"=>105, "IND18"=>-122, "IND2"=>-105, "IND3"=>270, "IND4"=>-105, "IND5"=>-115, "IND6"=>220, "IND7"=>130, "IND8"=>102, "IND9"=>110, "JAX1"=>-165, "JAX10"=>-105, "JAX11"=>-205, "JAX12"=>-198, "JAX13"=>-105, "JAX14"=>102, "JAX15"=>-115, "JAX16"=>-175, "JAX17"=>-205, "JAX18"=>-130, "JAX2"=>130, "JAX3"=>-300, "JAX4"=>-180, "JAX5"=>145, "JAX6"=>-260, "JAX7"=>-105, "JAX8"=>-102, "JAX9"=>0, "KAC1"=>-275, "KAC10"=>0, "KAC11"=>-148, "KAC12"=>-205, "KAC13"=>-218, "KAC14"=>-175, "KAC15"=>-218, "KAC16"=>-395, "KAC17"=>-155, "KAC18"=>-125, "KAC2"=>-150, "KAC3"=>-410, "KAC4"=>-115, "KAC5"=>-190, "KAC6"=>-325, "KAC7"=>-215, "KAC8"=>-175, "KAC9"=>-205, "LAC1"=>-138, "LAC10"=>-162, "LAC11"=>-130, "LAC12"=>-125, "LAC13"=>-120, "LAC14"=>-148, "LAC15"=>-130, "LAC16"=>-105, "LAC17"=>-105, "LAC18"=>105, "LAC2"=>-180, "LAC3"=>-120, "LAC4"=>-205, "LAC5"=>0, "LAC6"=>-115, "LAC7"=>185, "LAC8"=>-230, "LAC9"=>105, "LAR1"=>210, "LAR10"=>0, "LAR11"=>105, "LAR12"=>-130, "LAR13"=>120, "LAR14"=>250, "LAR15"=>-115, "LAR16"=>-102, "LAR17"=>140, "LAR18"=>240, "LAR2"=>175, "LAR3"=>285, "LAR4"=>-115, "LAR5"=>190, "LAR6"=>-190, "LAR7"=>110, "LAR8"=>240, "LAR9"=>120, "LAV1"=>172, "LAV10"=>110, "LAV11"=>185, "LAV12"=>170, "LAV13"=>0, "LAV14"=>100, "LAV15"=>110, "LAV16"=>350, "LAV17"=>-125, "LAV18"=>-105, "LAV2"=>295, "LAV3"=>-105, "LAV4"=>175, "LAV5"=>-120, "LAV6"=>-115, "LAV7"=>-105, "LAV8"=>164, "LAV9"=>-120, "MIA1"=>120, "MIA10"=>0, "MIA11"=>0, "MIA12"=>114, "MIA13"=>-175, "MIA14"=>-298, "MIA15"=>-120, "MIA16"=>-120, "MIA17"=>102, "MIA18"=>-122, "MIA2"=>-130, "MIA3"=>-170, "MIA4"=>150, "MIA5"=>-200, "MIA6"=>-305, "MIA7"=>160, "MIA8"=>-185, "MIA9"=>188, "MIN1"=>-270, "MIN10"=>-135, "MIN11"=>105, "MIN12"=>-180, "MIN13"=>0, "MIN14"=>-120, "MIN15"=>180, "MIN16"=>-115, "MIN17"=>-162, "MIN18"=>114, "MIN2"=>210, "MIN3"=>100, "MIN4"=>-120, "MIN5"=>160, "MIN6"=>-110, "MIN7"=>110, "MIN8"=>-115, "MIN9"=>-115, "NEE1"=>188, "NEE10"=>-192, "NEE12"=>100, "NEE13"=>100, "NEE14"=>114, "NEE15"=>180, "NEE16"=>105, "NEE17"=>220, "NEE18"=>-105, "NEE2"=>110, "NEE3"=>150, "NEE4"=>175, "NEE5"=>-140, "NEE6"=>-105, "NEE7"=>150, "NEE8"=>154, "NEE9"=>-175, "NEO1"=>-172, "NEO10"=>114, "NEO11"=>0, "NEO12"=>-110, "NEO13"=>-112, "NEO14"=>-180, "NEO15"=>-130, "NEO16"=>-118, "NEO17"=>-122, "NEO18"=>-148, "NEO2"=>-115, "NEO3"=>-105, "NEO4"=>-190, "NEO5"=>120, "NEO6"=>-150, "NEO7"=>-115, "NEO8"=>-122, "NEO9"=>-142, "NYG1"=>140, "NYG10"=>180, "NYG11"=>-122, "NYG12"=>-120, "NYG13"=>0, "NYG14"=>-130, "NYG15"=>110, "NYG16"=>285, "NYG17"=>-166, "NYG18"=>130, "NYG2"=>-195, "NYG3"=>175, "NYG4"=>-115, "NYG5"=>170, "NYG6"=>255, "NYG7"=>-135, "NYG8"=>102, "NYG9"=>100, "NYJ1"=>106, "NYJ10"=>-130, "NYJ11"=>154, "NYJ12"=>-130, "NYJ13"=>-270, "NYJ14"=>-360, "NYJ15"=>100, "NYJ16"=>-218, "NYJ17"=>-118, "NYJ18"=>-115, "NYJ2"=>115, "NYJ3"=>-175, "NYJ4"=>-105, "NYJ5"=>-115, "NYJ6"=>-105, "NYJ7"=>0, "NYJ8"=>-122, "NYJ9"=>-125, "PHI1"=>-200, "PHI10"=>0, "PHI11"=>142, "PHI12"=>-130, "PHI13"=>-134, "PHI14"=>-105, "PHI15"=>-125, "PHI16"=>-298, "PHI17"=>-535, "PHI18"=>-155, "PHI2"=>-250, "PHI3"=>-265, "PHI4"=>-330, "PHI5"=>-225, "PHI6"=>-115, "PHI7"=>-190, "PHI8"=>-185, "PHI9"=>-155, "PIT1"=>130, "PIT10"=>-148, "PIT11"=>100, "PIT12"=>164, "PIT13"=>-258, "PIT14"=>-135, "PIT15"=>-130, "PIT16"=>110, "PIT17"=>114, "PIT18"=>145, "PIT2"=>-115, "PIT3"=>-115, "PIT4"=>-175, "PIT5"=>-115, "PIT6"=>0, "PIT7"=>-130, "PIT8"=>-118, "PIT9"=>-180, "SEA1"=>-240, "SEA10"=>-185, "SEA11"=>-125, "SEA12"=>100, "SEA13"=>150, "SEA14"=>154, "SEA15"=>105, "SEA16"=>-125, "SEA17"=>-135, "SEA18"=>-205, "SEA2"=>120, "SEA3"=>-190, "SEA4"=>-105, "SEA5"=>0, "SEA6"=>175, "SEA7"=>-300, "SEA8"=>-125, "SEA9"=>136, "SAF1"=>-146, "SAF10"=>-115, "SAF11"=>-340, "SAF12"=>-120, "SAF13"=>114, "SAF14"=>-185, "SAF15"=>-290, "SAF16"=>-155, "SAF17"=>-170, "SAF18"=>-298, "SAF2"=>-205, "SAF3"=>-205, "SAF4"=>-410, "SAF5"=>-130, "SAF6"=>-115, "SAF7"=>-130, "SAF8"=>-115, "SAF9"=>0, "TAB1"=>235, "TAB10"=>-105, "TAB11"=>270, "TAB12"=>-105, "TAB13"=>-115, "TAB14"=>136, "TAB15"=>145, "TAB16"=>145, "TAB17"=>102, "TAB18"=>110, "TAB2"=>100, "TAB3"=>225, "TAB4"=>160, "TAB5"=>0, "TAB6"=>155, "TAB7"=>-105, "TAB8"=>340, "TAB9"=>-105, "TEN1"=>160, "TEN10"=>-115, "TEN11"=>170, "TEN12"=>-115, "TEN13"=>-142, "TEN14"=>240, "TEN15"=>-148, "TEN16"=>105, "TEN17"=>-115, "TEN18"=>110, "TEN2"=>155, "TEN3"=>165, "TEN4"=>165, "TEN5"=>-105, "TEN6"=>190, "TEN7"=>0, "TEN8"=>-115, "TEN9"=>150, "WSH1"=>-230, "WSH10"=>154, "WSH11"=>102, "WSH12"=>190, "WSH13"=>145, "WSH14"=>0, "WSH15"=>-105, "WSH16"=>180, "WSH17"=>142, "WSH18"=>130, "WSH2"=>145, "WSH3"=>165, "WSH4"=>275, "WSH5"=>-120, "WSH6"=>110, "WSH7"=>115, "WSH8"=>154, "WSH9"=>145}

best_path_list = []

count = 0
18.downto(1) do
  one_week_list = []
  #set moneyline arbitrarily high
  greatest_value = 0

  #find the best moneyline over the course of the season by setting a new minimum each time one is found
  for team, odds in hash_final
    if odds < greatest_value
      greatest_value = odds
      puts greatest_value
    end
  end
  
  #Find the team with the moneyline that matches the best over the course of the season, append the team/week to a list of best options
  puts count
  count +=1
  one_week_list = []
  for team, odds in hash_final
    if odds == greatest_value
      one_week_list << team
      puts team
    end
  end

  #check to see if multiple teams have the best odds for the same week
  if one_week_list.length > 1
    puts "Here are the teams with the same odds: " + one_week_list.to_s + "\n Please type the team you would choose to win: \n"
    selection = gets.chomp
    #for team, odds in hash_final
     #if team == selection
    best_path_list << selection
    puts "team: " + selection
    city = selection[0, 3]
    if team.length == 4
      week = selection[-1]
    elsif team.length == 5 
      week = selection[-2..-1]
    end
  else
    for team, odds in hash_final
      if odds == greatest_value
        best_path_list << team
        best_path_list << odds
        s_odds = odds.to_s
        puts "team: " + team + " odds: " + s_odds
        #Set values for the team and week of the choice that will be removed from the list

        city = team[0, 3]
        if team.length == 4
          week = team[-1]
        elsif team.length == 5 
          week = team[-2..-1]
        end
      end
    end
  end

  #Remove the teams with the best odds and all other options for the same week from the hash of all moneylines (now that they've been added to a new list) so that we can loop the program without overlap
  
  #for team, odds in hash_final
    #if team.start_with? city
      #puts city
      #hash_final.delete team
    #elsif team.end_with? week
      #puts week
      #hash_final.delete team
    #end
  #end
  for team, odds in hash_final
    if team.start_with? city
      hash_final.delete(team)
    end
    if team.end_with? week
      hash_final.delete(team)
    end
  end
end


#def get_team_and_week(team)
  #city = team[0, 3]
  #if team.length == 4
    #week = team[-1]
  #elsif team.length == 5 
    #week = team[-2..-1]


puts best_path_list