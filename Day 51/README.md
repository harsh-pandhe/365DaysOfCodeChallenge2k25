# 🎯 Day #51 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever tried opening a box, only to find another box inside... and another? **Nested lists** are like that—lists inside lists inside lists. Today’s challenge? **Flattening them into a single list!**  

## 📚 What I Did Today  
I wrote a function that **recursively** flattens a nested list, making it a single-level list.  

### 📝 **Flattening a Nested List Using Recursion**  

```python
def flatten_list(nested_list):
    """ Recursively flattens a nested list into a single-level list """
    flat_list = []
    
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    
    return flat_list

nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
flattened = flatten_list(nested_list)
print("Flattened List:", flattened)
```

## 💡 Key Learning  
- **Recursion makes handling unknown depths of nesting easy.**  
- **Using `isinstance(item, list)` ensures we only recurse when needed.**  
- **Extending the list (instead of appending) keeps it properly flattened.**  

## ✨ Extra Touch  
✅ **Handles any level of nested lists.**  
✅ **Works dynamically—doesn't need prior knowledge of the structure.**  
✅ **Super useful for data processing tasks!**  

## 🚀 Your Turn  
Try modifying this function to **handle nested tuples as well!**  

---

#365DaysOfCode #CodingChallenge #Recursion #FlattenLists  
