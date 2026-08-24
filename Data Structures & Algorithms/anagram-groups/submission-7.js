class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groups = strs.reduce((acc, s) => {
            let gKey = s.split('').sort().join('')
            if (!acc[gKey]) {
                acc[gKey] = []
            }
            acc[gKey].push(s)
            return acc
        }, {})

        return Object.values(groups)
    }
}
