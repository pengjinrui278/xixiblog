from drawing import *
from pathlib import Path
import re

DOC=ROOT/'src/content/posts'
insertions=[]
def register(d,chapter,anchor,caption,alt,exercise=False):
    d.save();insertions.append((chapter,anchor,figure(d.name,caption,alt,d.height),exercise))
def label(d,x,y,s,color=INK):
    if '_' not in s:
        d.text(x,y,s,size=23,color=color,weight='bold')
    else:
        base, sub = s.split('_', 1)
        d.parts.append(f'<text x="{x}" y="{y}" font-size="23" text-anchor="middle" fill="{color}" font-weight="bold">{escape(base)}<tspan baseline-shift="sub" font-size="16">{escape(sub)}</tspan></text>')
def battery(d,x,y,label_text):
    d.line(x-24,y-8,x+24,y-8,width=3);d.line(x-12,y+8,x+12,y+8,width=3)
    d.text(x-38,y-8,'+',color=RED);d.text(x-38,y+22,'−',color=BLUE)
    d.text(x+40,y+8,label_text,anchor='start')
def capacitor(d,x,y):
    d.line(x-29,y-10,x+29,y-10,width=3);d.line(x-29,y+10,x+29,y+10,width=3)
    d.text(x+45,y+8,'C');d.text(x-45,y-4,'+',color=RED);d.text(x-45,y+29,'−',color=BLUE)
def ann_arrow(d,cx,cy,r,a1,a2,color=BLUE):
    pts=[(cx+r*math.cos(t),cy+r*math.sin(t)) for t in [a1+(a2-a1)*k/30 for k in range(31)]]
    d.polyline(pts,color=color,width=3,arrow=True)

# 11.1: microscopic drift and the normal component of current density.
d=Diagram('ch11-current-density','电流方向与穿过截面的分量',height=660)
d.text(28,82,'① 金属导体：正电流与电子漂移反向',anchor='start')
d.rect(75,125,490,145,fill='#f0ece3',stroke=GRAY,radius=15)
for x in [135,260,385,510]: d.charge(x,210,'−')
d.arrow(140,155,490,155,RED);label(d,320,140,'E、j',RED)
d.arrow(425,240,215,240,BLUE);label(d,320,260,'电子 v_d',BLUE)
d.line(35,310,605,310,GRAY,1)
d.text(28,354,'② 截面正法线 n 已选定',anchor='start')
d.line(245,410,245,590,GREEN,7);d.text(208,600,'截面',color=GREEN)
d.arrow(245,540,525,540,GREEN);label(d,562,579,'n、dS',GREEN)
d.arrow(245,540,480,410,RED);label(d,500,414,'j',RED)
d.line(480,410,480,540,GRAY,2,dash='6 6')
d.arrow(270,560,470,560,ORANGE);d.text(392,599,'j cosθ',color=ORANGE)
d.path('M 315 540 A 70 70 0 0 0 306 506',GRAY,2);d.text(333,522,'θ')
d.footer('点乘只计法向分量：I = ∫ j · dS。粗体字母表示矢量。')
register(d,11,'### 漂移速度怎样进入公式','图 11-1｜电子向左漂移，正电流向右；斜向电流穿过截面时只取法向分量。','上图电场与电流密度向右，电子漂移向左。下图电流密度与截面法线夹角θ，法向分量为j cosθ。')

# 11.4: same current, different cross-section.
d=Diagram('ch11-series-wire','习题 11.4：串接导线的电流与密度',height=470)
d.arrow(95,110,260,110,RED);d.arrow(365,110,535,110,RED)
d.text(320,95,'I = 1.3 A，两段相同',color=RED)
d.rect(75,180,245,140,fill='#e2e8ed',stroke=GRAY,width=3)
d.rect(320,200,245,100,fill='#e8c8a5',stroke=ORANGE,width=3)
d.text(190,165,'铝：d = 2.5 mm');d.text(444,185,'铜：d = 1.8 mm')
for y in [215,250,285]:d.arrow(110,y,280,y,BLUE,2)
for y in [213,231,250,269,287]:d.arrow(350,y,525,y,BLUE,2)
d.text(195,355,'截面较大');d.text(445,355,'截面较小')
d.text(320,404,'j = I / S：铜线中的电流密度更大',color=BLUE)
d.footer('箭头疏密表示电流密度；导线几何仅作示意。')
register(d,11,'### 习题 11.4','图 11-2｜串联导线中的总电流相同，细铜线的电流密度较大。','粗铝线与细铜线串接，电流均为1.3A；铝线直径2.5mm，铜线直径1.8mm。',True)

