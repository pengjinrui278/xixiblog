"""Reproducible teaching diagrams for textbook chapters 9 and 10.
Run from the repository root: python scripts/physics_diagrams/chapters_09_10.py
Each diagram is schematic; curves explicitly marked are computed from formulas.
"""
from drawing import *
from pathlib import Path
import re

FIGS = {}
def done(d, chapter, anchor, caption, alt):
    d.save()
    FIGS.setdefault(chapter, []).append((anchor, figure(d.name, caption, alt, d.height)))

def dim(d, x1,y1,x2,y2,label,tx=None,ty=None,color=GRAY):
    d.line(x1,y1,x2,y2,color,1.7)
    if abs(y2-y1)<1:
        d.line(x1,y1-5,x1,y1+5,color); d.line(x2,y2-5,x2,y2+5,color)
    elif abs(x2-x1)<1:
        d.line(x1-5,y1,x1+5,y1,color); d.line(x2-5,y2,x2+5,y2,color)
    d.text(tx if tx is not None else (x1+x2)/2,ty if ty is not None else (y1+y2)/2-10,label,color=color)

def plusline(d,x1,x2,y,sign='+',color=RED):
    for x in range(int(x1),int(x2)+1,40): d.text(x,y,sign,color=color,weight='bold')

def radial(d,cx,cy,r1,r2,angles,color=BLUE):
    for a in angles:
        a=math.radians(a)
        d.arrow(cx+r1*math.cos(a),cy+r1*math.sin(a),cx+r2*math.cos(a),cy+r2*math.sin(a),color)

# 9.3: ring projection and integration into a disk.
d=Diagram('ch09-ring-disk','圆环轴线：横向抵消，轴向相加',height=730)
d.ellipse(220,250,55,112,stroke=RED,width=3)
d.line(110,250,575,250,GRAY,1.5,dash='5 6')
d.charge(220,138);d.charge(220,362)
d.text(180,115,'dq₁',color=RED);d.text(180,400,'dq₂',color=RED)
d.line(220,138,425,250,GRAY,dash='5 5');d.line(220,362,425,250,GRAY,dash='5 5')
d.circle(425,250,4,fill=INK);d.text(418,286,'P')
d.arrow(425,250,510,204,BLUE);d.arrow(425,250,510,296,BLUE)
d.text(531,189,'dE₂',weight='bold',color=BLUE);d.text(531,329,'dE₁',weight='bold',color=BLUE)
d.arrow(425,250,575,250,GREEN,4);d.text(585,235,'E',weight='bold',color=GREEN)
d.line(220,250,220,145,ORANGE);d.text(194,211,'R',color=ORANGE)
dim(d,220,420,425,420,'z',ty=448)
d.text(220,278,'O',anchor='end')
d.line(30,477,610,477,LIGHT)
d.text(35,514,'圆盘 = 一圈圈微小圆环',anchor='start',weight='bold')
d.ellipse(210,610,135,67,fill=LIGHT,stroke=ORANGE)
d.ellipse(210,610,85,42,stroke=RED,width=12)
d.ellipse(210,610,85,42,stroke=BG,width=4)
d.line(210,610,280,586,INK);d.text(242,575,'r')
d.line(293,600,365,575,GRAY);d.text(400,573,'厚度 dr',anchor='start')
d.text(400,619,'dq = σ · 2πr dr',anchor='middle')
d.text(320,700,'先对称分解，再把同向分量积分',color=GRAY)
done(d,9,'**短推导**：每个电荷元到轴上点的距离都是', '图9-1　圆环轴线上的对称叠加，以及把圆盘分成同心圆环的方法。图示 Q>0、z>0。','圆环上两个对称正电荷元到轴上P点，横向场分量抵消，合场向右；下图为圆盘分环。')

