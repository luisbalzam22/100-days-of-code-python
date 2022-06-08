# f-strings also work outside a print() function
#-------example_start-------
def test(string_to_insert):
    return f"Hello {string_to_insert}"
test("World") # Hello World
#--------example_end--------

