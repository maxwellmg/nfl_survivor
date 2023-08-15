#!/usr/bin/env ruby

theoretical_hash = {PHL1: 100, NYG1: 150, DAL1: 300, WAS1: -150, PHL2: 101, NYG2: 151, DAL2: 301, WAS2: -151, PHL3: 102, NYG3: 152, DAL3: 302, WAS3: -152}

best_path_list = []
greatest_value = 0
3.downto(1) do
  for team, odds in theoretical_hash
    if odds > greatest_value
      greatest_value = odds
    best_path_list << team
    week = team[3]
    #city = team[:2]
    puts week
    #puts city
  end
end
end
puts best_path_list
