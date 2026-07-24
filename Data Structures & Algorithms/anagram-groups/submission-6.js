class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let seen = {}

        for (let i = 0; i < strs.length; i++) {
            let s = strs[i]
            let keykey = s.split('').sort().join(',')
            if (seen[keykey] === undefined) {
                seen[keykey] = []
            }

            seen[keykey].push(s)
        }

        return Object.values(seen)
    }
}
