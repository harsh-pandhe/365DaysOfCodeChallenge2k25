# 🎯 Day #47 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever felt like life throws a bunch of **negatives** at you, and you have to find the **best streak** to keep going? That’s exactly what **Kadane’s Algorithm** does—it finds the **maximum subarray sum** even in the midst of negative numbers! 📈  

## 📚 What I Did Today  
I implemented **Kadane’s Algorithm**, a powerful way to find the **maximum sum of a contiguous subarray** in **O(n) time**. 🚀  

### 📝 **Kadane's Algorithm Implementation**  

```python
# kadane_algorithm.py
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", max_subarray_sum(arr))
```

## 💡 Key Learning  
- **Kadane’s Algorithm** keeps track of the best sum while scanning the array in a **single pass (O(n) time)**.  
- If the sum becomes **negative**, we reset it—because a negative sum would only hurt the future subarray.  
- **Real-life analogy?** It’s like focusing on the best streak in life and **cutting off negativity** before it drags you down!  

## ✨ Extra Touch  
✅ **Handles both positive & negative numbers efficiently**  
✅ **Works in O(n) time, making it optimal**  
✅ **Can be modified to return the actual subarray as well!**  

## 🚀 Your Turn
Try modifying this to **return the actual subarray** that gives the max sum!  

---

#365DaysOfCode #CodingChallenge #KadaneAlgorithm #KeepPushing  