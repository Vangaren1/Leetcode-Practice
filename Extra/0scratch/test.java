

// First, create a simple class so we can compare 2d points. 

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

class twoD{
    int x, y;
    public twoD(int[] p){
         x = p[0];
         y = p[1];
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true; // same object
        if (!(o instanceof twoD other)) return false;
        return x == other.x && y == other.y;
    }
    @Override
    public int hashCode(){
        return Objects.hash(x, y); 
    }
}

public int intersection(int[][] a, int[][] b){
    Set<twoD> setA = new HashSet<>();
    int count = 0;
    for ( int index= 0; index < a.length ; index++) {
        twoD tmp = new twoD(a[index]);
        setA.add(tmp);
    }

    for ( int index2 = 0;index2 < b.length; index2 ++) {
        twoD temp = new twoD(b[index2]);
        if ( setA.contains(temp)) count++;
    }
    return count;
}


public void colorSort(String[] bucket){
    int red=0;
    int white=0;
    int blue=0;

    for ( String tmp: bucket){
        switch (tmp){
            case "red":
                red++;
                break;
            case "white":
                white++;
                break;
            case "blue":
                blue++;
                break;
            default:
                break;
        }
    }
    int index = 0;
    for (int rTmp = 0; rTmp < red; rTmp++){
        bucket[rTmp] = "red";
    }
    index = red;
    for (int wTmp = 0; wTmp < white; wTmp++) {
        bucket[wTmp +index] = "white";
    }
    index = white + red;
    for (int bTmp = 0; bTmp < blue; bTmp++) {
        bucket[bTmp + index] = "blue";
    }

}