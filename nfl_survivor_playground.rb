theoretical_hash = {"PHL1" => 100, "NYG1" => 150, "DAL1" => 300, "WSH1" => -150, "PHL2" => 101, "NYG2" => 151, "DAL2" => 301, "WSH2" => -151, "PHL3" => 102, "NYG3" => 152, "DAL3" => 302, "WSH3" => -152}

week = "2"
city = "DAL"

#for team, odds in theoretical_hash
#    if team.start_with? city
#      theoretical_hash.delete team
#    end
#end

for team, odds in theoretical_hash
    if team.end_with? week
      theoretical_hash.delete team
    end
end


puts theoretical_hash