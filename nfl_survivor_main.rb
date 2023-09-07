#!/usr/bin/env ruby
from 2023_odds import hash_final

best_path_list = []

18.downto(1) do
  greatest_value = 1000
  for team, odds in hash_final
    if odds < greatest_value
      greatest_value = odds
    end
  end
  for team, odds in hash_final
    if odds == greatest_value
      best_path_list << team
      city = team[0, 3]
      if team.length == 4
        week = team[-1]
      elsif team.length == 5 
        week = team[-2..-1]
      end
    end
  end
  for team, odds in hash_final
    if team.start_with? city
      hash_final.delete team
    end
    if team.end_with? week
      hash_final.delete team
    end
  end
end





puts best_path_list
