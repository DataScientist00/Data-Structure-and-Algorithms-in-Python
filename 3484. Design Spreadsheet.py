# problem link-->> http://leetcode.com/problems/design-spreadsheet/description/

class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = {}
        
    def setCell(self, cell: str, value: int) -> None:
        self.matrix[cell] = value        

    def resetCell(self, cell: str) -> None:
        if cell in self.matrix:
            del self.matrix[cell] 

    def getValue(self, formula: str) -> int:
        # formula always like "=X+Y"
        assert formula.startswith('=')
        expr = formula[1:]  # remove '='
        a_str, b_str = expr.split('+')

        def resolve(tok: str) -> int:
            tok = tok.strip()
            if tok == "":
                return 0
            # If begins with digit => integer literal
            if tok[0].isdigit():
                return int(tok)
            # else cell reference
            return self.matrix.get(tok, 0)

        return resolve(a_str) + resolve(b_str)





# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
