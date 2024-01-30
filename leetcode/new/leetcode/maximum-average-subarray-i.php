class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function findMaxAverage($nums, $k) {
        $sum = 0;
        for ($i = 0; $i < $k; ++$i) {
            $sum += $nums[$i];
        }
        $maxSum = $sum;

        $size = count($nums);
        for ($i = $k; $i < $size; ++$i) {
            $sum = $sum + $nums[$i] - $nums[$i - $k];
            if ($sum > $maxSum) {
                $maxSum = $sum;
            }
        }

        return $maxSum / $k;
    }
}