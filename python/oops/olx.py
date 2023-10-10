class Olx:

 vehicles=[   
      
 {"id":1,"name":"passionpro","year":2010,"selling_price":34000,"color":"black","location":"ekm"},
 {"id":2,"name":"cbz","year":2015,"selling_price":28000,"color":"red","location":"tsr"},
 {"id":3,"name":"alto","year":2000,"selling_price":100000,"color":"silver","location":"tsr"},
 {"id":4,"name":"reclassic350","year":2018,"selling_price":120000,"color":"grey","location":"ekm"},
 {"id":5,"name":"activa","year":2010,"selling_price":24000,"color":"black","location":"ekm"},         
 {"id":6,"name":"herohondasd","year":2000,"selling_price":80000,"color":"red","location":"tsr"}              
                
               
           ]
 
 def create(self,*args,**kwargs):
  self.vehicles.append(kwargs)
  print("vehicle added successfully")
  
 def get(self,*args,**kwargs):
  return self.vehicles
 def retrieve(self,id=None,*args,**kwargs):
  obj=[v for v in self.vehicles if v.get("id")==id][0]
  return obj
 def destroy(self,id=None,*args,**kwargs):
  obj=[v for v in self.vehicles if v.get("id")==id][0]
  obj.pop()
obj=Olx()
(obj.create(id=7,name="nano",year=2018,selling_price=70000,color="yellow",location="thrsr"))
print(obj.get())
# print(obj.retrieve(id=7))