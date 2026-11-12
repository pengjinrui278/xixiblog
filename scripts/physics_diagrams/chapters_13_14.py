"""Original teaching diagrams for physics chapters 13 and 14.
Run from any directory with the bundled Python. No external assets.
"""
from drawing import *
from pathlib import Path
import math

FIGURES=[]
def done(d,caption,alt):
    d.save();FIGURES.append((d.name,caption,alt,d.height))

def ring_arrow(d,cx,cy,r,start,end,color=BLUE,width=3):
    # angles in mathematical orientation: positive angles are counterclockwise.
    pts=[(cx+r*math.cos(math.radians(a)),cy-r*math.sin(math.radians(a))) for a in [start+(end-start)*i/32 for i in range(33)]]
    d.polyline(pts,color,width,arrow=True)

def field_dots(d,xs,ys,kind='out',color=BLUE):
    for x in xs:
        for y in ys:d.symbol(x,y,kind,color,7)

def dimension(d,x1,y1,x2,y2,label,tx=None,ty=None):
    d.line(x1,y1,x2,y2,GRAY,1.5)
    if abs(y2-y1)<1:
        d.line(x1,y1-6,x1,y1+6,GRAY);d.line(x2,y2-6,x2,y2+6,GRAY)
    else:
        d.line(x1-6,y1,x1+6,y1,GRAY);d.line(x2-6,y2,x2+6,y2,GRAY)
    d.text(tx if tx is not None else (x1+x2)/2,ty if ty is not None else (y1+y2)/2+28,label,color=GRAY)

# CHAPTER 13

