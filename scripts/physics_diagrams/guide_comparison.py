from drawing import *
import math

# Projection is kept separate from the normal-to-paper convention.
d=Diagram('guide-dot-product','点乘：只取沿另一个矢量方向的分量',height=390)
d.arrow(95,275,545,275,INK); d.text(560,284,'b',weight='bold')
d.arrow(95,275,380,110,BLUE); d.text(390,100,'a',color=BLUE,weight='bold')
d.line(380,110,380,275,GRAY,dash='6 6')
d.path('M 365 275 L 365 260 L 380 260',GRAY)
d.path('M 158 275 A 63 63 0 0 0 150 243',ORANGE)
d.text(172,251,'θ',color=ORANGE)
d.line(95,305,380,305,BLUE); d.line(95,298,95,312,BLUE);d.line(380,298,380,312,BLUE)
d.text(237,338,'a cos θ',color=BLUE)
d.text(70,300,'O')
d.footer('点乘的结果是标量；夹角超过 90° 时，投影为负。')
d.save()

# Right-handed x-y axes, z toward the viewer.
d=Diagram('guide-cross-product','叉乘：先判断 v × B，再乘电荷的正负号',height=450)
for cx,sign,fy in [(170,'+',355),(465,'−',155)]:
    for x,y in [(cx-80,140),(cx+70,140),(cx-80,340),(cx+70,340)]: d.symbol(x,y,'out',PURPLE)
    d.charge(cx,245,sign)
    d.arrow(cx+22,245,cx+115,245,ORANGE); d.text(cx+85,227,'v',color=ORANGE,weight='bold')
    d.arrow(cx,245+(22 if fy>245 else -22),cx,fy,GREEN)
    d.text(cx-24,fy+5,'F',color=GREEN,weight='bold')
    d.text(cx,90,'正电荷' if sign=='+' else '负电荷')
d.text(320,398,'⊙：B 向纸外；两图中的 v 均向右',color=PURPLE,weight='bold')
d.footer('右 × 外 = 下；负电荷所受磁力再反向。')
d.save()

# Generic flux and circulation comparison, reused by the beginner guide.
d=Diagram('comparison-flux-circulation','通量看穿面，环流看沿路径前进',height=660)
d.text(28,83,'① 通量：取法向分量',anchor='start',weight='bold')
d.path('M 175 285 L 385 285 L 465 235 L 255 235 Z',GRAY,2,fill='#f0ede4')
d.arrow(320,260,320,125,GREEN);d.text(307,115,'dS',color=GREEN,weight='bold',anchor='end')
d.arrow(320,260,430,152,BLUE);d.text(452,149,'A',color=BLUE,weight='bold')
d.path('M 320 209 A 51 51 0 0 1 356 224',ORANGE);d.text(343,196,'θ',color=ORANGE)
d.text(480,283,'面 S',color=GRAY)
d.text(320,324,'角度 θ 从法线量起，不从平面量起',size=22)
d.line(25,350,615,350,LIGHT)
d.text(28,388,'② 环流：取路径的切向分量',anchor='start',weight='bold')
d.circle(255,505,80,stroke=GRAY)
d.path('M 335 505 A 80 80 0 0 0 255 425',PURPLE,3,arrow=True)
d.arrow(330,494,330,419,PURPLE);d.text(359,443,'A',color=PURPLE,weight='bold')
d.arrow(352,505,352,460,GREEN);d.text(396,490,'dℓ',color=GREEN,weight='bold')
d.text(255,513,'闭合路径 L',size=21)
d.text(468,550,'先选绕行正向',size=22)
d.footer('面积矢量垂直于面；线元矢量沿着路径。')
d.save()

# Uniform polarized and magnetized rectangular bodies.
d=Diagram('comparison-bound-sources','极化留下束缚电荷；磁化留下束缚电流',height=650)
d.text(28,80,'① 均匀极化：表面电荷',anchor='start',weight='bold')
d.rect(160,120,320,145,fill='#edf3fa',stroke=BLUE,radius=3)
for y in (150,192,234):
    d.text(178,y,'−',color=BLUE,weight='bold');d.text(461,y,'+',color=RED,weight='bold')
for y in (158,223):d.arrow(250,y,390,y,BLUE)
d.text(320,196,'P',color=BLUE,weight='bold')
d.arrow(160,192,83,192,GREEN);d.text(83,170,'n',color=GREEN,weight='bold')
d.arrow(480,192,556,192,GREEN);d.text(556,170,'n',color=GREEN,weight='bold')
d.text(160,307,'负束缚电荷',color=BLUE);d.text(480,307,'正束缚电荷',color=RED)
d.line(25,340,615,340,LIGHT)
d.text(28,382,'② 均匀磁化：沿表面流动的电流',anchor='start',weight='bold')
d.rect(160,425,320,135,fill='#f1edf8',stroke=PURPLE,radius=3)
for x in (210,285,360,435):
    d.symbol(x,425,'out',PURPLE);d.symbol(x,560,'in',PURPLE)