# 11.6: radial shell resistor.
d=Diagram('ch11-spherical-resistor','习题 11.6：球层面积随半径改变',height=540)
cx,cy=320,267
d.circle(cx,cy,158,fill='#e5f0e9',stroke=GREEN,width=3)
d.circle(cx,cy,75,fill=BG,stroke=ORANGE,width=3)
d.circle(cx,cy,116,stroke=ORANGE,width=9)
d.circle(cx,cy,116,stroke=BG,width=2)
for a in [-.65,.65,2.5,3.7,4.1,5.1]:
 d.arrow(cx+82*math.cos(a),cy+82*math.sin(a),cx+146*math.cos(a),cy+146*math.sin(a),BLUE,2)
d.circle(cx,cy,3,fill=INK);d.text(cx-18,cy+25,'O')
d.line(cx,cy,cx,cy-75,INK,2);d.text(cx+25,cy-35,'R₁')
d.line(cx,cy,cx+116,cy,ORANGE,2);d.text(cx+65,cy-14,'r',color=ORANGE)
d.line(cx,cy,cx-112,cy+112,INK,2);d.text(cx-79,cy+69,'R₂')
d.line(425,220,520,180,ORANGE,2);d.text(534,160,'薄层 dr',color=ORANGE)
d.text(320,465,'薄球层彼此串联：dR = ρ dr / (4πr²)')
d.footer('截面图：蓝箭头表示内壳电势较高时的径向电流。')
register(d,11,'### 习题 11.6','图 11-3｜电流穿过同心球面；半径越大，可通过的面积 4πr² 越大。','同心内外球壳半径R1和R2，半径r的薄球层厚度dr，电流沿径向向外。',True)

# Emf and terminal voltage, discharge convention.
d=Diagram('ch11-source-voltage','电源供电时：非静电作用把电荷送回高电势',height=560)
d.rect(70,135,230,310,fill='#f0ece3',stroke=GRAY,radius=12)
d.text(185,112,'电源内部')
d.line(185,135,500,135,width=3);d.line(500,135,500,230,width=3)
d.resistor(500,230,500,340);d.line(500,340,500,445,width=3);d.line(500,445,185,445,width=3)
d.text(548,293,'R')
d.text(315,146,'+',color=RED,weight='bold');d.text(315,454,'−',color=BLUE,weight='bold')
d.arrow(347,135,445,135,RED);d.text(396,117,'I',color=RED)
d.arrow(440,445,350,445,RED)
d.arrow(128,380,128,206,RED);label(d,128,191,'E_k',RED)
d.arrow(237,207,237,380,BLUE);label(d,237,411,'E',BLUE)
d.text(185,478,'电源：ε，内阻 r')
d.text(320,516,'端电压 U₊ − U₋ = ε − Ir')
d.footer('供电约定：I 从电源正极向外流出。')
register(d,11,'### 电动势不等于任何时候的端电压','图 11-4｜供电时电源内部的非静电作用向上输送正电荷，静电场反向；外电路从正极流向负极。','电源正极在上、负极在下，外接电阻R；非静电场向上，静电场向下，外电路电流从正极流出。')

# 11.10 three branches, all cells positive at top.
d=Diagram('ch11-three-branches','习题 11.10：三支路连接同一对节点',height=640)
for x in [120,320,520]:
 d.line(x,135,x,190,width=3);d.line(x,450,x,510,width=3)
