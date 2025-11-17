import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        char [] str = s.toCharArray();
        if (simulate(str) == true) {
                answer += 1;
        }
        
        for (int i = 1 ; i < s.length(); i ++) {
            char tmp = str[0];
            for (int j = 1; j < s.length(); j++) {
                str[j-1] = str[j];
            }
            str[s.length() - 1] = tmp;
            
            if (simulate(str) == true) {
                answer += 1;
            }
        }
        return answer;
    }
    static boolean simulate(char [] str){
        Stack<Character> st = new Stack<>();
        boolean key = true;
        for (char c : str){
            if (c == '(' || c == '{' || c == '['){
                st.add(c);
            }
            else if (c == ')') {
                if (!st.isEmpty()){
                    char t = st.pop();
                    if (t != '(') {
                        key = false; 
                        break;
                    }
                }else {
                    key = false; 
                    break;
                }
            }else if (c == '}') {
                if (!st.isEmpty()){
                    char t = st.pop();
                    if (t != '{') {
                        key = false; 
                        break;
                    }
                }else {
                    key = false; 
                    break;
                }
            }else if (c == ']') {
                if (!st.isEmpty()){
                    char t = st.pop();
                    if (t != '[') {
                        key = false; 
                        break;
                    }
                }else {
                    key = false; 
                    break;
                }
            }
        }
        if (!st.isEmpty() || !key) return false;
        return true;
    }
}