d.arrow(250,495,393,495,PURPLE);d.text(320,478,'M',color=PURPLE,weight='bold')
d.arrow(505,425,505,399,GREEN);d.text(532,420,'n',color=GREEN,weight='bold')
d.arrow(505,560,505,596,GREEN);d.text(532,589,'n',color=GREEN,weight='bold')
d.text(81,502,'端面',size=21);d.text(81,533,'无电流',size=21)
d.text(320,607,'上表面 ⊙，下表面 ⊗',color=PURPLE,size=22)
d.footer('这里只标出上下表面的等效电流，方向按叉乘判定。')
d.save()

# Cross-section of two infinite line sources.
d=Diagram('comparison-line-sources','长直源的场：电场沿径向，磁场沿环向',height=420)
for cx,label in [(165,'正线电荷 λ > 0'),(475,'电流 I 向纸外')]: d.text(cx,90,label)
d.circle(165,235,82,stroke=GRAY,width=1.5)
d.charge(165,235)
for a in range(0,360,45):
    t=math.radians(a)
    d.arrow(165+36*math.cos(t),235-36*math.sin(t),165+122*math.cos(t),235-122*math.sin(t),BLUE)
d.text(277,208,'E',color=BLUE,weight='bold')
d.symbol(475,235,'out',RED,r=18)
d.circle(475,235,90,stroke=PURPLE,width=2.5)
for a in [0,90,180,270]:
    t=math.radians(a)
    x,y=475+90*math.cos(t),235-90*math.sin(t)
    tn=t+0.25
    xx,yy=475+90*math.cos(tn),235-90*math.sin(tn)
    d.path(f'M {x} {y} A 90 90 0 0 0 {xx} {yy}',PURPLE,3,arrow=True)
d.text(581,218,'B',color=PURPLE,weight='bold')
d.text(165,373,'圆柱高斯面求 E',color=BLUE)
d.text(475,373,'圆周环路求 B',color=PURPLE)
d.footer('这是垂直长直源的截面；两种场的大小均随 1/r 变化。')
d.save()

# Gaussian surface in a uniform field: entering and leaving portions balance.
d=Diagram('comparison-zero-flux','净通量为零，场可以处处不为零',height=400)
d.circle(320,220,106,fill='#f5f0e6',stroke=GRAY,width=2)
for y in (153,220,287):d.arrow(68,y,572,y,BLUE)
d.arrow(214,220,154,220,GREEN);d.arrow(426,220,486,220,GREEN)
d.text(164,198,'n',color=GREEN,weight='bold');d.text(478,198,'n',color=GREEN,weight='bold')
d.text(91,125,'E',color=BLUE,weight='bold');d.text(320,105,'不含电荷的闭合球面',size=22)
d.text(164,350,'左侧穿入：负',color=BLUE);d.text(475,350,'右侧穿出：正',color=BLUE)
d.footer('等量穿入与穿出相抵消；球面内、球面上仍有电场。')
d.save()

# Geometry shared by electric and magnetic interface conditions.
d=Diagram('comparison-boundary','边界条件：用小柱面取法向，用小回路取切向',height=600)
d.rect(28,90,584,195,fill='#f0f4f8',stroke='none')
d.rect(28,285,584,220,fill='#f4eee6',stroke='none')
d.line(28,285,612,285,GRAY,2)
d.text(515,126,'介质 2');d.text(515,475,'介质 1')
d.arrow(560,280,560,210,GREEN);d.text(584,217,'n',color=GREEN,weight='bold')
# Pillbox cross-section: top and bottom faces have opposite normals.
d.rect(95,245,150,80,fill='none',stroke=BLUE,width=2)
d.ellipse(170,245,75,14,stroke=BLUE);d.ellipse(170,325,75,14,stroke=BLUE)
d.arrow(170,244,170,170,BLUE);d.arrow(170,325,170,400,BLUE)
d.text(170,148,'薄小柱面',color=BLUE)
d.text(170,440,'上、下表面取通量',size=20)
# Thin rectangular path, clockwise relative to the screen.
d.rect(340,258,145,54,fill='none',stroke=PURPLE,width=2)
d.arrow(370,258,450,258,PURPLE);d.arrow(450,312,370,312,PURPLE)
d.text(414,180,'扁小矩形回路',color=PURPLE)
d.text(414,440,'长边取切向环流',size=20)
d.text(320,542,'柱面压薄；回路短边缩短',size=23)
d.footer('法线约定从介质 1 指向介质 2；“连续”针对相应分量。')
d.save()