d.line(120,135,520,135,width=3);d.line(120,510,520,510,width=3)
d.circle(320,135,5,fill=INK);d.circle(320,510,5,fill=INK)
d.text(320,113,'a');d.text(320,545,'b')
for x in [120,520]:
 d.resistor(x,190,x,260);d.line(x,260,x,308,width=3);battery(d,x,316,'ε₁' if x==120 else 'ε₃');d.line(x,324,x,380,width=3);d.resistor(x,380,x,450)
 d.text(x+40,231,'R₁');d.text(x+40,422,'R₁')
d.resistor(320,190,320,280);d.text(365,241,'R₂')
d.line(320,280,320,368,width=3);battery(d,320,376,'ε₂');d.line(320,384,320,450,width=3)
d.arrow(65,263,65,365,RED);d.text(42,318,'I₁',color=RED)
d.arrow(270,451,270,296,BLUE);d.text(244,350,'I₂',color=BLUE)
d.arrow(585,434,585,347,GREEN);d.text(604,398,'I₃',color=GREEN)
d.text(320,580,'R₁ = 1 Ω，R₂ = 2 Ω')
d.text(320,615,'ε₁ = 2 V，ε₂ = ε₃ = 4 V')
register(d,11,'### 习题 11.10','图 11-5｜按原题连接关系重绘。三电源正极均朝上，箭头与正文假设的电流方向一致。','三条并联支路，上节点a下节点b。左支路两个R1和电源ε1，电流向下；中支路R2和ε2、右支路两个R1和ε3，电流向上。',True)

# Separate charging and discharging circuits; no ambiguous switch position.
d=Diagram('ch11-rc-circuits','RC 的两种接线：充电与放电',height=760)
for base,title in [(0,'① 充电：接通电源'),(350,'② 放电：移去电源后闭合 R–C 回路')]:
 d.text(30,83+base,title,anchor='start')
 top=132+base;bot=305+base
 d.line(130,top,255,top,width=3);d.resistor(255,top,370,top);d.text(310,top-17,'R')
 d.line(370,top,510,top,width=3);d.line(510,top,510,210+base,width=3);capacitor(d,510,220+base);d.line(510,230+base,510,bot,width=3)
 d.line(510,bot,130,bot,width=3)
 if base==0:
  d.line(130,top,130,212,width=3);battery(d,130,220,'ε');d.line(130,228,130,bot,width=3)
  d.arrow(395,top,470,top,RED);d.text(420,top+36,'I',color=RED)
  d.text(320,345,'I = dq / dt；q 从 0 增加',color=RED)
 else:
  d.line(130,top,130,bot,width=3);d.arrow(470,top,395,top,BLUE);d.text(420,top+36,'I放',color=BLUE)
  d.text(320,695,'I放 = −dq / dt；原正极板的 q 减少',color=BLUE)
d.footer('两图分别表示开关完成切换后的完整连接，电容原正极板均在上。')
register(d,11,'### 从未充电开始充电','图 11-6｜充电时电流流入正极板；放电时电流从原正极板流出。两图是切换完成后的不同电路。','上图电源、电阻、电容串联充电，电流从电源正极流向电容上极板。下图电源移去，电容通过电阻放电，电流从上极板流出。')

# RC graphs, both charging voltage and decaying current.
d=Diagram('ch11-rc-curves','RC 指数变化：一个 τ 之后改变多少？',height=560)
x0,y0,sx,sy=85,390,91,235
d.arrow(x0,y0,580,y0,INK,2);d.arrow(x0,y0,x0,95,INK,2)
d.text(586,425,'t / τ');d.text(54,105,'比例');d.text(60,y0+8,'0');d.text(59,y0-sy+7,'1')
d.line(x0,y0-sy,555,y0-sy,GRAY,1,dash='5 5')
for i in [1,2,3,4,5]:
 d.line(x0+sx*i,y0,x0+sx*i,y0+6,INK);d.text(x0+sx*i,y0+31,str(i))
ptsup=[];ptsdown=[]
for i in range(101):
 t=i/20;ptsup.append((x0+sx*t,y0-sy*(1-math.exp(-t))));ptsdown.append((x0+sx*t,y0-sy*math.exp(-t)))
