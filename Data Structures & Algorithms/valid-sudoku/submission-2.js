class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const tracker = {}

        for (let row = 0; row < board.length; row++) {
            for (let col = 0; col < board[row].length; col++) {
                let currentNumber = board[row][col]
                if (currentNumber === ".") {
                    continue
                } 
                let currentCell = Math.floor(row / 3) * 3 + Math.floor(col / 3)
                console.log('cnum',currentNumber)
                console.log('row', row)
                console.log(currentCell)
                if (tracker[currentNumber] === undefined) {
                    tracker[currentNumber] = {
                        cells: {
                            [currentCell]: true
                        },
                        rows: {
                            [row]: true
                        },
                        cols: {
                            [col]: true
                        }
                    }
                } else {
                    let current = tracker[currentNumber]
                    if (!!current.cells[currentCell]) {
                        return false
                    } else {
                        current.cells[currentCell] = true
                    }

                    if (!!current.rows[row]) {
                        return false
                    } else {
                        current.rows[row] = true
                    }

                    if (!!current.cols[col]) {
                        return false
                    } else {
                        current.cols[col] = true
                    }
                }

            }
        }
        return true
    }
}