# Analytic normalized step and relaxation curves (not measured data).
d=Diagram('comparison-transients','RC 与 RL：同一条归一化曲线，两种时间常量',height=450)
d.text(320,80,'建立除以稳态值；衰减除以初始值',size=21)
x0,y0,w,h=85,330,470,215
d.arrow(x0,y0,580,y0,INK);d.arrow(x0,y0,x0,95,INK)
d.text(575,367,'t / τ');d.text(54,105,'1')
d.line(x0,y0-h,x0+w,y0-h,GRAY,dash='5 5')
d.line(x0+w/4,110,x0+w/4,y0,GRAY,dash='5 5')
up=[];dn=[]
for i in range(161):
    t=4*i/160; x=x0+w*t/4
    up.append((x,y0-h*(1-math.exp(-t))));dn.append((x,y0-h*math.exp(-t)))
d.polyline(up,BLUE,3);d.polyline(dn,ORANGE,3)
d.circle(x0+w/4,y0-h*(1-math.exp(-1)),4,fill=BLUE,stroke=BLUE)
d.text(x0+w/4+20,y0-h*(1-math.exp(-1))-16,'0.632',color=BLUE,anchor='start')
d.text(x0+w/4,367,'1');d.text(449,154,'建立过程',color=BLUE);d.text(451,294,'衰减过程',color=ORANGE)
d.text(320,405,'RC 看电容电压；RL 看电感电流',size=22)
d.footer('解析示意：横轴分别用 τ = RC 或 τ = L/R 归一化。')
d.save()

# Insert exact, self-contained figure blocks once.
posts=ROOT/'src/content/posts'
entries={
'physics-guide.md':[
('点乘满足 $\\mathbf a\\cdot\\mathbf b=\\mathbf b\\cdot\\mathbf a$。','guide-dot-product','图导-1　斜向矢量在水平方向的投影，决定点乘的大小与正负。','矢量a斜向右上，b向右，垂足投影长度为a cos theta。',390),
('若是电子，则向上。','guide-cross-product','图导-2　相同速度和磁场下，正、负电荷的磁力方向相反。','磁场向纸外，速度向右；正电荷受力向下，负电荷受力向上。',450),
('开曲面先选法线，再用右手定则配套规定边界绕行方向。','comparison-flux-circulation','图导-3　一个对面求和，一个沿线求和；先看清微元的方向。','上图显示场与面法线的夹角；下图显示圆路径上沿切线的场与线元。',660)],
'physics-comparison.md':[
('通量累加**法向分量**，环流累加**切向分量**。两者都是标量，正负取决于所选方向。','comparison-flux-circulation','图比-1　通量与环流的几何对象和取分量方式不同。','面积微元垂直于面，路径微元沿切线；图示比较通量与环流。',660),
('都不要求整个场为零。','comparison-zero-flux','图比-2　零净通量的反例：没有包围电荷的球面仍可处于非零匀强场中。','均匀电场从球面左侧穿入、右侧穿出，两侧通量抵消。',400),
('非均匀极化或磁化时，内部也可能存在束缚源。','comparison-bound-sources','图比-3　同样是均匀响应，极化对应表面电荷，磁化对应表面电流。','均匀极化体左负右正；向右磁化的材料上表面电流向纸外、下表面向纸内。',650),
('用跨界面的扁小矩形回路消去短边贡献，得到切向条件。','comparison-boundary','图比-4　电学与磁学的边界关系，都可从这两种跨界面的小几何体出发。','薄柱面跨越介质界面，上下法线相反；扁矩形的上下长边绕行方向相反。',600),
('是与所定电流方向满足右手关系的环向单位矢量。','comparison-line-sources','图比-5　同样是长直源，场的方向不同，所选积分对象也不同。','正长直线电荷的电场沿径向向外；向纸外的长直电流产生逆时针环绕磁场。',420),
('对照教材 §11.5 与 §14.4，看清一个跟踪电压，一个跟踪电流。','comparison-transients','图比-6　用各自的时间常量归一化，RC 电压与 RL 电流具有相同的指数变化形式。','建立曲线从0升到1，t等于时间常量时达到0.632；衰减曲线从1趋近0。',450)]}
for fn,items in entries.items():
    p=posts/fn;s=p.read_text(encoding='utf-8')
    for anchor,name,cap,alt,height in items:
        if f'/images/physics/{name}.svg' in s:continue
        assert s.count(anchor)==1,(fn,anchor,s.count(anchor))
        s=s.replace(anchor,anchor+'\n'+figure(name,cap,alt,height),1)
    p.write_text(s,encoding='utf-8')
print('Generated 8 diagrams and inserted 9 figures into the guide and comparison.')