# Exercise 9.5.
d=Diagram('ch09-ex09-05','习题9.5：先定位观察点',height=620)
d.text(35,88,'① 延长线上：各场元同向',anchor='start',weight='bold')
d.line(75,165,350,165,RED,6);plusline(d,90,330,147)
d.circle(450,165,5,fill=INK);d.text(450,200,'P')
d.arrow(450,165,565,165,BLUE);d.text(575,150,'E',weight='bold',color=BLUE)
dim(d,75,213,350,213,'L = 15 cm',ty=247)
dim(d,350,115,450,115,'R = 5 cm',ty=100)
d.line(30,278,610,278,LIGHT)
d.text(35,320,'② 中垂线上：横向相消',anchor='start',weight='bold')
d.line(125,530,515,530,RED,6);plusline(d,145,495,563)
d.circle(320,400,5,fill=INK);d.text(294,392,'Q')
d.line(320,400,320,530,GRAY,dash='5 5')
d.text(351,478,'a = 5 cm',anchor='start')
d.line(200,530,320,400,GRAY,dash='5 5');d.line(440,530,320,400,GRAY,dash='5 5')
d.arrow(320,400,258,333,BLUE);d.arrow(320,400,382,333,BLUE)
d.arrow(320,400,320,337,GREEN,4)
d.text(320,356,'',color=GREEN)
d.text(408,370,'E 沿中垂线',color=GREEN,weight='bold',anchor='start')
d.text(320,603,'图示 λ>0；长度与箭头不按数值比例绘制',color=GRAY,size=20)
done(d,9,'**延长线上的点**：所有电荷元的场同向。','图9-2　习题9.5的两种几何位置。上图从近端量 R，下图从中点量 a。','正电细线延长线上P点场向右；中垂线上Q点对称分量抵消，合场向上。')

# Flux normal plus closed surface.
d=Diagram('ch09-flux','电通量：夹角取场与法线的夹角',height=650)
d.polyline([(125,250),(350,250),(450,160),(225,160),(125,250)],ORANGE,2,fill=LIGHT)
d.arrow(285,211,285,86,PURPLE);d.text(272,82,'n',weight='bold',color=PURPLE,anchor='end')
d.arrow(285,211,430,110,BLUE);d.text(455,111,'E',weight='bold',color=BLUE)
d.path('M 285 158 A 53 53 0 0 1 328 180',GRAY,2);d.text(315,146,'θ')
d.text(345,238,'dS',color=ORANGE)
d.text(320,310,'dΦ = E cosθ dS',size=26)
d.line(30,340,610,340,LIGHT)
d.text(35,381,'闭合面：穿入为负，穿出为正',anchor='start',weight='bold')
d.circle(320,498,92,stroke=PURPLE,width=2)
for y in [455,498,541]:
    d.arrow(90,y,235,y,BLUE);d.arrow(240,y,390,y,BLUE);d.arrow(405,y,555,y,BLUE)
d.text(154,425,'穿入 −',color=BLUE);d.text(490,425,'穿出 +',color=BLUE)
d.text(320,625,'面内无电荷：净通量为零，但 E 不为零',size=22)
done(d,9,'闭合曲面的法线统一向外：','图9-3　开放面先选法线；闭合面统一取外法线。下图均匀场穿过一个球面，进出通量相抵。','上图电场与面积外法线夹角theta；下图均匀电场穿入和穿出无电荷球面。')

