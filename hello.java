private static long getIntegerWithDigitsCount(int N) {
    long a=0;
    int c=1;
    String num=Integer.toString(N);
    for(int i=1;i<num.length();i++){
        if(num.charAt(i-1)==num.charAt(i)){
            c++;
        }
        else{
            
            a=a*10+c;
            a=a*10+Integer.parseInt(String.valueOf(num.charAt(i-1)));
            c=1;
        }
    }
    a=a*10+c;
    a=a*10+N%10;
    return a;

}
