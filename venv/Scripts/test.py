import struct
class NutellaPacket:
    def __init__(self,id:int,secret_code:str,package_size:int,nutella_eater:str):
        self.id = id
        self.secret_code = secret_code
        self.package_size = package_size
        self.nutella_eater = nutella_eater
    def serialize(self):
        return struct.pack("!I"+str(len(self.secret_code))+"sI"+str(len(self.nutella_eater))+"s",self.id,self.secret_code.encode(),self.package_size,self.nutella_eater.encode())
WeZaElFaGeRXD = NutellaPacket(5240,"Networks",4096,"Mozoo")
print(struct.unpack("!I"+str(len(WeZaElFaGeRXD.secret_code))+"sI"+str(len(WeZaElFaGeRXD.nutella_eater))+"s",WeZaElFaGeRXD.serialize()))
