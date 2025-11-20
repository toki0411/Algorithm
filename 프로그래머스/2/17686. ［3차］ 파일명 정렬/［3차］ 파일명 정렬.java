import java.util.*;
class Solution {
    
    public ArrayList<String> solution(String[] files) {
        List<File> file = new ArrayList<>();
        for (String f : files){
            int idx = 0; int idx2 = f.length(); boolean key = false;
            for (int i = 0; i < f.length(); i++) {
                if (!key && Character.isDigit(f.charAt(i))){
                    idx = i;
                    key = true;
                }
                if (key && !Character.isDigit(f.charAt(i))){
                    idx2 = i;
                    break;
                }
            }
            String head = f.substring(0, idx).toUpperCase();
            String number = f.substring(idx, idx2);
            String tail = f.substring(idx2, f.length());        
            //System.out.println(number);
            file.add(new File(head, Integer.parseInt(number), tail, f));
        }
        file.sort((f1, f2) -> {
            int com = f1.head.compareTo(f2.head);
            if (com == 0) {
                return Integer.compare(f1.number, f2.number);
            }
            return com;
        });
        ArrayList<String> answer = new ArrayList<>();
        for (File f : file) {
            answer.add(f.origin);
        }
        return answer;
    }
    
    static class File {
        String head;
        int number;
        String tail;
        String origin;
        
        File (String head, int number, String tail, String origin) {
            this.head = head;
            this.number = number;
            this.tail = tail;
            this.origin = origin;
        }
        
    }
}