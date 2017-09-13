class Builder:
      def BuildWall(self):
          pass
      def BuildDoor(self):
          pass
      def BuildWindow(self):
          pass
      def GetRoom(self):
          pass
 class ConcreteBuilder1(Builder):
     def __init__(self):
         self.__Room=[]
     def BuildWall(self):
         self.__Room.append("Builder1 Build the wall. ")
     def BuildDoor(self):
         self.__Room.append("Builder1 Build the door. ")
     def BuildWindow(self):
         self.__Room.append("Builder1 Build the window. ")
     def GetRoom(self):
         return self.__Room
 class ConcreteBuilder2(Builder):
     def __init__(self):
         self.__Room=[]
     def BuildWall(self):
         self.__Room.append("Builder2 Build the wall. ")
     def BuildDoor(self):
         self.__Room.append("Builder2 Build the door. ")
     def BuildWindow(self):
         self.__Room.append("Builder2 Build the window. ")
     def GetRoom(self):
         return self.__Room
 class Director:
     def __init__(self,Builder):
         self.__build=Builder
     def order(self):
         self.__build.BuildWall()        
         self.__build.BuildWindow()
         self.__build.BuildDoor()
 if __name__ == "__main__":
     
     builder1=ConcreteBuilder1()
     director=Director(builder1)
     director.order()
     print builder1.GetRoom()
 
     builder2=ConcreteBuilder2()
     director=Director(builder2)
     director.order()
     print builder2.GetRoom()