d.polyline(ptsup,RED,3);d.polyline(ptsdown,BLUE,3)
d.line(x0+sx,y0,x0+sx,130,GRAY,1,dash='5 5')
for val,col,lab,dy in [(.632,RED,'0.632',-12),(.368,BLUE,'0.368',30)]:
 yy=y0-sy*val;d.circle(x0+sx,yy,4,fill=col,stroke=col);d.text(x0+sx+43,yy+dy,lab,color=col)
d.text(400,130,'充电电压 / ε',color=RED)
d.text(360,335,'充电 I / I₀',color=BLUE)
d.text(320,476,'蓝线也表示放电时的 q / q₀ 与 I放 / I₀',color=BLUE)
d.text(320,516,'τ = RC：τ 越大，变化越慢')
register(d,11,'### 时间常数与能量','图 11-7｜充电电压逐渐上升，电流逐渐衰减；放电电荷也沿蓝线衰减。','归一化RC曲线，红线由0趋向1，蓝线由1趋向0；t等于τ时分别为0.632和0.368。')

# Lorentz force in the page with B out of page.
d=Diagram('ch12-lorentz-direction','同一个磁场：正负电荷的偏转相反',height=580)
for base,sgn,col in [(0,'+',RED),(235,'−',BLUE)]:
 d.text(35,84+base,'正电荷 q > 0' if sgn=='+' else '负电荷 q < 0',anchor='start',color=col)
 for x in [150,270,390,510]:
  for y in [130+base,245+base]:d.symbol(x,y,'out',PURPLE)
 cy=190+base;d.charge(285,cy,sgn);d.arrow(309,cy,440,cy,GREEN);label(d,461,cy+8,'v',GREEN)
 fy=cy+75 if sgn=='+' else cy-75;d.arrow(285,cy+(20 if sgn=='+' else -20),285,fy,col);label(d,335,fy,'F_B',col)
d.line(35,286,605,286,GRAY,1)
d.text(320,538,'⊙ B 垂直纸面向外；先判 v × B，再乘 q',color=PURPLE,weight='bold')
d.footer('此图速度向右：正电荷受力向下，负电荷受力向上。')
register(d,12,'几个直接结论：','图 12-1｜叉乘先给出正电荷受力方向，负电荷反向；磁力垂直于速度。','磁场垂直纸面向外，正负电荷速度均向右；正电荷的磁力向下，负电荷的磁力向上。')

# Finite straight wire P and Q.
d=Diagram('ch12-finite-wire','习题 12.3：有限导线的两个观察点',height=570)
xw,xp,top,bot=185,485,140,440;mid=(top+bot)/2
d.line(xw,top,xw,bot,INK,6);d.arrow(xw,355,xw,225,RED,4);d.text(157,220,'I',color=RED)
d.circle(xp,mid,4,fill=INK);d.circle(xp,top,4,fill=INK)
d.text(xp+30,mid+8,'P');d.text(xp+30,top+8,'Q')
d.line(xw,mid,xp,mid,GRAY,2,dash='5 6');d.line(xw,top,xp,top,GRAY,2,dash='5 6');d.line(xp,top,xp,mid,GRAY,2,dash='5 6')
d.text(335,mid-14,'a');d.text(525,218,'L/2')
d.line(xw,top,xp,mid,BLUE,2);d.line(xw,bot,xp,mid,BLUE,2)
d.text(335,205,'到 P 的位矢',size=20,color=BLUE)
d.line(95,top,95,bot,GRAY);d.line(85,top,105,top,GRAY);d.line(85,bot,105,bot,GRAY);d.text(70,mid,'L')
d.symbol(xp,mid+65,'in',PURPLE);label(d,430,mid+108,'B_P',PURPLE);d.text(505,mid+108,'向纸内',color=PURPLE)
d.symbol(xp,top-50,'in',PURPLE);label(d,390,top-42,'B_Q',PURPLE)
d.text(320,492,'P 在中垂线上；Q 与上端点同高')
d.footer('蓝线从源点指向观察点；本图按电流向上绘制。')
register(d,12,'### 习题 12.3','图 12-2｜先把 P、Q 与导线端点的位置画清，再确定积分上下限。','长度L的直导线电流向上，右侧距离a处的P与导线中点同高，Q在P上方L/2，与导线上端点同高；两点磁场均向纸内。',True)

