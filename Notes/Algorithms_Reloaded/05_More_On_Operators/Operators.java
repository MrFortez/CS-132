

class Operators {
    
}

class Relational {

}

class Logical {

}

class Bitwise {

    // & is bitwise and
    // | is the bitwise or
    // ^ is the bitwise xor
    // ~ is for bitwise not
    // << is for left shift
    // >> is for right shift
}

class PrefixAndPostfix {
    public static void main(String[] args) {
        int i = 1;
        int j = 1;

        // postfix operator
        // 1. the ++ or -- after i is the operator
        // 2. adds or subtracts 1
        // 3. It returns i before we added 1
        
        int result_i = i++;
        System.out.println(result_i);
        
        // prefix operator
        // 1. the ++ or -- before j is the operator
        // 2. adds or subtracts 1
        // 3. It returns i after we added 1
        int result_j = ++j;
    }
}