# Exercise 9.14, exact normalized curve.
d=Diagram('ch09-ex09-14','习题9.14：球对称，不必均匀',height=690)
d.circle(250,215,123,fill=LIGHT,stroke=ORANGE,width=3)
d.circle(250,215,78,stroke=PURPLE,width=2)
d.circle(250,215,42,stroke=RED,width=8)
d.line(250,215,373,215,ORANGE);d.text(329,202,'R',color=ORANGE)
d.line(250,215,206,151,PURPLE);d.text(201,166,'r',color=PURPLE)
d.text(430,151,'ρ(s) = ks²',anchor='middle')
d.text(470,199,'薄球壳：',anchor='middle');d.text(470,235,'dV = 4πs²ds',anchor='middle')
d.line(281,185,370,270,RED);d.text(455,292,'半径 s，厚度 ds',color=RED)
d.text(250,365,'紫色圆：球形高斯面的截面',color=PURPLE,size=21)
d.line(30,390,610,390,LIGHT)
d.text(35,430,'k>0 时的归一化场强曲线',anchor='start',weight='bold')
ox,oy=92,610; sx,sy=175,140
d.arrow(ox,oy,580,oy,INK,2);d.arrow(ox,oy,ox,449,INK,2)
pts=[]
for i in range(251):
    x=i/100
    y=x**3 if x<=1 else 1/x**2
    pts.append((ox+sx*x,oy-sy*y))
d.polyline(pts,BLUE,3)
d.line(ox+sx,oy,ox+sx,oy-sy,GRAY,dash='5 5')
d.text(ox+sx,641,'1');d.text(565,644,'r/R')
d.text(145,461,'E/E(R)',size=21)
d.text(180,560,'∝ r³',color=BLUE);d.text(410,532,'∝ 1/r²',color=BLUE)
d.text(320,677,'球内先算包围电荷；球外包住全部电荷',color=GRAY,size=21)
done(d,9,'电荷仍然球对称，所以取半径 $r$ 的同心球面。','图9-4　习题9.14的薄球壳分割及按正文公式绘制的场强曲线。r=R 处两段连续。','非均匀带电球内部取球形高斯面，薄球壳为积分元；下方场强随r先三次增长再平方反比下降。')

# Exercise 9.24.
d=Diagram('ch09-ex09-24','习题9.24：场相消，电势相加',height=470)
cx,cy=310,235
points=[(190,115),(430,115),(430,355),(190,355)]
d.polyline(points+[points[0]],GRAY,2,dash='6 5')
for x,y in points:
    d.charge(x,y);d.text(x,y-27 if y<cy else y+46,'+q',color=RED)
    d.line(x,y,cx,cy,GRAY,1.5,dash='4 5')
    dx,dy=cx-x,cy-y; length=math.hypot(dx,dy)
    d.arrow(cx,cy,cx+dx/length*65,cy+dy/length*65,BLUE)
d.circle(cx,cy,4,fill=INK);d.text(cx-17,cy-14,'O')
d.text(425,205,'r = 5 cm',size=22)
d.text(320,431,'中心：E = 0；U = 4kₑq/r > 0',size=25)
done(d,9,'由对称性，中心的场强相互抵消为零；','图9-5　习题9.24。中心处四个电场矢量两两抵消，四个正电势贡献仍然相加。','正方形四角各有正电荷，中心四个对角线方向电场相抵，中心电势为正。')

# Exercise 9.28.
d=Diagram('ch09-ex09-28','习题9.28：逐个判断壳内、壳外',height=490)
cx,cy=220,242
d.circle(cx,cy,140,stroke=ORANGE,width=3);d.circle(cx,cy,47,stroke=RED,width=3)
d.line(95,cy,525,cy,GRAY,1.5,dash='5 5')
d.circle(cx,cy,4,fill=INK);d.text(cx-18,cy+31,'O')
d.circle(cx+94,cy,5,fill=BLUE);d.text(cx+94,cy-21,'a',color=BLUE)
d.circle(cx+235,cy,5,fill=GREEN);d.text(cx+235,cy-21,'b',color=GREEN)
d.text(220,84,'外壳：R₂ = 0.30 m，+Q₂',color=ORANGE)
d.text(220,175,'内壳 +Q₁',color=RED)
d.text(47,324,'R₁ = 0.10 m',anchor='start',color=RED)
d.line(172,303,188,273,RED)
dim(d,cx,410,cx+94,410,'rₐ = 0.20 m',tx=225,ty=397)
dim(d,cx,455,cx+235,455,'rᵦ = 0.50 m',ty=481)
done(d,9,'$a$ 在小球壳外、大球壳内；','图9-6　习题9.28的球壳截面，半径按同一比例绘制。a 在两壳之间，b 在两壳外。','内壳半径0.1米、外壳半径0.3米，a距中心0.2米，b距中心0.5米。')