# Loop axis field and circular arc element projections.
d=Diagram('ch12-loop-axis','圆线圈：横向分量抵消，轴向分量相加',height=540)
d.ellipse(185,275,58,125,stroke=INK,width=3)
d.line(100,275,570,275,GRAY,2,dash='5 5');d.arrow(185,275,320,275,GREEN);label(d,295,253,'p_m',GREEN)
d.circle(485,275,4,fill=INK);d.text(503,306,'P')
d.line(185,150,485,275,GRAY,1);d.line(185,400,485,275,GRAY,1)
d.arrow(485,275,530,167,BLUE);d.arrow(485,275,530,383,BLUE);label(d,560,159,'dB₁',BLUE);label(d,560,408,'dB₂',BLUE);d.symbol(185,150,'out',RED,10);d.symbol(185,400,'in',RED,10)
d.arrow(440,425,572,425,RED);label(d,506,455,'合场 B 沿轴线',RED)
d.text(325,310,'x');d.line(185,275,185,150,ORANGE,2);d.text(163,218,'R',color=ORANGE)
d.path('M 169 154 A 58 125 0 0 1 238 322',RED,3,arrow=True);d.text(267,195,'I',color=RED)
d.text(320,91,'从右侧沿轴线看：电流逆时针，磁矩向右')
d.text(320,494,'圆心：B = μ₀NI / (2R)')
d.footer('线圈透视示意；配对电流元产生的 dB 横向分量反向。')
register(d,12,'### 圆电流、圆弧和磁矩','图 12-3｜利用成对电流元的对称性，圆线圈轴线上只留下轴向磁场。','圆线圈轴线向右，磁矩向右；观察点P处成对磁场分量一上一下，横向抵消而轴向相加。')

# Flux vs circulation. Upper uniform B through closed surface, lower loop.
d=Diagram('ch12-flux-circulation','磁通看穿过面；环流看沿着路',height=710)
d.text(30,83,'① 闭合曲面：穿入与穿出相抵',anchor='start')
d.ellipse(320,225,155,100,fill='#eef4f8',stroke=GRAY,width=2)
for yy in [175,225,275]:d.arrow(80,yy,560,yy,BLUE,2)
label(d,565,154,'B',BLUE);d.text(120,345,'穿入：负');d.text(520,345,'穿出：正')
d.text(320,385,'闭合面的总磁通 = 0')
d.line(35,408,605,408,GRAY,1)
d.text(30,454,'② 闭合路径：B 与 dl 的切向关系',anchor='start')
d.circle(245,570,78,stroke=GREEN,width=2);d.symbol(245,570,'out',RED,16);d.text(245,612,'I 穿出纸面',color=RED)
ann_arrow(d,245,570,78,1.0,-.1,BLUE);label(d,355,561,'B、dl',BLUE)
d.text(440,645,'此绕向为逆时针',color=GREEN)
d.footer('闭面法线与回路切线是两种不同方向，不能混用。')
register(d,12,'### 安培环路定理','图 12-4｜磁通积分用面法线，环路积分用路径切线。下图电流穿出纸面，正绕向为逆时针。','上图均匀磁场从左穿入闭合曲面并从右穿出，净磁通为零；下图电流穿出纸面，磁场与逆时针环路切线同向。')

# Coaxial cable cross section with the four regions.
d=Diagram('ch12-coaxial-cable','习题 12.17：同轴电缆的四个区域',height=680)
cx,cy=320,272
d.circle(cx,cy,174,fill='#e8e2f0',stroke=PURPLE,width=3);d.circle(cx,cy,125,fill=BG,stroke=PURPLE,width=3);d.circle(cx,cy,67,fill='#f5e4df',stroke=RED,width=3)
for a in [k*math.pi/4 for k in range(8)]:d.symbol(cx+150*math.cos(a),cy+150*math.sin(a),'in',PURPLE,9)
for x,y in [(cx,cy),(cx-30,cy),(cx+30,cy),(cx,cy-30),(cx,cy+30)]:d.symbol(x,y,'out',RED,8)
for r,angle,lab in [(67,-math.pi/2,'a'),(125,0,'b'),(174,math.pi/4,'c')]:
 xx=cx+r*math.cos(angle);yy=cy+r*math.sin(angle);d.line(cx,cy,xx,yy,INK,1.5);d.text((cx+xx)/2+15,(cy+yy)/2-9,lab)
