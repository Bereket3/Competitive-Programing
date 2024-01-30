class Solution {

    /**
     * @param Integer[] $people
     * @param Integer $limit
     * @return Integer
     */
    function numRescueBoats($people, $limit) {
        sort($people);
        $left = 0;
        $right = sizeof($people) - 1;
        $out = 0;
        while ($right>= $left){
            if($people[$left] + $people[$right] <= $limit){
                $left++;
            }
            $out++;
            $right--;
        }
        return $out;
    }
}