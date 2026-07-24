class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = []
        for (let s of strs) {
            res.push(s.length, '#', s)
        }

        return res.join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const res = []
        let i = 0;
        while (i < str.length) {
            let j = i
            while (str[j] !== '#') {
                j++
            }

            let endOfString = parseInt(str.substring(i,j))+1
            res.push(str.substring(j+1, j+endOfString))
            i = j+endOfString
        }

        return res
    }
}