# Equipotential diagram.
d=Diagram('ch09-potential','等势面与电场：看变化率，不看绝对高低',height=370)
for x,u in [(120,30),(250,20),(380,10),(510,0)]:
    d.line(x,120,x,290,ORANGE,2,dash='7 5');d.text(x,98,f'{u} V',color=ORANGE)
for y in [153,218,273]: d.arrow(70,y,568,y,BLUE,2.5)
d.text(570,198,'E',weight='bold',color=BLUE)
d.rect(250,218,13,13,stroke=INK,width=1.5)
d.text(320,335,'虚线：等势面的截线；蓝箭头：电场方向',size=21)
done(d,9,'等势面上 $\\mathrm dU=0$，所以非零电场垂直等势面。','图9-7　均匀电场的等势面。等距离对应相同电势差，电场由高电势指向低电势。','四个等间距的竖直等势面截线依次30、20、10、0伏，电场水平向右并与等势面垂直。')

# Dipole torque.
d=Diagram('ch09-dipole','电偶极子：偶极矩从负电荷指向正电荷',height=470)
for y in [100,366]:d.arrow(70,y,570,y,BLUE,2)
d.text(590,95,'E',weight='bold',color=BLUE)
d.line(210,294,390,174,GRAY,3)
d.arrow(260,261,347,203,PURPLE,4);d.text(280,211,'pₑ',weight='bold',color=PURPLE)
d.charge(210,294,'-');d.charge(390,174,'+')
d.arrow(192,294,92,294,RED,4);d.text(129,277,'F₋',weight='bold',color=RED)
d.arrow(409,174,515,174,RED,4);d.text(471,154,'F₊',weight='bold',color=RED)
d.line(300,234,402,234,GRAY,1.5,dash='4 5')
d.path('M 344 234 A 44 44 0 0 0 337 210',GRAY,2);d.text(365,223,'θ')
d.symbol(489,293,'in',PURPLE,15);d.text(489,334,'τ 向纸内',weight='bold',color=PURPLE)
d.text(320,415,'合力为零，力矩使偶极子顺时针转向电场',size=22)
d.text(320,449,'稳定取向：pₑ 与 E 同向',color=GRAY,size=22)
done(d,9,'放入**均匀**外电场时，两端受力等大反向，','图9-8　倾斜电偶极子在匀强场中的力与力矩。叉乘给出的力矩朝纸内，对应顺时针转动。','负电荷在左下、正电荷在右上，外电场向右，正电荷受力右、负电荷受力左，力矩向纸内。')

# 10.1: conductor response and cavity.
d=Diagram('ch10-conductor','静电平衡：材料内部的合电场为零',height=700)
d.rect(185,112,270,165,fill=LIGHT,stroke=GRAY,radius=20)
for y in [145,195,245]:
    d.text(204,y,'−',color=BLUE,weight='bold');d.text(435,y,'+',color=RED,weight='bold')
d.arrow(237,170,400,170,BLUE);d.text(320,150,'E₀',color=BLUE,weight='bold')
d.arrow(400,230,237,230,PURPLE);d.text(320,260,"E′",color=PURPLE,weight='bold')
d.text(320,94,'外场向右，电子向左重排',size=22)
d.text(320,315,"内部：E = E₀ + E′ = 0",size=24)
d.line(30,341,610,341,LIGHT)
d.text(35,382,'腔内有 +q：内表面必须感应 −q',anchor='start',weight='bold')
d.circle(230,520,105,fill=LIGHT,stroke=GRAY,width=3);d.circle(230,520,67,fill=BG,stroke=GRAY)
d.charge(230,520)
for a in [0,60,120,180,240,300]:
    t=math.radians(a)
    d.text(230+76*math.cos(t),527+76*math.sin(t),'−',color=BLUE,weight='bold')
    d.text(230+116*math.cos(t),527+116*math.sin(t),'+',color=RED,weight='bold')
