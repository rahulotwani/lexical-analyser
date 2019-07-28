class NFA_for_ID():  
    def _init_(self, data):
        self.data = data
        self.nextState = None
        self.pos = 0
        self.res = "Not-Valid"

    def switch(self, s):
        if s==0:
            # Epsilon tarnsition
            self.nextState = 1
        elif s==1:
            # the a case
            c = self.data[self.pos]
            self.pos += 1

            if c.isalpha():
                self.nextState = 2
            else:
                # Terminate NFA
                self.nextState = None
        elif s==2:
            # Epsilon tarnsition
            self.nextState = 3
        elif s==3:
            # the (a|b)* case
            try:
                c = self.data[self.pos]
                self.pos += 1

                if c.isalnum():
                    self.nextState = 3
                else:
                    # Terminate NFA
                    self.nextState = None
            except IndexError:
                self.nextState = 4
        elif s==4:
            # this means the string is a valid indentifier
            self.res = "Valid"
            self.nextState = None

    def checkID(self):
        if len(self.data) > 0:
            self.nextState = 0

            while self.nextState != None:
                self.switch(self.nextState)

            return self.res
        else:
            raise("Error: Token Size 0")

stt = "National Institute of Technolgy 123 DGP@gmail"

r = {}
for x in stt.split(" "):
	r[x] = NFA_for_ID(x).checkID()

print("Input String:", stt)
print("result: \n", r)