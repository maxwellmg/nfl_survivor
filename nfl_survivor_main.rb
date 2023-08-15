#!/usr/bin/env ruby

theoretical_hash = {"PHL1" => 100, "NYG1" => 150, "DAL1" => 300, "WSH1" => -150, "PHL2" => 101, "NYG2" => 151, "DAL2" => 301, "WSH2" => -151, "PHL3" => 102, "NYG3" => 152, "DAL3" => 302, "WSH3" => -152}

best_path_list = []

3.downto(1) do
  greatest_value = 0
  for team, odds in theoretical_hash
    if odds > greatest_value
      greatest_value = odds
    end
  for team, odds in theoretical_hash
    if odds == greatest_value
      best_path_list << team
      week = team[3]
      city = team[0, 2]
      for team, odds in theoretical_hash
        if team.start_with? city
          theoretical_hash.delete team
        end
        if team.end_with? week
          theoretical_hash.delete team
        end
      end
    end
  end
end
end



puts best_path_list