radial(d,230,520,23,57,[30,90,150,210,270,330])
d.text(448,454,'导体总电荷为 0',size=22)
d.text(450,501,'金属内 E = 0',size=24)
d.line(380,512,321,538,GRAY)
d.text(450,556,'外表面总电荷 +q',size=22,color=RED)
d.text(320,676,'空腔里可以有场；“零场”说的是导体材料',size=22)
done(d,10,'静电屏蔽的关键是导体的静电平衡和闭合外壳。','图10-1　上图用外加场和感应场的相消表示静电平衡；下图为未接地、中性导体的带电空腔截面。','导体内外加场向右、感应场向左而总场零；空腔含正电荷时内表面负电、外表面正电，金属内仍无场。')

# Exercise 10.2: two panels.
d=Diagram('ch10-ex10-02','习题10.2：连接前后，电荷重新分布',height=800)
for i,cy in enumerate([225,574]):
    d.text(35,85 if i==0 else 437,'① 未连接' if i==0 else '② 用细导线连接',anchor='start',weight='bold')
    d.circle(225,cy,115,fill=LIGHT,stroke=GRAY,width=3)
    d.circle(225,cy,105,fill=BG,stroke=GRAY)
    d.circle(225,cy,55,fill=LIGHT,stroke=GRAY,width=2)
    if i==0:
        for a in [0,90,180,270]:
            t=math.radians(a)
            d.text(225+46*math.cos(t),cy+7+46*math.sin(t),'+',color=RED,weight='bold')
            d.text(225+92*math.cos(t),cy+7+92*math.sin(t),'−',color=BLUE,weight='bold')
    else:d.line(225,cy-55,225,cy-105,INK,4)
    for a in [0,90,180,270]:
        t=math.radians(a);d.text(225+127*math.cos(t),cy+7+127*math.sin(t),'+',color=RED,weight='bold')
    d.circle(283,cy-58,5,fill=PURPLE);d.text(295,cy-73,'P',color=PURPLE)
    d.text(225,cy+7,'A',weight='bold')
    d.text(380,cy-93,'B',anchor='start',weight='bold')
    if i==0:
        d.text(475,cy-41,'A：+q',color=RED)
        d.text(475,cy+2,'B内侧：−q',color=BLUE)
        d.text(475,cy+45,'B外侧：+q',color=RED)
        d.text(320,386,'Rₐ=0.10 m；Rᵦ=0.20 m；OP=0.15 m',size=22)
    else:
        d.text(475,cy-35,'净电荷全在',size=23)
        d.text(475,cy+4,'最外表面',size=23)
        d.text(475,cy+49,'内部等势',color=PURPLE)
        d.text(320,762,'P点电势：600 V → 450 V',size=25)
d.line(30,407,610,407,LIGHT)
done(d,10,'**未连接**：壳的内、外表面分别感应','图10-2　习题10.2。连接前球壳内外感应电荷等量异号；连接后整个系统成为一个导体。','两同心导体连接前内球正电、壳内负电壳外正电，连接后只有最外表面带电；观察点在两导体之间。')

