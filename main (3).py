def   linearsearchproduct(productlist,targetproduct):
  indeces=[]
  for index, product in enumerate     (productlist):
    if product==targetproduct:
      indeces.append(index)
  return indeces  
products=                             ["bangles","chain","earings","bangles","ring","bangles"]
target="bangles" 
target2="saree"
result=linearsearchproduct(products,target)
print(result)       