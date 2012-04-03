
import avl_template

frontwing = object()

class AC():
    def __init__(self):
        self.template = avl_template.template

    def avlFile(self):
        return self.template % {'fw_trans': self.frontwing.printTrans(),
                                'rw_trans': self.rearwing.printTrans()}

class Surface():
    def printTrans(self):
        return "%f %f %f" % (self.translate[0], self.translate[1], self.translate[2])


frontwing = Surface()
frontwing.translate = [-0.596, 0.0, -0.03]

rearwing = Surface()
rearwing.translate = [-0.596, 0.0, -0.03]

ac = AC()
ac.frontwing = frontwing
ac.rearwing = rearwing

print ac.avlFile()