# Metal slab.
d=Diagram('ch10-metal-slab','思考题10.6：只有真空间隙产生电势降',height=440)
d.rect(110,139,390,9,fill=RED,stroke=RED);d.rect(110,341,390,9,fill=BLUE,stroke=BLUE)
plusline(d,130,480,125);plusline(d,130,480,380,'−',BLUE)
d.rect(110,221,390,49,fill=LIGHT,stroke=GRAY)
plusline(d,130,480,213,'−',BLUE);plusline(d,130,480,292,'+',RED)
for x in [165,305,445]:d.arrow(x,153,x,201,BLUE);d.arrow(x,298,x,335,BLUE)
d.text(305,253,'金属内 E = 0',size=23)
dim(d,550,143,550,345,'d',tx=575,ty=254)
dim(d,65,221,65,270,'t',tx=44,ty=252)
d.text(320,419,'总有效间隙 d − t，电容增大',size=24)
done(d,10,'设原间距 $d$，插入板厚 $t<d$，且不接触两极板。','图10-3　中性金属板上表面感应负电、下表面感应正电。金属内部没有电势降。','正负平行极板之间插入厚度t的金属，电场仅在上下真空间隙内向下，总电势降距离为d减t。')

# Polarization micro + macro.
d=Diagram('ch10-polarization','极化：分子尺度的响应与表面束缚电荷',height=670)
d.text(35,83,'① 无极分子：正负中心发生相对偏移',anchor='start',weight='bold')
d.circle(140,177,47,fill=LIGHT,stroke=GRAY);d.text(140,185,'±',size=30)
d.text(140,255,'无外场',color=GRAY)
d.arrow(215,177,306,177,GRAY)
d.ellipse(433,177,85,48,fill=LIGHT,stroke=GRAY)
d.charge(397,177,'-');d.charge(467,177,'+')
d.arrow(385,110,485,110,BLUE);d.text(510,117,'E',color=BLUE,weight='bold')
d.arrow(411,235,454,235,PURPLE);d.text(485,243,'pₑ',color=PURPLE,weight='bold')
d.line(30,292,610,292,LIGHT)
d.text(35,336,'② 均匀极化：内部抵消，边界留下电荷',anchor='start',weight='bold')
d.rect(130,391,380,157,fill=LIGHT,stroke=GRAY,radius=8)
for y in [430,493]:
    for x in [195,290,385,480]:
        d.line(x-29,y,x+7,y,GRAY)
        d.charge(x-29,y,'-',r=12);d.charge(x+7,y,'+',r=12)
d.arrow(220,579,416,579,PURPLE);d.text(445,586,'P',color=PURPLE,weight='bold')
d.arrow(130,468,66,468,GRAY);d.text(65,450,'n',weight='bold',color=GRAY)
d.arrow(510,468,574,468,GRAY);d.text(574,450,'n',weight='bold',color=GRAY)
d.text(109,378,'−σ′',color=BLUE);d.text(531,378,'+σ′',color=RED)
d.text(320,640,'P 向外的一端为正，向内的一端为负',size=22)
done(d,10,'### 3.3 束缚电荷的正负如何判断','图10-4　位移极化与均匀极化的示意。偶极矩从负电荷指向正电荷；边界符号由 P 与外法线的点乘确定。','分子正负中心在外场中分离；多个偶极子平均向右排列，介质左端负束缚电荷右端正束缚电荷。')

# Coaxial exercise.
d=Diagram('ch10-ex10-17','习题10.17：内表面的外法线指向轴线',height=640)
cx,cy=243,251
d.circle(cx,cy,160,fill=LIGHT,stroke=GRAY,width=3)
d.circle(cx,cy,145,fill='#edf4ee',stroke=GRAY,width=2)
d.circle(cx,cy,61,fill=LIGHT,stroke=GRAY,width=3)
for a in [45,135,225,315]:
    t=math.radians(a)
    d.text(cx+49*math.cos(t),cy+7+49*math.sin(t),'+',color=RED,weight='bold')
    d.text(cx+72*math.cos(t),cy+7+72*math.sin(t),'−',color=BLUE,weight='bold')
    d.text(cx+132*math.cos(t),cy+7+132*math.sin(t),'+',color=RED,weight='bold')
    d.text(cx+153*math.cos(t),cy+7+153*math.sin(t),'−',color=BLUE,weight='bold')
