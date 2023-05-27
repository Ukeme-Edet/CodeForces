/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function (nums) {
    let bottom = 0,
        top = nums.length;
    let middle = bottom + Math.floor((top - bottom) / 2);
    while (bottom < top) {
        if (nums[middle] > 0) {
            while (nums[middle - 1] > 0 || !(nums[middle] > 0)) {
                if (nums[middle - 1] > 0) {
                    top = middle;
                    middle = bottom + Math.floor((top - bottom) / 2);
                } else {
                    bottom = middle;
                    middle = bottom + Math.floor((top - bottom) / 2);
                }
            }
            return middle;
        } else if (nums[middle] < 0) {
            while (nums[middle + 1] < 0 || !(nums[middle] < 0)) {
                if (nums[middle + 1] < 0) {
                    bottom = middle;
                    middle = bottom + Math.floor((top - bottom) / 2);
                } else {
                    top = middle;
                    middle = bottom + Math.floor((top - bottom) / 2);
                }
            }
            return nums.length - middle;
        } else {
            let topLeft = middle,
                bottomRight = middle,
                middleLeft = bottom + Math.floor((topLeft - bottom) / 2),
                middleRight = bottomRight + Math.floor((top - bottomRight) / 2);
            while (bottom < topLeft && bottomRight < top) {
                if (
                    nums[middleLeft - 1] < 0 &&
                    nums[middleLeft] === 0 &&
                    nums[middleLeft + 1] >= 0
                ) {
                    return nums.length - middleLeft;
                } else if (nums[middleLeft] < 0) {
                    bottom = middleLeft;
                    middleLeft = bottom + Math.floor((topLeft - bottom) / 2);
                } else if (nums[middleLeft] > 0 || nums[middleLeft] === 0) {
                    topLeft = middleLeft;
                    middleLeft = bottom + Math.floor((topLeft - bottom) / 2);
                }
                if (
                    nums[middleRight - 1] <= 0 &&
                    nums[middleRight] === 0 &&
                    nums[middleRight + 1] > 0
                ) {
                    return middleRight;
                } else if (nums[middleRight] > 0) {
                    top = middleRight - 1;
                    middleRight =
                        bottomRight + Math.floor((top - bottomRight) / 2);
                } else if (nums[middleRight] <= 0 || nums[middleRight] === 0) {
                    bottomRight = middleRight;
                    middleRight =
                        bottomRight + Math.floor((top - bottomRight) / 2);
                }
            }
            return -1; // No non-zero or non-negative numbers found
        }
    }
    return -1; // No non-zero or non-negative numbers found
};

maximumCount([5, 20, 66, 1314]);