# Dashed Ampere loop has radius within outer conductor.
d.path(f'M {cx+142} {cy} A 142 142 0 1 0 {cx-142} {cy} A 142 142 0 1 0 {cx+142} {cy}',GREEN,2,dash='6 6')
ann_arrow(d,cx,cy,142,3.5,2.8,GREEN);d.text(86,238,'L',color=GREEN)
d.text(320,493,'⊙ 内导体 +I；⊗ 外导体 −I')
d.text(320,532,'r < a：只包住部分正向电流')
d.text(320,570,'a < r < b：包住全部 +I')
d.text(320,608,'b < r < c：再减去部分反向电流')
d.footer('r > c：净电流为零；本题的同轴对称性给出 B = 0。')
register(d,12,'### 习题 12.17','图 12-5｜截面中，外导体的回流方向与内导体相反；虚线环路示范如何计算包围电流。','同轴电缆截面，内圆半径a、电流出纸面，外圆筒内外半径b和c、电流入纸面；半径r的环路可位于四个区域。',True)

# Force on rectangular loop, strong attraction on the near edge.
d=Diagram('ch12-wire-loop-force','习题 12.25：近边吸力大于远边斥力',height=560)
xw,x1,x2,yt,yb=110,275,525,145,370
d.line(xw,95,xw,420,INK,5);d.arrow(xw,285,xw,180,RED,4);d.text(78,160,'I₁',color=RED)
d.rect(x1,yt,x2-x1,yb-yt,stroke=INK,width=3)
d.arrow(x1,315,x1,210,GREEN);d.arrow(x1+70,yt,x2-70,yt,GREEN);d.arrow(x2,210,x2,315,GREEN);d.arrow(x2-70,yb,x1+70,yb,GREEN)
d.text(x1+32,270,'I₂',color=GREEN)
d.arrow(x1,260,155,260,BLUE,4);d.text(195,236,'F近',color=BLUE,weight='bold')
d.arrow(x2,260,590,260,BLUE,3);d.text(573,236,'F远',color=BLUE,weight='bold')
d.arrow(400,yt,400,95,ORANGE);d.arrow(400,yb,400,420,ORANGE)
d.symbol(400,260,'in',PURPLE,13);label(d,403,305,'B',PURPLE)
for yy,xx,lab in [(451,x1,'x₁'),(492,x2,'x₂')]:
 d.line(xw,yy,xx,yy,GRAY);d.line(xw,yy-6,xw,yy+6,GRAY);d.line(xx,yy-6,xx,yy+6,GRAY);d.text((xw+xx)/2,yy-10,lab)
d.text(554,365,'l')
d.footer('横边受力上下相抵；两竖边的合力指向长直导线。')
register(d,12,'### 习题 12.25','图 12-6｜近边与长直导线电流同向，受到较大的吸力；远边受到较小的斥力。','左侧长直导线电流向上，右侧矩形线框电流顺时针。近竖边受力向左且大，远竖边受力向右且小，横边受力上下抵消。',True)

# Helix and velocity decomposition for exercise 12.35.
d=Diagram('ch12-particle-helix','习题 12.35：把斜速度拆成两个分量',height=720)
d.text(30,82,'① 分解：θ 是速度与磁场的夹角',anchor='start')
d.arrow(120,280,520,280,PURPLE);label(d,555,286,'B',PURPLE)
d.arrow(120,280,415,110,INK);label(d,439,116,'v',INK)
d.arrow(120,280,415,280,RED);label(d,280,315,'v∥',RED)
d.arrow(415,280,415,110,BLUE);label(d,447,204,'v⊥',BLUE)
d.path('M 197 280 A 77 77 0 0 0 187 242',GRAY,2);d.text(212,259,'30°')
d.line(35,345,605,345,GRAY,1);d.text(30,389,'② 合成：绕圈 + 沿轴匀速前进',anchor='start')
d.arrow(65,515,585,515,PURPLE);label(d,577,493,'B',PURPLE)
pts=[]
for k in range(241):
 t=4*math.pi*k/240;pts.append((105+420*t/(4*math.pi)+45*math.sin(t),515-75*math.cos(t)))