d.text(cx,cy+7,'轴线')
d.arrow(cx+78,cy,cx+128,cy,PURPLE,3)
d.text(457,241,'E、D、P',weight='bold',color=PURPLE)
d.text(474,274,'均沿径向',size=22)
d.line(cx,cy,cx,cy-61,GRAY);d.text(cx+28,cy-72,'R₁',color=GRAY)
d.line(cx,cy,cx,cy+145,GRAY);d.text(cx+24,cy+112,'R₂',color=GRAY)
d.text(243,448,'圆柱形电容器的横截面',color=GRAY)
d.line(30,471,610,471,LIGHT)
d.text(35,510,'介质区域：R₁ < r < R₂',anchor='start',weight='bold')
d.arrow(203,555,133,555,GRAY);d.text(216,563,'内表面 n',weight='bold',anchor='start')
d.text(480,563,'σ′ < 0',color=BLUE)
d.arrow(133,608,203,608,GRAY);d.text(216,616,'外表面 n',weight='bold',anchor='start')
d.text(480,616,'σ′ > 0',color=RED)
done(d,10,'取半径 $r$、长 $l$ 的同轴柱面，','图10-5　习题10.17。金属电极上的自由电荷与介质边界的束缚电荷成对相邻。底部外法线示意取右侧截点。','同轴圆柱横截面，内电极正电外电极负电，介质内边界束缚负电外边界正电，右侧介质内表面外法线向左。')

# Boundary geometry and components.
d=Diagram('ch10-boundary','界面条件：法向看 D，切向看 E',height=590)
d.rect(38,91,564,206,fill='#f4eee5',stroke='none');d.rect(38,297,564,210,fill='#e9f2f7',stroke='none')
d.line(38,297,602,297,GRAY,2)
d.text(74,129,'介质1',anchor='start');d.text(74,166,'ε₁ = 2ε₂',anchor='start',color=ORANGE)
d.text(74,350,'介质2',anchor='start')
d.line(302,116,302,483,GRAY,1.5,dash='5 5')
d.arrow(551,236,551,351,GRAY);d.text(575,291,'n',weight='bold',color=GRAY)
d.arrow(302,297,423,207,BLUE,4);d.text(455,202,'E₁',weight='bold',color=BLUE)
d.arrow(181,477,302,297,BLUE,4);d.text(161,475,'E₂',weight='bold',color=BLUE)
# E1 and E2 arrows along the same physical direction (up-right), lengths scaled for En1=En2/2.
d.line(423,207,423,297,ORANGE,1.8,dash='5 4')
d.arrow(302,297,423,297,GREEN,2.5)
d.text(384,331,'相同切向分量',color=GREEN,size=21)
d.text(400,420,'无自由面电荷',size=22)
d.text(400,463,'D₁ₙ = D₂ₙ',size=24)
d.text(320,551,'E₁ₜ = E₂ₜ；较大 ε 内，场更偏离法线',size=22)
done(d,10,'把场分成垂直界面的**法向分量**和沿界面的**切向分量**。','图10-6　无自由面电荷的介质界面。图示 ε₁=2ε₂，切向场不变，介质1中的法向场减半。','水平介质界面，上方介电常数为下方两倍，场从下左到上右，切向分量相等而上方法向分量较小。')

# Side-by-side media, exercise 10.15.
d=Diagram('ch10-ex10-15','习题10.15：并排介质承受同一电压',height=500)
d.rect(110,143,205,210,fill='#f4eee5',stroke=GRAY);d.rect(315,143,205,210,fill='#e9f2f7',stroke=GRAY)
d.rect(100,133,430,10,fill=RED,stroke=RED);d.rect(100,353,430,10,fill=BLUE,stroke=BLUE)
plusline(d,125,510,119);plusline(d,125,510,393,'−',BLUE)
d.text(212,185,'εᵣ₁ = 4',color=ORANGE);d.text(418,185,'εᵣ₂ = 6',color=BLUE)
d.text(212,221,'面积 S/2');d.text(418,221,'面积 S/2')
d.arrow(212,245,212,321,BLUE,3);d.text(245,289,'E₁',weight='bold',color=BLUE)
d.arrow(418,245,418,321,BLUE,3);d.text(451,289,'E₂',weight='bold',color=BLUE)
dim(d,568,138,568,358,'d',tx=590,ty=257)
d.text(50,258,'U',weight='normal')
d.text(320,441,'U = 15 V；d = 3 mm；S = 20 cm²',size=22)
d.text(320,477,'E₁ = E₂；D₂ > D₁，P₂ > P₁',size=24)
done(d,10,'令 $\\mathbf n$ 从正极板指向负极板。两块介质并排，','图10-7　习题10.15。两块介质左右并排，相当于两个电容器并联；场平行于介质分界面。','两平行板左右各填一半介电常数4和6的介质，上正下负、两区电场同样向下，两介质共同承受15伏。')

