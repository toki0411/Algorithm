import java.util.HashMap;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i ++) {
            map.put(players[i], i);
        }
        for (int i = 0; i < callings.length; i ++) {
            int now_rank = map.get(callings[i]);
            int winner_rank = now_rank - 1;
            int loser_rank = now_rank;
            String tmp = players[winner_rank];
            players[winner_rank] = callings[i];
            players[loser_rank] = tmp;  
            
            map.remove(callings[i]);
            map.remove(tmp);
            map.put(callings[i], winner_rank);
            map.put(tmp, loser_rank);
        }
        return players;
    }
}