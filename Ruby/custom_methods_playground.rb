#!/usr/bin/env ruby

def teams_selected 
  @teams_selected ||=[]
end

#"ARI" => "Arizona", "ATL" => "Atlanta", "BAL" => "Baltimore", "BUF" => "Buffalo", "CAR" => "Carolina", "CHI" => "Chicago", "CIN" => "Cincinatti", "CLE" => "Cleveland", "DAL" => "Dallas", "DEN" => "Denver", "DET" => "Detroit", "GRB" => "Green Bay", "HOU" => "Houston", "IND" => "Indianapolis", "JAX" => "Jacksonville", "KAC" => "Kansas City", "LAC" => "Los Angeles Chargers", "LAR" => "Los Angeles Rams", "LAV" => "Las Vegas", "MIA" => "Miami", "MIN" => "Minnesota", "NEE" => "New England", "NEO" => "New Orleans","NYG" => "New York Giants", "NYJ" => "New York Jets", "PHI" => "Philadelphia", "PIT" => "Pittsburgh", "SAF" => "San Francisco", "SEA" => "Seattle", "TAB" => "Tampa Bay", "TEN" => "Tennessee", "WSH" => "Washington"
def weeks_played()
  abbreviaton_to_full_team = {
    "ARI" => "Arizona", "ATL" => "Atlanta", "BAL" => "Baltimore", "BUF" => "Buffalo", "CAR" => "Carolina", "CHI" => "Chicago", "CIN" => "Cincinatti", "CLE" => "Cleveland", "DAL" => "Dallas", "DEN" => "Denver", "DET" => "Detroit", "GRB" => "Green Bay", "HOU" => "Houston", "IND" => "Indianapolis", "JAX" => "Jacksonville", "KAC" => "Kansas City", "LAC" => "Los Angeles Chargers", "LAR" => "Los Angeles Rams", "LAV" => "Las Vegas", "MIA" => "Miami", "MIN" => "Minnesota", "NEE" => "New England", "NEO" => "New Orleans","NYG" => "New York Giants", "NYJ" => "New York Jets", "PHI" => "Philadelphia", "PIT" => "Pittsburgh", "SAF" => "San Francisco", "SEA" => "Seattle", "TAB" => "Tampa Bay", "TEN" => "Tennessee", "WSH" => "Washington"
}
  team_abbreviations = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET", "GRB", "HOU", "IND", "JAX", "KAC", "LAC", "LAR", "LAV", "MIA", "MIN", "NEE", "NEO", "NYG", "NYJ", "PHI", "PIT", "SAF", "SEA", "TAB", "TEN", "WSH"]
  #teams_selected = []
  puts "Has the NFL Regular Season started? (Answer either 'y' or 'n')"
  while teams_selected.length() == 0 do
    resp = gets.chomp
    if resp == "y"
      puts "Which teams have you selected? Please enter them one at a time. Input 'done' when finished. Input 'h' for accepted team abbreviations."
      new_team = ""
      until new_team == "DONE"
        new_team = gets.chomp.upcase
        if team_abbreviations.include? new_team
          if teams_selected.include? new_team
            puts "#{new_team} has already been added to the 'ignore' list. Select a different team, or input 'done' to calculate odds."
          else
            teams_selected << new_team
            puts "So far #{teams_selected} will be removed from possible choices. Input another team to continue. Input 'done' to calculate season."
          end
        elsif new_team == "H"
          puts "Here are the acceptable abbreviations: \n #{abbreviaton_to_full_team} \nPlease select a team: "
        elsif new_team == "DONE"
          next
        else
          puts "Did not recognize #{new_team}. Please try again. Input 'h' for accepted team abbreviations"
        end
      end
      teams_selected
    elsif resp == "n"
      puts "Okay! Starting from scratch then."
      teams_selected << "None"
      teams_selected
    else
      puts "Please enter either 'y' or 'n' to proceed"
    end
  end
end

weeks_played()
puts teams_selected
if teams_selected == ["None"]
  puts "it worked"
end