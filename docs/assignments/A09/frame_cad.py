import cadquery as cq
C=4.93; W=1.0; T=0.25; D=0.375; GAP=0.875; SP=0.375; SPH=0.150
L=C+W
def plate():
    p=(cq.Workplane("XY").slot2D(L,W,0).extrude(T))          # full-radius ends
    p=p.faces(">Z").workplane().pushPoints([(-C/2,0),(C/2,0)]).hole(D)
    p=p.faces(">Z").workplane().pushPoints([(-0.465,0),(0.465,0)]).hole(SPH)
    return p
def spacer():
    return cq.Workplane("XY").circle(SP/2).circle(SPH/2).extrude(GAP)
pl=plate()
cq.exporters.export(pl,"A09_frame_plate.step")
a=cq.Assembly(name="A09_frame")
a.add(pl,name="plate_A",loc=cq.Location(cq.Vector(0,0,0)),color=cq.Color(0.75,0.76,0.78))
a.add(pl,name="plate_B",loc=cq.Location(cq.Vector(0,0,T+GAP)),color=cq.Color(0.75,0.76,0.78))
for i,x in enumerate((-0.465,0.465)):
    a.add(spacer(),name=f"spacer_{i+1}",loc=cq.Location(cq.Vector(x,0,T)),color=cq.Color(0.55,0.58,0.62))
a.save("A09_frame_assembly.step")
comp=a.toCompound()
cq.exporters.export(comp,"A09_frame_assembly.stl")
cq.exporters.export(comp,"iso.svg",opt={"width":1400,"height":700,"projectionDir":(1,-1.2,0.9),"showAxes":False,"strokeWidth":0.8})
bb=comp.BoundingBox();print(bb.xlen,bb.ylen,bb.zlen)