d.polyline(pts,BLUE,3,arrow=True)
d.line(210,515,210,590,ORANGE,2);d.text(237,570,'r',color=ORANGE)
d.line(105,627,315,627,GRAY,2);d.line(105,619,105,635,GRAY);d.line(315,619,315,635,GRAY);d.text(210,657,'一圈的轴向距离 h')
d.footer('r 由 v⊥ 决定；h = v∥T。下图为螺旋线投影示意。')
register(d,12,'### 习题 12.35','图 12-7｜垂直速度决定绕圈半径，平行速度决定每一圈前进的距离；题中夹角为 30°。','上图把与磁场成30度的速度分成平行和垂直分量，下图螺旋线沿磁场方向前进，标出半径r和螺距h。',True)

# Hall effect, electrons; use same axes and voltage convention as text.
d=Diagram('ch12-hall-effect','习题 12.37：铜片中的霍尔电荷分离',height=720)
d.text(30,82,'俯视铜片：B 沿 +z，垂直纸面向外',anchor='start')
d.rect(100,155,430,250,fill='#f4e2c9',stroke=ORANGE,width=3)
for x in [145,240,335,430,490]:
 d.text(x,185,'+',color=RED,size=28,weight='bold');d.text(x,390,'−',color=BLUE,size=28,weight='bold')
for x,y in [(145,250),(480,250),(145,330),(480,330)]:d.symbol(x,y,'out',PURPLE,10)
d.arrow(95,142,525,142,RED);d.text(320,125,'I 沿 +x',color=RED)
d.charge(320,278,'−');d.arrow(300,278,205,278,BLUE);label(d,237,257,'v_d',BLUE)
d.arrow(320,302,320,350,BLUE);label(d,373,347,'F_B',BLUE)
d.arrow(320,254,320,209,RED);label(d,374,226,'F_E',RED)
d.arrow(565,205,565,360,GREEN);label(d,588,285,'E_H',GREEN)
d.text(320,441,'上侧：缺少电子，电势高',color=RED)
d.text(320,476,'下侧：电子积聚，电势低',color=BLUE)
d.arrow(85,535,180,535,INK,2);d.text(200,544,'+x')
d.arrow(85,535,85,465,INK,2);d.text(56,458,'+y')
d.text(350,535,'宽 w 沿 y；厚 d 沿 z')
d.text(350,574,'本题 d = 1.0 mm（沿磁场）')
d.text(320,621,'平衡时：电力向上，磁力向下，合力为零')
d.text(320,664,'电压大小 |U_H| = IB / (ned)')
d.footer('这里画电子型导体；电荷正负与 E_H、F_E 的方向要分开。')
register(d,12,'### 习题 12.37','图 12-8｜按正文坐标约定绘制铜片。电子向左漂移，磁力把电子推向下侧；建立的霍尔电场向下，电子所受电力向上。','铜片电流沿正x向右，磁场沿正z出纸面，电子向左漂移，磁力向下；上侧正电荷高电势，下侧负电荷低电势。厚度d沿磁场。',True)

# Insert once; replacing an existing same-name figure makes reruns safe.
for ch,anchor,fig,exercise in insertions:
 p=DOC/f'physics-{ch}.md';s=p.read_text(encoding='utf-8')
 src=re.search(r'/images/physics/([^"/]+)\.svg',fig).group(1)
 pattern=r'\n<figure class="physics-figure">(?:(?!<figure).)*?'+re.escape(src)+r'\.svg(?:(?!<figure).)*?</figure>\n'
 s=re.sub(pattern,'\n',s,flags=re.S)
 idx=s.index(anchor)
 if exercise:
  ins=s.index('\n\n**解答',idx)
 else:
  ins=idx
 s=s[:ins]+fig+'\n'+s[ins:]
 p.write_text(s,encoding='utf-8')
print('Created and inserted',len(insertions),'diagrams')
