#create class
class pair_elements:
  def twoSum(self,nums,target):
    #create an empty dictionary
    lookup={}

    #iterate thriugh the tuple
    for i, num in enumerate(nums):
      if target-num in lookup:
        return (lookup[target-num],i)
      lookup[num]=i

#take input from dum of the user
value=int(input("Enter the sum of which you want to make this search:"))
print("index1=%d,index2=%d"%pair_elements().twoSum((10,20,30,40,50,60,70),value))