# Separation under fixed Q and fixed U; explicit switches.
d=Diagram('ch10-ex10-27','习题10.27：拉大板距前，先看电源',height=700)
for row,cy in enumerate([195,484]):
    title='① 电源断开：Q 不变' if row==0 else '② 保持接电源：U₀ 不变'
    d.text(35,85 if row==0 else 374,title,anchor='start',weight='bold')
    top,bottom=cy-55,cy+55
    d.line(130,top,430,top,RED,6);d.line(130,bottom,430,bottom,BLUE,6)
    plusline(d,155,405,top-14);plusline(d,155,405,bottom+30,'−',BLUE)
    d.arrow(279,top-5,279,top-51,GREEN);d.arrow(279,bottom+5,279,bottom+51,GREEN)
    d.text(450,cy-15,'外力拉开',color=GREEN)
    d.text(470,cy+23,'d → 2d')
    # Supply circuit enters at left, and switch only exists in first row.
    d.line(130,top,70,top,INK);d.line(70,top,70,cy-18,INK)
    d.line(53,cy-18,87,cy-18,INK,3);d.line(61,cy+4,79,cy+4,INK,3)
    d.text(40,cy-29,'+',size=22);d.text(38,cy+17,'−',size=22)
    d.line(70,cy+4,70,bottom,INK)
    if row==0:
        d.line(70,bottom,84,bottom,INK);d.circle(87,bottom,3,fill=INK)
        d.line(88,bottom,111,bottom-23,INK)
        d.circle(116,bottom,3,fill=INK);d.line(119,bottom,130,bottom,INK)
    else:d.line(70,bottom,130,bottom,INK)
    d.text(50,cy+61,'U₀',size=21)
    d.text(320,326 if row==0 else 615,'场能增加；外力功 = CU₀²/2' if row==0 else '电荷回流电源；外力功 = CU₀²/4',size=22)
d.line(30,345,610,345,LIGHT)
d.text(320,672,'缓慢拉开：外力与极板间吸引力等大反向',size=22,color=GRAY)
done(d,10,'**情况一：拉开前断电。**','图10-8　习题10.27的两种电路条件。上图开关断开，电荷不变；下图闭路，电源维持电压。','平行板向外拉开，上图电源开关断开维持电荷，下图连着电源维持电压；外力做功不同。')

# Insert semantic figures immediately before their teaching anchors.
for chapter, entries in FIGS.items():
    path=ROOT/'src/content/posts'/f'physics-{chapter:02}.md'
    text=path.read_text(encoding='utf-8-sig')
    # Regeneration is idempotent and changes only this script's named diagrams.
    text=re.sub(r'\n<figure class="physics-figure">\n  <a href="/images/physics/ch(?:09|10)-[\s\S]*?</figure>\n', '', text)
    for anchor,html in entries:
        if text.count(anchor)!=1:raise ValueError(f'Anchor not unique: {chapter} {anchor}')
        text=text.replace(anchor,html+'\n'+anchor,1)
    path.write_text(text,encoding='utf-8')
print('Created and inserted',sum(map(len,FIGS.values())),'diagrams')