def ch13():
    d=Diagram('ch13-response','顺磁与抗磁：先比较磁化方向',height=520)
    d.text(38,82,'相同的局部 H，取向右为正',anchor='start',color=GRAY)
    for y,title,sign in [(130,'顺磁质：χₘ > 0',1),(310,'抗磁质：χₘ < 0',-1)]:
        d.rect(28,y-18,584,165,fill=LIGHT,stroke='none',radius=12)
        d.text(50,y+15,title,anchor='start',weight='bold')
        d.arrow(170,y+55,430,y+55,BLUE);d.text(475,y+63,'H',weight='bold',color=BLUE)
        if sign>0:d.arrow(170,y+105,265,y+105,RED)
        else:d.arrow(265,y+105,170,y+105,RED)
        d.text(310,y+113,'M',weight='bold',color=RED)
        d.text(420,y+113,'同向' if sign>0 else '反向',color=RED)
    d.footer('M = χₘH；为看清方向，图中磁化响应已放大。')
    done(d,'图13-1　顺磁与抗磁的区别是磁化响应方向；普通材料的响应通常很弱。','在相同向右磁场强度H下，顺磁材料磁化强度M向右，抗磁材料M向左。')

    d=Diagram('ch13-fields','B、H、M：先把单位统一再相加',height=470)
    d.text(320,84,'B / μ₀ = H + M',size=28,weight='bold')
    d.text(35,126,'示例：线性顺磁质，三个矢量同向',anchor='start',color=GRAY)
    d.arrow(100,185,360,185,BLUE);d.text(230,171,'H',weight='bold',color=BLUE)
    d.arrow(360,185,470,185,RED);d.text(415,171,'M',weight='bold',color=RED)
    d.line(100,205,100,275,GRAY,dash='5 5');d.line(470,205,470,275,GRAY,dash='5 5')
    d.arrow(100,285,470,285,PURPLE);d.text(285,322,'B / μ₀',weight='bold',color=PURPLE)
    d.text(320,380,'H、M、B / μ₀ 的单位均为 A/m')
    d.text(320,418,'决定磁力的场量仍是 B',weight='bold')
    d.footer('箭头示意矢量合成；不表示真实材料的比例。')
    done(d,'图13-2　B 与 H 的单位不同；将 B 除以 μ₀ 后，才能与 H、M 在同一尺度上作矢量相加。','上方首尾相接的蓝色H与红色M箭头之和，等于下方紫色B除以真空磁导率的箭头。')

    d=Diagram('ch13-solenoid','习题13.1：相同电流，比较空气与铁芯',height=600)
    for cy,label,fill in [(205,'空气：B₀ = μ₀nI',BG),(435,'铁芯：B = μ₀(H + M)',LIGHT)]:
        d.rect(120,cy-55,400,110,fill=fill,stroke=GRAY,radius=9)
        for x in range(145,511,30):d.ellipse(x,cy,10,68,stroke=ORANGE,width=2)
        d.rect(200,cy-20,260,40,fill=BG,stroke='none')
        d.arrow(210,cy,450,cy,BLUE);d.text(485,cy+8,'H',weight='bold',color=BLUE)
        d.text(320,cy-90,label,weight='bold')
        d.text(320,cy+105,'n、I 不变，因此 H = nI 相同')
    d.footer('长螺线管中部模型；线圈绕向选成内部 H 向右。')
    done(d,'图13-3　同样的匝密度和电流给出相同 H；加入铁芯后，材料磁化使 B 改变。','上下两个相同长螺线管，空气芯与铁芯中H均向右且大小相同。')

    d=Diagram('ch13-toroid','习题13.4：环形铁芯中的场与磁通',height=530)
    d.circle(320,265,150,fill=LIGHT,stroke=GRAY);d.circle(320,265,88,fill=BG,stroke=GRAY)
    for a in range(145,215,10):
        r=math.radians(a);d.line(320+87*math.cos(r),265+87*math.sin(r),320+151*math.cos(r+.06),265+151*math.sin(r+.06),ORANGE,3)
    ring_arrow(d,320,265,119,25,-45,BLUE,4);ring_arrow(d,320,265,119,200,130,BLUE,4)
    d.text(320,250,'B、H',weight='bold',color=BLUE);d.text(320,283,'沿环向')
    d.text(50,125,'N 匝',anchor='start',color=ORANGE);d.line(115,135,190,194,GRAY)
    d.text(504,294,'截面 S',anchor='start');d.line(497,282,450,263,GRAY)
    d.text(320,458,'平均磁路长 ℓ；H ≈ NI / ℓ')
    d.footer('理想细环：忽略漏磁，截面内 B 近似均匀。')
    done(d,'图13-4　环路沿铁芯中心绕一周；截面 S 与环向磁场垂直，磁通近似为 BS。','绕线环形铁芯的俯视图，蓝色箭头顺时针沿环向，标出绕组匝数N和铁芯截面S。')

    d=Diagram('ch13-domains','磁畴：未磁化不等于内部没有磁矩',height=600)
    for y,title,aligned in [(120,'宏观未磁化：各磁畴方向不同',False),(360,'外场磁化后：有利方向的磁畴扩展',True)]:
        d.text(320,y-25,title,weight='bold')
        d.rect(80,y,480,150,fill=LIGHT,stroke=GRAY)
        if not aligned:
            for x in [200,320,440]:d.line(x,y,x,y+150,GRAY)
            d.line(80,y+75,560,y+75,GRAY)
            directions=[0,90,180,270,225,45,135,315]
            for i,a in enumerate(directions):
                x=140+(i%4)*120;yy=y+37+(i//4)*75;r=math.radians(a)
                d.arrow(x-23*math.cos(r),yy+23*math.sin(r),x+23*math.cos(r),yy-23*math.sin(r),PURPLE)
        else:
            d.line(440,y,440,y+150,GRAY);d.line(440,y+75,560,y+75,GRAY)
            for x in [140,250,360]:
                for yy in [y+40,y+110]:d.arrow(x-25,yy,x+25,yy,PURPLE)
            d.arrow(480,y+53,520,y+23,PURPLE);d.arrow(480,y+110,520,y+130,PURPLE)
    d.arrow(400,300,550,300,BLUE);d.text(365,308,'H',weight='bold',color=BLUE)
    d.footer('分区和箭头为磁畴模型示意，并非显微照片。')
    done(d,'图13-5　未磁化时，各磁畴的磁矩相互抵消；磁化过程中，有利方向的磁畴扩展并转向。','上下两个分区矩形表示铁磁体，未磁化时各区箭头方向不同，施加向右H后多数磁畴箭头向右。')

    d=Diagram('ch13-hysteresis','磁滞回线：沿箭头读出磁化历史',height=570)
    d.arrow(70,280,575,280,INK,2);d.arrow(320,470,320,80,INK,2)
    d.text(588,288,'H',weight='bold');d.text(320,69,'B',weight='bold')
    d.path('M 510 125 C 420 125 380 170 320 170 C 245 170 235 260 235 280 C 220 375 190 430 130 435',RED,4)
    d.path('M 130 435 C 220 435 260 390 320 390 C 395 390 405 300 405 280 C 420 185 450 130 510 125',BLUE,4)
    d.arrow(384,147,352,161,RED);d.arrow(254,413,289,397,BLUE)
    for x,y in [(320,170),(320,390),(235,280),(405,280)]:d.circle(x,y,5,fill=INK,stroke=INK)
    d.text(354,194,'Bᵣ',color=RED);d.text(362,417,'−Bᵣ',color=BLUE)
    d.text(233,315,'−H꜀');d.text(409,315,'H꜀');d.text(300,309,'O')
    d.text(40,102,'H 逐渐减小',anchor='start',color=RED)
    d.text(395,466,'H 逐渐增大',color=BLUE)
    d.text(320,513,'同一个 H，可对应不同的 B',weight='bold')
    d.footer('示意曲线；Bᵣ 为剩磁，H꜀ 为矫顽力的大小。')
    done(d,'图13-6　从正向磁化状态减小 H，沿红色上支向左；反向磁化后再增大 H，沿蓝色下支向右。','BH磁滞回线，标出正负剩磁与矫顽力；上支箭头向左，下支箭头向右。')

    d=Diagram('ch13-boundary','磁场边界：Bn 连续，无面电流时 Ht 连续',height=520)
    d.rect(30,80,580,210,fill=LIGHT,stroke='none');d.line(30,290,610,290,GRAY,3)
    d.line(300,95,300,450,GRAY,1.5,dash='6 6')
    d.arrow(300,290,545,125,BLUE,4);d.arrow(205,455,300,290,BLUE,4)
    d.text(55,120,'介质 2：μ₂ > μ₁',anchor='start')
    d.text(55,340,'介质 1',anchor='start')
    d.text(335,103,'法线 n',weight='bold',color=GRAY)
    d.path('M 300 220 A 70 70 0 0 1 358 251',ORANGE,2);d.text(339,218,'θ₂',color=ORANGE)
    d.path('M 300 365 A 75 75 0 0 1 262 355',ORANGE,2);d.text(276,398,'θ₁',color=ORANGE)
    d.text(515,189,'B₂',weight='bold',color=BLUE);d.text(200,410,'B₁',weight='bold',color=BLUE)
    d.text(440,360,'进入更大 μ：');d.text(440,398,'偏离法线')
    d.footer('角度均对法线；界面无自由面电流。')
    done(d,'图13-7　进入磁导率较大的介质，磁感应线偏离法线；注意 θ 从法线量起。','磁感应线由下方低磁导率介质斜向上进入高磁导率介质后更加偏离竖直法线，标出入射角与折射角。')

    d=Diagram('ch13-gap','习题13.3：同一磁路中的铁芯与气隙',height=570)
    d.circle(320,265,150,fill=LIGHT,stroke=GRAY);d.circle(320,265,92,fill=BG,stroke=GRAY)
    d.rect(407,240,74,50,fill=BG,stroke='none')
    d.line(410,240,468,240,GRAY);d.line(410,290,468,290,GRAY)
    for a in range(150,211,10):
        r=math.radians(a);d.line(320+91*math.cos(r),265+91*math.sin(r),320+151*math.cos(r+.06),265+151*math.sin(r+.06),ORANGE,3)
    ring_arrow(d,320,265,121,120,65,BLUE,4)
    d.arrow(440,220,440,310,BLUE,4)
    d.text(320,253,'铁芯',weight='bold');d.text(320,290,'ℓFe = 0.60 m')
    d.text(55,145,'N = 1000',anchor='start',color=ORANGE);d.text(55,175,'I = 1.5 A',anchor='start',color=ORANGE)
    d.line(480,240,500,240,GRAY);d.line(480,290,500,290,GRAY);dimension(d,500,240,500,290,'g',tx=523,ty=272)
    d.text(485,350,'g = 0.01 m')
    d.text(320,458,'B铁 ≈ B气隙 = 0.18 T',weight='bold',color=BLUE)
    d.text(320,504,'H铁 ℓFe + H气隙 g = NI')
    d.footer('忽略漏磁与气隙边缘发散；图中气隙被放大。')
    done(d,'图13-8　忽略漏磁与发散时，铁芯和气隙中的 B 相同；H 因磁导率不同而不同，必须分段积分。','带右侧气隙的环形铁芯，蓝色磁场沿磁路顺时针跨越气隙，标出0.60米铁芯磁路和0.01米气隙。')

# CHAPTER 14

def ch14():
    d=Diagram('ch14-lenz','楞次定律：阻碍的是磁通变化',height=700)
    for cy,increase in [(215,True),(505,False)]:
        d.text(320,cy-115,'原磁场向外，正在增强' if increase else '原磁场向外，正在减弱',weight='bold')
        field_dots(d,[150,200,250],[cy-55,cy,cy+55])
        d.circle(200,cy,88,stroke=INK,width=3)
        if increase:ring_arrow(d,200,cy,99,70,-30,RED,4)
        else:ring_arrow(d,200,cy,99,-30,70,RED,4)
        d.text(420,cy-35,'感应电流 I',color=RED)
        d.text(420,cy+5,'顺时针' if increase else '逆时针',weight='bold',color=RED)
        d.symbol(378,cy+60,'in' if increase else 'out',PURPLE,15)
        d.text(422,cy+67,'B感',weight='bold',color=PURPLE)
        d.text(320,cy+130,'感应磁场向内，抵抗增加' if increase else '感应磁场向外，补偿减少')
    d.footer('正法线向外 ⊙，正绕向为逆时针；蓝色点表示原场。')
    done(d,'图14-1　原磁场都向纸外：增强时感应电流顺时针，减弱时则逆时针。','两个圆环中原磁场均向纸外；上图原场增强，感应电流顺时针产生向内场；下图原场减弱，电流逆时针产生向外场。')

    d=Diagram('ch14-moving-rod','习题14.5：先做叉乘，再沿杆积分',height=530)
    field_dots(d,[205,285,365,445,525],[125,200,365],'in',BLUE)
    d.line(110,90,110,390,INK,4);d.arrow(110,190,110,105,RED,4);d.text(77,145,'I',color=RED)
    d.line(240,255,555,255,ORANGE,10);d.text(240,231,'A',weight='bold');d.text(555,231,'B',weight='bold')
    d.charge(245,285,'+',13);d.charge(550,285,'−',13)
    d.arrow(395,241,395,160,GREEN,4);d.text(421,171,'v',weight='bold',color=GREEN)
    d.arrow(446,305,330,305,RED,4);d.text(387,345,'v × B',weight='bold',color=RED)
    d.text(565,125,'B',weight='bold',color=BLUE)
    dimension(d,110,396,240,396,'0.10 m');dimension(d,110,452,555,452,'1.0 m')
    d.footer('电流和运动向上；磁场入纸面 ⊗；A端电势高。')
    done(d,'图14-2　正电荷受 v×B 向左推，A端电势更高。各处磁场不同，应沿杆积分。','向上的长直电流右侧，AB横杆向上运动，磁场入纸面，v叉乘B向左；A距导线0.10米、B距导线1.0米。')

    d=Diagram('ch14-rotating-rod','转动杆：每一小段的速度都不同',height=520)
    field_dots(d,[120,230,340,450,560],[110,210,310,410],'out',BLUE)
    d.line(165,365,470,145,ORANGE,8);d.circle(165,365,8,fill=INK,stroke=INK)
    d.text(142,397,'O');d.text(565,82,'A（高电势）',anchor='end');d.line(515,94,478,137,GRAY,1.5)
    d.line(165,365,307,263,PURPLE,3);d.text(224,292,'r',color=PURPLE)
    d.line(297,280,319,250,RED,6);d.text(340,275,'dr',color=RED)
    d.arrow(307,263,250,183,GREEN,4);d.text(210,165,'v = ωr',color=GREEN,weight='bold')
    ring_arrow(d,165,365,75,-25,70,INK,3);d.text(413,354,'ω：逆时针')
    d.text(495,390,'B 向外',weight='bold',color=BLUE)
    d.text(320,467,'沿杆积分：ε = ∫ Bωr dr = Bωℓ² / 2')
    d.footer('从纸面正面观察；转轴与 B 同向，杆垂直转轴。')
    done(d,'图14-3　杆越靠外，速度越大；本图逆时针转动且磁场向外，正电荷被推向外端 A。','绕O逆时针转动的杆，磁场向纸外，标出径向位置r、线元dr及与杆垂直的速度v等于ωr。')

    d=Diagram('ch14-induced-field','涡旋电场：磁场外面也可以有电场',height=650)
    d.circle(320,275,130,fill=LIGHT,stroke=BLUE,width=2)
    field_dots(d,[260,320,380],[210,275,340],'out',BLUE)
    for r in [70,175]:
        d.circle(320,275,r,stroke=RED,width=2)
        ring_arrow(d,320,275,r,65,-10,RED,4)
    d.text(320,85,'B 向外且增大；Eᵢ 顺时针',weight='bold')
    d.line(320,275,450,275,BLUE,2);d.text(467,306,'R',color=BLUE)
    d.text(535,268,'Eᵢ',color=RED,weight='bold')
    d.text(320,488,'r ≤ R：|Eᵢ| = (r / 2) |dB / dt|')
    d.text(320,534,'r > R：|Eᵢ| = (R² / 2r) |dB / dt|')
    d.text(320,582,'外部 B ≈ 0，Eᵢ 仍可不为零',weight='bold')
    d.footer('蓝色圆域是磁场区域；红色圆是感生电场线。')
    done(d,'图14-4　对称模型中，磁场局限在蓝色圆域，感生电场却延伸到外部；其方向由磁通变化确定。','圆柱截面的蓝色磁场向外增强，内部和外部红色感生电场线都沿顺时针；标出区域半径R和内外场强公式。')

    d=Diagram('ch14-eddy-ring','思考题14.6：完整圆环与断口圆环',height=570)
    d.text(320,83,'从磁铁一侧看：N极正在靠近圆环',weight='bold')
    for cx,cut in [(175,False),(465,True)]:
        if cut:
            d.path(f'M {cx+66} 229 A 82 82 0 1 0 {cx+66} 325',ORANGE,8)
            d.text(cx,380,'有断口',weight='bold')
            d.text(cx,420,'无整环传导电流')
        else:
            d.circle(cx,277,82,stroke=ORANGE,width=8)
            ring_arrow(d,cx,277,105,-20,65,RED,4)
            d.text(cx,380,'完整导电环',weight='bold');d.text(cx,420,'感应电流逆时针',color=RED)
        field_dots(d,[cx-28,cx+28],[250,305],'in',BLUE)
    d.text(320,476,'原磁场向纸内且增强；完整环产生向外感应场')
    d.footer('有无闭合导线，都不改变变化磁场会产生电场这一事实。')
    done(d,'图14-5　从靠近的N极一侧观察，原磁场向纸内增强；完整环的感应电流逆时针，断口环没有整环持续传导电流。','左右两个圆环从靠近的磁铁N极一侧观察，原场入纸面。完整环有逆时针感应电流，右侧断口环没有整环电流。')

    d=Diagram('ch14-toroid','习题14.20：按半径分条求磁通',height=740)
    d.circle(320,205,125,fill=LIGHT,stroke=GRAY);d.circle(320,205,70,fill=BG,stroke=GRAY)
    for a in range(150,211,12):
        rr=math.radians(a);d.line(320+70*math.cos(rr),205+70*math.sin(rr),320+125*math.cos(rr+.06),205+125*math.sin(rr+.06),ORANGE,3)
    ring_arrow(d,320,205,97,70,0,BLUE,4)
    d.text(320,201,'N 匝',color=ORANGE);d.text(320,232,'俯视图')
    d.text(320,380,'矩形截面：面积元 dS = h dr',weight='bold')
    d.rect(160,425,330,115,fill=LIGHT,stroke=GRAY);d.rect(315,425,20,115,fill='#c6dbeb',stroke=BLUE)
    for x in [210,270,385,445]:d.symbol(x,480,'in',BLUE,9)
    d.line(90,560,520,560,INK,1.5);d.text(80,550,'O')
    dimension(d,90,585,160,585,'a');dimension(d,90,635,490,635,'b')
    dimension(d,525,425,525,540,'h',tx=553,ty=490)
    d.text(325,412,'dr',color=BLUE);d.text(405,605,'半径 r →')
    d.footer('a = 0.050 m，b = 0.10 m，h = 0.010 m；B ∝ 1/r。')
    done(d,'图14-6　把矩形截面分成宽 dr、高 h 的窄条；每条的磁场不同，先积分得单匝磁通，再乘匝数 N。','上方为空气环形螺线管俯视图，下方为径向矩形截面，标出内半径a、外半径b、截面高度h及面积元h乘dr。')

    d=Diagram('ch14-rl','RL 电路：电流连续建立，也连续衰减',height=760)
    # Closed series circuit; source represented by battery with + at top.
    d.line(100,125,260,125,INK,3);d.resistor(260,125,420,125);d.line(420,125,520,125,INK,3)
    d.line(520,125,520,185,INK,3)
    d.path('M 520 185 C 480 185 480 215 520 215 C 480 215 480 245 520 245 C 480 245 480 275 520 275',INK,3)
    d.line(520,275,520,315,INK,3);d.line(520,315,100,315,INK,3)
    d.line(100,125,100,210,INK,3);d.line(70,210,130,210,INK,3);d.line(84,231,116,231,INK,3);d.line(100,231,100,315,INK,3)
    d.text(52,209,'+');d.text(52,238,'−');d.text(48,280,'ε₀');d.text(340,98,'R');d.text(557,236,'L')
    d.arrow(160,125,220,125,RED,3);d.text(190,106,'I',color=RED)
    d.text(320,365,'接入恒定电源：I → ε₀ / R',weight='bold')
    # normalized curves
    d.arrow(95,645,570,645,INK,2);d.arrow(95,645,95,425,INK,2)
    d.text(77,421,'I');d.text(585,651,'t');d.line(95,450,555,450,GRAY,1.5,dash='5 5')
    d.text(55,457,'I∞');d.text(77,670,'0')
    grow=[];decay=[]
    for j in range(101):
        t=5*j/100;x=95+92*t;grow.append((x,645-195*(1-math.exp(-t))));decay.append((x,645-195*math.exp(-t)))
    d.polyline(grow,RED,3);d.polyline(decay,BLUE,3)
    d.line(187,645,187,450,GRAY,1.5,dash='4 4');d.text(187,675,'τ = L/R')
    d.text(430,493,'建立',color=RED);d.text(430,611,'衰减',color=BLUE)
    d.text(320,716,'衰减时：撤去电源，但 R、L 仍闭合')
    d.footer('曲线按归一化解绘制；切断成开路不能套同一衰减回路。')
    done(d,'图14-7　上方电路接恒定电源后，电流按红线建立；将电源替换为导线、保留闭合RL回路，电流按蓝线衰减。','上方是电源、电阻、电感串联电路，下方绘出电流指数上升及衰减曲线，时间常数为L除以R。')

    d=Diagram('ch14-mutual','习题14.21：大线圈的磁场穿过小环',height=560)
    d.circle(320,265,155,stroke=ORANGE,width=4);d.circle(320,265,151,stroke=ORANGE,width=1.5)
    d.circle(320,265,38,stroke=PURPLE,width=4)
    field_dots(d,[290,320,350],[235,265,295],'out',BLUE)
    ring_arrow(d,320,265,168,-25,35,RED,4);d.text(528,229,'I₁',color=RED)
    d.line(320,265,430,375,GRAY,1.5);d.text(489,432,'R = 0.20 m',color=GRAY)
    d.line(348,242,430,155,GRAY,1.5);d.text(468,136,'小环面积 s',color=PURPLE)
    d.text(175,95,'大线圈：N = 100',color=ORANGE)
    d.text(320,466,'小环置于中心附近，两环共面')
    d.text(320,505,'Φ₂₁ ≈ B中心 s；M = μ₀Ns / (2R)')
    d.footer('大线圈电流按逆时针为正，其中心磁场向外 ⊙。')
    done(d,'图14-8　小环位于大线圈中心附近时，可把穿过它的磁场近似为中心磁场；互感取决于几何与匝数。','共面的大圆线圈中央有一个小圆环，大线圈逆时针电流产生向纸外磁场，标出大线圈半径R及小环面积s。')


def insert_figures():
    byname={row[0]:figure(*row) for row in FIGURES}
    paths={13:ROOT/'src/content/posts/physics-13.md',14:ROOT/'src/content/posts/physics-14.md'}
    # Insert before a unique heading/paragraph; exercises are illustrated between prompt and solution.
    placements={
      13:[('ch13-response','### 思考题13.2'),('ch13-fields','**解题顺序：**'),
          ('ch13-solenoid','**解：**空气近似真空'),('ch13-toroid','**解：**用细环、截面磁场'),
          ('ch13-domains','### 4.2 看懂'),('ch13-hysteresis','### 4.3 软磁'),
          ('ch13-boundary','高磁导率软磁材料'),('ch13-gap','**解：**铁中磁路长')],
      14:[('ch14-lenz','有感应电动势不一定'),('ch14-moving-rod','**解：**导线右侧磁场'),
          ('ch14-rotating-rod','N匝平面线圈以角速度'),('ch14-induced-field','外部虽然 $B=0$'),
          ('ch14-eddy-ring','**解答：**完整导电环'),('ch14-toroid','**解：**环内磁场为'),
          ('ch14-rl','## 5. 互感'),('ch14-mutual','**解：**取小环位于')]
    }
    import re
    for chapter,path in paths.items():
        s=path.read_text(encoding='utf8')
        for name,anchor in placements[chapter]:
            s=re.sub(r'\n<figure class="physics-figure">(?:(?!</figure>).)*?/images/physics/'+re.escape(name)+r'\.svg(?:(?!</figure>).)*?</figure>\n', '', s, flags=re.S)
            if anchor not in s and anchor.replace('：**', '：** ') in s:
                anchor = anchor.replace('：**', '：** ')
            if anchor not in s:raise ValueError(f'Missing anchor {anchor}')
            s=s.replace(anchor,byname[name]+'\n'+anchor,1)
        path.write_text(s,encoding='utf8')

if __name__=='__main__':
    ch13();ch14();insert_figures()
    print(f'Generated and inserted {len(FIGURES)} chapter diagrams.')
