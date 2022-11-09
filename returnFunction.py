def is_called():
    def is_returned():
        print('test')
    return is_returned

new = is_called()     # passes the function "is_returned" to "new"
                      # note the parentheses
new()