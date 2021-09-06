# myClasses
myClasses inheriting from standard Python (meta) Classes


**xList** adds a few extra functions to those inherited by list. 

`xList.rest(arg)` - returns all values not identical to value

`xList.update_rm(arg)` - updates and returns list removing all instances of value

`xList.indxs(arg)` - returns all indexes of value (cf. Python *list.index()* only gives first position)

`xList.items()` - returns a set of the xList

`xList.wildcard(arg)` - if xList is strings only, returns all instances featuring wildcard<br/><br/>


**xDict** adds a function to Python dict

`xDict.reap(arg)` - returns a zero (or preset class variable) instead of `None` from standard dict

`xDict.modify(arg)` - permits different return values to be set according to instance
