class TimeMap {
    
    class Pair {
        String value = "";
        int timestamp = 0;
        Pair (String a, int b) {
            value = a;
            timestamp = b;
        }
    }
    
    HashMap<String, ArrayList<Pair>> hm;

    public TimeMap() {
        hm = new HashMap<String, ArrayList<Pair>>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (hm.containsKey(key))
        {
            hm.get(key).add(new Pair(value, timestamp));
        }
        else
        {
            ArrayList<Pair> al = new ArrayList<Pair>();
            al.add(new Pair(value, timestamp));
            hm.put(key, al);
        }
    }
    
    public String get(String key, int timestamp) {
        String out = "";
        if (hm.containsKey(key))
        {
            ArrayList<Pair> al = hm.get(key);
            int l = 0;
            int h = al.size() - 1;
            while (l <= h)
            {
                int mid = (h-l)/2 + l;
                Pair p = al.get(mid);
                if (p.timestamp == timestamp)
                {
                    return p.value;
                }
                else if (p.timestamp < timestamp)
                {
                    out = p.value;
                    l = mid + 1;
                }
                else
                {
                    h = mid - 1;
                }
            }
        }
        return out;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */