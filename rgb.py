
'''

YOU WILL NEED A hej.json FILE IN THE SAME FOLDER AS THE CODE
PASTE THIS IN IT:


{
  "chroma": {
    "developerName": "Your name",
    "developerContact": "Your email",
    "category": "application",
    "supportedDevices": ["keyboard"],
    "description": "Basic hello world sketch",
    "title": "Hello world!"
  }
}



'''



from pychroma import Sketch
import cryptocompare
oldprice = 0



class MySketch(Sketch):
    config_path = 'hej.json'
    def setup(self):
        self.oldprice = 0
        self.constraints = ((1, 21), (0, 5))
        self.frame_rate = 30
        self.keyboard.color_mode('rgb')
        self.r = 0
        self.g = 0
        self.b = 0

    def update(self):
        self.r = 255
        self.g = 0
        price = cryptocompare.get_price('BTC')['BTC']['EUR']
        if float(price) > float(self.oldprice):
            self.r = 0
            self.g = 255
        self.oldprice = price
    def render(self):
        for i in range(self.constraints[1][0], self.constraints[1][1] + 1):
            for j in range(self.constraints[0][0], self.constraints[0][1] + 1):
                self.keyboard.set_grid((j, i), (self.r, self.g, self.b))