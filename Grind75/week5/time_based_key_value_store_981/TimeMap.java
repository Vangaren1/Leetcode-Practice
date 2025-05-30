package Grind75.week5.time_based_key_value_store_981;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

class TimeMap {

    public Map<String, TreeMap<Integer, String>> myMap;

    public TimeMap() {
        myMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        myMap.computeIfAbsent(key, k -> new TreeMap<>()).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        TreeMap<Integer, String> tmp = myMap.get(key);
        if( tmp == null){
            return "";
        }
        Map.Entry<Integer, String> tMap = tmp.floorEntry(timestamp);
        if ( tMap == null){
            return "";
        }
        return tMap.getValue();
    }

    public static void main(String[] args) {
        System.out.println("Running time_based_key_value_store_981...");
    }
}
