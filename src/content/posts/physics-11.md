---
title: "第11章｜稳恒电流：把电荷流动、局部电场和电路连起来"
description: "从电流密度与电荷守恒出发，理解欧姆定律、焦耳热、电动势、基尔霍夫定律和 RC 充放电，配教材典型习题与思考题解答。"
pubDate: 2026-11-12
tags: [大学物理, 电磁学, 学习笔记]
series:
  name: 大学物理电磁学笔记
  order: 4
---

本章对应教材第 94～115 页，PDF 第 104～125 页。主线是：**电场推动电荷形成电流，电源持续补充能量，电荷守恒和电势关系约束整个电路。**

## 1. §11.1 电流与电流密度：看整体，也看局部

### 电流不是“导线里有多少电荷”

电流是电荷的定向运动。电子、离子、半导体中的空穴都可以成为载流子。金属中的电子有杂乱的热运动；没有电场时，各方向的运动平均抵消，不形成宏观电流。加上电场后，电子在热运动之外产生微小的平均定向速度，叫**漂移速度**。

选定一个截面的正法线方向，电流定义为单位时间通过截面的净电荷量：

$$
I=\frac{\mathrm dq}{\mathrm dt},\qquad [I]=\mathrm A=\mathrm{C/s}.
$$

$I$ 是有正负的标量。正电荷沿正法线通过，或负电荷沿反方向通过，都记为正电流。不能因为电流有习惯方向，就把 $I$ 当作空间矢量。

电流密度 $\mathbf j$ 描述某一点的电流方向和疏密，单位是 $\mathrm{A/m^2}$。它沿正电荷定向运动的方向；电子的漂移方向与它相反。

$$
\boxed{I=\int_S\mathbf j\cdot\mathrm d\mathbf S},\qquad
\mathrm d\mathbf S=\mathbf n\,\mathrm dS.
$$

这是**点乘**：只有垂直穿过截面的那一部分电流有贡献。若 $\mathbf j$ 均匀且垂直截面，才可简化成 $I=jS$；若与法线夹角为 $\theta$，则 $I=jS\cos\theta$。








<figure class="physics-figure">
  <a href="/images/physics/ch11-current-density.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-current-density.svg" alt="上图电场与电流密度向右，电子漂移向左。下图电流密度与截面法线夹角θ，法向分量为j cosθ。" width="640" height="660" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-1｜电子向左漂移，正电流向右；斜向电流穿过截面时只取法向分量。</figcaption>
</figure>

### 漂移速度怎样进入公式

设每立方米有 $n$ 个同类载流子，每个带电量 $q$，平均漂移速度为 $\mathbf v_d$。在 $\mathrm dt$ 内能通过截面的载流子来自长度为 $v_d\mathrm dt$ 的小柱体，因此

$$
\boxed{\mathbf j=nq\mathbf v_d}.
$$

对电子，$q=-e$，所以 $\mathbf j=-ne\mathbf v_d$；只算大小时用 $j=nev_d$。有多种载流子时，把各类的 $n_s q_s\mathbf v_s$ 相加。

**灯很快亮，不表示电子从开关一路飞奔到灯泡。** 教材第 97 页强调：建立电场的信息传播很快，导线各处已有的电子随即开始漂移；漂移速度本身很小。

### 思考题 11.1｜有电流就一定带净电荷吗？

**出处：教材第 112 页；题意简述。** 在 $\mathbf j\ne0$ 的地方，电荷体密度是否必不为零？

**解答：不一定。** 通流金属中，正离子和电子的电荷可在宏观上抵消，使净电荷密度近似为零；正离子基本固定，电子却在漂移，因此电流密度不为零。电荷密度统计“正负电荷剩多少”，电流密度还要看“它们各往哪里运动”。

### 稳恒电流来自电荷守恒

取一个固定的闭合曲面，外法线为正。流出的净电荷越多，内部积存的电荷越少：

$$
\boxed{\oiint_S\mathbf j\cdot\mathrm d\mathbf S
=-\frac{\mathrm dQ_{\text{内}}}{\mathrm dt}}.
$$

负号表达“流出使内部减少”。稳恒时，各点的 $\mathbf j$ 不随时间变化，电荷分布也不再随时间变化，故

$$
\boxed{\oiint_S\mathbf j\cdot\mathrm d\mathbf S=0}.
$$

它表示流入等于流出，并不表示没有电荷流动。串联导体各截面的电流相同，就来自这个条件。

### 稳恒电场与静电场怎样区分

稳恒电场的空间分布不随时间变化，同样满足静电场的环路关系，电势差仍可由电场的线积分求出。但要区分两种导体状态：

| 状态 | 导体内部 | 表面电场 |
|---|---|---|
| 静电平衡 | $\mathbf E=0$，没有宏观电流，是等势体 | 若非零，垂直导体表面 |
| 有电阻的导体通稳恒电流 | 通常 $\mathbf E\ne0$，沿导线存在电势降 | 可有沿表面的分量，推动电流 |

“稳恒”说的是分布不随时间变化；“静电平衡”还要求导体内的电荷不发生宏观定向流动。

### 习题 11.4｜粗铝线接细铜线，哪里流得更密？

**出处：教材第 114 页；题意简述。** 直径 $2.5\,\mathrm{mm}$ 的铝线与直径 $1.8\,\mathrm{mm}$ 的铜线串接，通 $1.3\,\mathrm A$ 稳恒电流。求两者电流密度及铜中电子的漂移速率。铜的质量密度为 $8.96\times10^3\,\mathrm{kg/m^3}$，每个铜原子贡献一个自由电子。






<figure class="physics-figure">
  <a href="/images/physics/ch11-series-wire.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-series-wire.svg" alt="粗铝线与细铜线串接，电流均为1.3A；铝线直径2.5mm，铜线直径1.8mm。" width="640" height="470" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-2｜串联导线中的总电流相同，细铜线的电流密度较大。</figcaption>
</figure>



**解答。** 串联时两段的 $I$ 相同，而 $j=I/S=4I/(\pi d^2)$：

$$
j_{\mathrm{Al}}=2.65\times10^5\,\mathrm{A/m^2},\qquad
j_{\mathrm{Cu}}=5.11\times10^5\,\mathrm{A/m^2}.
$$

取铜的摩尔质量 $M=63.5\times10^{-3}\,\mathrm{kg/mol}$、阿伏伽德罗常数 $N_A=6.02\times10^{23}\,\mathrm{mol^{-1}}$，电子数密度为

$$
n=\frac{\rho_{\text{质量}}N_A}{M}
\approx8.49\times10^{28}\,\mathrm{m^{-3}}.
$$

于是

$$
v_d=\frac{j_{\mathrm{Cu}}}{ne}\approx3.76\times10^{-5}\,\mathrm{m/s}.
$$

电子向电流的反方向漂移。这题把“电流相同”和“电流密度相同”分开了。

## 2. §11.2 欧姆定律：从一段导线到一个点

### 电阻、电阻率和电导率

对温度等条件固定的欧姆导体，

$$
U=IR,\qquad R=\rho\frac{l}{S},\qquad \gamma=\frac1\rho.
$$

$U$ 为沿电流方向的电势降，$\rho$ 是电阻率，$\gamma$ 是电导率。教材正文用 $\gamma$，部分习题用 $\sigma$ 表示电导率，这里统一用 $\gamma$。它们的单位分别为 $\Omega\!\cdot\!\mathrm m$ 与 $\mathrm{S/m}$。

$R=\rho l/S$ 对应均匀材料、等截面、沿长度方向通电的情形。不同几何形状应取小段：

$$
\mathrm dR=\rho\frac{\mathrm dl}{S(l)},
$$

再按串联或并联关系组合，不能任取一个面积代入整段公式。

### 微分形式的简短推导

取一小段顺着电流的细柱，长 $\mathrm dl$、面积 $\mathrm dS$。其中 $\mathrm dU=E\mathrm dl$、$\mathrm dI=j\mathrm dS$、$\mathrm dR=\rho\mathrm dl/\mathrm dS$。由 $\mathrm dU=\mathrm dI\,\mathrm dR$ 得 $E=\rho j$，因而

$$
\boxed{\mathbf j=\gamma\mathbf E}.
$$

这是一条局部关系：已知某点电场，就知道该点电流密度。对各向同性欧姆材料，$\mathbf j$ 与 $\mathbf E$ 同向；$\gamma$ 为标量。

这里的 $\mathbf E$ 是推动普通电阻中电荷运动的电场。电源内部还有非静电作用，要按下一节的电源模型处理。

### 思考题 11.2｜同种材料的粗细两段

**出处：教材第 112 页；题意简述。** 两根截面不同的铜棒串联，电流、电流密度、电场是否相同？若等长，两段电压是否相同？

**解答。** $I$ 相同；$j=I/S$，细棒的 $j$ 大；同种材料同温度时 $E=j/\gamma$，细棒内的 $E$ 大；等长时 $U=El$，细棒的电势降也大。不能把“导体等势”用于正在通电的电阻。

### 电阻率还受什么影响

教材用近似式 $\rho_t=\rho_0(1+\alpha t)$ 描述一定温度范围内金属电阻率的变化，$\rho_0$ 为 $0^\circ\mathrm C$ 时的值。常见金属的 $\alpha>0$，升温通常使电阻增大。

有些材料低于转变温度会进入超导态，直流电阻消失；已建立的闭合超导电流可长期维持。**“电流存在就必须处处有非零电场”是普通有电阻导体的结论，不能直接套到超导态。**

## 3. 焦耳热：电能在哪里变成热

电荷在电场作用下获得能量，经碰撞把能量传给材料。普通电阻的热功率为

$$
P=UI=I^2R=\frac{U^2}{R},\qquad Q=I^2Rt
$$

（最后一式要求 $I,R$ 不变）。若它们随时间变化，应积分：$Q=\int I^2R\,\mathrm dt$。

取一小块导体，其单位体积的发热功率为

$$
\boxed{p_{\text{热}}=\mathbf j\cdot\mathbf E
=\gamma E^2=\rho j^2},\qquad[p_{\text{热}}]=\mathrm{W/m^3}.
$$

教材将这个热功率密度记为 $w$；这里写作 $p_{\text{热}}$，与第 10、14 章单位为 $\mathrm{J/m^3}$ 的场能密度分开。前者是“每秒发多少热”，后者是“此刻存了多少能量”。

### 习题 11.5｜一次算通 $E$、$j$ 和发热

**出处：教材第 114 页；题意简述。** 铜棒长 $2\,\mathrm m$、截面积 $1600\,\mathrm{mm^2}$，两端电压 $50\,\mathrm{mV}$，电导率 $5.7\times10^7\,\mathrm{S/m}$。求电流密度、电场强度和热功率密度。

**解答。** 先把电压换成 $0.050\,\mathrm V$：

$$
E=\frac Ul=0.025\,\mathrm{V/m},
$$

$$
j=\gamma E=1.425\times10^6\,\mathrm{A/m^2},
$$

$$
p_{\text{热}}=\gamma E^2=3.56\times10^4\,\mathrm{W/m^3}.
$$

截面积没有进入这三个局部量的计算。若要算总电流或总功率，才用 $I=jS$、$P=p_{\text{热}}Sl$。这能帮助区分“局部强弱”和“整体多少”。

### 习题 11.6｜球壳间电阻为什么不能套 $\rho l/S$

**出处：教材第 114 页；题意简述。** 半径 $R_1<R_2$ 的同心导体球壳之间充满电阻率为 $\rho$ 的均匀材料。求壳间电阻；内壳比外壳电势高 $U$ 时，求 $\mathbf j(r)$。






<figure class="physics-figure">
  <a href="/images/physics/ch11-spherical-resistor.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-spherical-resistor.svg" alt="同心内外球壳半径R1和R2，半径r的薄球层厚度dr，电流沿径向向外。" width="640" height="540" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-3｜电流穿过同心球面；半径越大，可通过的面积 4πr² 越大。</figcaption>
</figure>



**解答。** 电流沿半径流动，半径 $r$ 处可通过的面积为 $4\pi r^2$。薄球层彼此串联，故

$$
\mathcal R=\int_{R_1}^{R_2}\frac{\rho\,\mathrm dr}{4\pi r^2}
=\boxed{\frac{\rho}{4\pi}\left(\frac1{R_1}-\frac1{R_2}\right)}.
$$

各球面的总电流相同，$I=U/\mathcal R$，所以

$$
\boxed{\mathbf j(r)=
\frac{U}{\rho r^2(1/R_1-1/R_2)}\,\mathbf e_r},
\qquad R_1<r<R_2.
$$

$\mathbf e_r$ 指向外；若 $U$ 为负，电流方向自动反转。几何面积随 $r$ 增大，因此 $j$ 按 $1/r^2$ 减小。

## 4. §11.3 电动势：每库仑电荷得到多少能量

外电路中，正电荷由高电势处流向低电势处，电势能减少。要使它持续循环，电源必须把电荷从低电势处送回高电势处。这一步靠化学、机械等**非静电作用**。

将非静电力除以电荷量，定义等效的非静电场强 $\mathbf E_k=\mathbf F_k/q$。电动势为

$$
\boxed{\mathcal E=\frac{A_k}{q}
=\oint\mathbf E_k\cdot\mathrm d\mathbf l}.
$$

电动势的单位是伏特，含义是“每库仑电荷获得的非静电能量”，它不是力，也不是矢量。电池符号旁的方向约定指从负极到正极的升势方向。

静电力绕闭合回路的总功为零；非静电作用可以持续把其他形式的能量转化为电能。这正是电源能维持电流的原因。








<figure class="physics-figure">
  <a href="/images/physics/ch11-source-voltage.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-source-voltage.svg" alt="电源正极在上、负极在下，外接电阻R；非静电场向上，静电场向下，外电路电流从正极流出。" width="640" height="560" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-4｜供电时电源内部的非静电作用向上输送正电荷，静电场反向；外电路从正极流向负极。</figcaption>
</figure>

### 电动势不等于任何时候的端电压

对电动势为 $\mathcal E$、内阻为 $r$ 的电源，若 $I$ 从电源正极向外流出，

$$
\boxed{U_+-U_-=\mathcal E-Ir}.
$$

开路时 $I=0$，端电压等于电动势；对外供电时，内部有 $Ir$ 的电势降；若电流流入正极给电池充电，则在上述电流约定下 $I<0$，端电压大于电动势。

### 思考题 11.9｜最大输出功率是否等于最高效率？

**出处：教材第 113 页；题意简述。** 电源 $\mathcal E,r$ 接可变外电阻 $R$。求电流、端电压、输出功率及效率，并比较开路、短路和最大功率状态。

**解答。**

$$
I=\frac{\mathcal E}{R+r},\qquad
U=\frac{\mathcal E R}{R+r},\qquad
P_R=\frac{\mathcal E^2R}{(R+r)^2}.
$$

开路极限 $R\to\infty$：$I\to0$、$U\to\mathcal E$、输出功率趋零。短路 $R=0$：$U=0$、$I=\mathcal E/r$，输出到外电阻的功率为零，能量消耗在内阻中。

由

$$
\frac{\mathrm dP_R}{\mathrm dR}
=\frac{\mathcal E^2(r-R)}{(R+r)^3}
$$

知 $R=r$ 时输出功率最大，$P_{\max}=\mathcal E^2/(4r)$。效率为

$$
\eta=\frac{P_R}{\mathcal EI}=\frac R{R+r},
$$

此时只有 $50\%$。增大 $R$ 可以提高效率，但不会一直提高输出功率。

## 5. §11.4 基尔霍夫定律：两个守恒关系解复杂电路

### 节点定律

$$
\boxed{\sum I_{\text{流入}}=\sum I_{\text{流出}}}.
$$

它来自稳恒条件下电荷不在节点积累。先给每条支路假设方向，求出负值就表示实际方向相反，无须预先猜对所有电流。

### 回路定律与符号规则

沿任意选定的闭合绕行方向，电势变化总和为零：

$$
\boxed{\sum\Delta U=0}.
$$

| 沿所选绕行方向经过的元件 | 电势变化 |
|---|---|
| 电阻，顺着假设电流 | $-IR$ |
| 电阻，逆着假设电流 | $+IR$ |
| 理想电源，由负极到正极 | $+\mathcal E$ |
| 理想电源，由正极到负极 | $-\mathcal E$ |

内阻也按电阻处理。路径方向和电流方向是两套约定，不能混在一起。对 $n$ 个节点，只需要 $n-1$ 个独立节点方程；回路方程也要选独立的，重复绕同一套回路不会增加新信息。

本章讨论的回路中没有随时间变化的穿链磁通；第 14 章出现感应电动势时，要把它作为电动势计入方程。

### 习题 11.10｜用节点电压整理三个支路

**出处：教材第 114～115 页；题意简述。** 原图的三个支路连接同一上节点 $a$ 和下节点 $b$。各电源均为正极朝上：左支路含两个 $R_1$ 及 $\mathcal E_1$；中支路含 $R_2$ 及 $\mathcal E_2$；右支路含两个 $R_1$ 及 $\mathcal E_3$。已知 $R_1=1\,\Omega$、$R_2=2\,\Omega$、$\mathcal E_1=2\,\mathrm V$、$\mathcal E_2=\mathcal E_3=4\,\mathrm V$，内阻忽略。原图 $I_1$ 向下，$I_2,I_3$ 向上。






<figure class="physics-figure">
  <a href="/images/physics/ch11-three-branches.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-three-branches.svg" alt="三条并联支路，上节点a下节点b。左支路两个R1和电源ε1，电流向下；中支路R2和ε2、右支路两个R1和ε3，电流向上。" width="640" height="640" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-5｜按原题连接关系重绘。三电源正极均朝上，箭头与正文假设的电流方向一致。</figcaption>
</figure>



**解答。** 令 $V=U_a-U_b$，按每条支路的电势变化得到

$$
I_1=\frac{V-\mathcal E_1}{2R_1},\qquad
I_2=\frac{\mathcal E_2-V}{R_2},\qquad
I_3=\frac{\mathcal E_3-V}{2R_1}.
$$

节点 $a$ 有 $I_1=I_2+I_3$，代入数值得

$$
\frac{V-2}{2}=\frac{4-V}{2}+\frac{4-V}{2}.
$$

所以

$$
\boxed{U_a-U_b=\frac{10}{3}\,\mathrm V},\qquad
\boxed{I_1=\frac23\,\mathrm A,\quad I_2=I_3=\frac13\,\mathrm A}.
$$

结果均为正，实际方向与原图相同。先设一个节点电压，能把多回路的符号问题变成三条清晰的支路关系。

## 6. §11.5 RC 充放电：电流为什么逐渐变小

$R$ 与电容 $C$ 串联，忽略电源内阻，或将内阻计入总电阻 $R$。记 $q$ 为约定正极板上的电荷，电容电压 $U_C=q/C$。**电容电压不能瞬间突变**；否则有限电容会要求无限大的瞬时电流。








<figure class="physics-figure">
  <a href="/images/physics/ch11-rc-circuits.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-rc-circuits.svg" alt="上图电源、电阻、电容串联充电，电流从电源正极流向电容上极板。下图电源移去，电容通过电阻放电，电流从上极板流出。" width="640" height="760" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-6｜充电时电流流入正极板；放电时电流从原正极板流出。两图是切换完成后的不同电路。</figcaption>
</figure>

### 从未充电开始充电

接上恒定电动势 $\mathcal E$，取电流流入正极板为正，则

$$
I=\frac{\mathrm dq}{\mathrm dt},\qquad
\mathcal E-IR-\frac qC=0.
$$

整理成 $\mathrm dq/(C\mathcal E-q)=\mathrm dt/(RC)$，从 $q(0)=0$ 积分，得到

$$
\boxed{q(t)=C\mathcal E\left(1-e^{-t/(RC)}\right)},
$$

$$
\boxed{U_C(t)=\mathcal E\left(1-e^{-t/(RC)}\right)},\qquad
\boxed{I(t)=\frac{\mathcal E}{R}e^{-t/(RC)}}.
$$

刚接通时 $q=0$，电容电压为零，电流最大；充入电荷越多，电容电压越大，留给电阻的电压越小，电流随之衰减。最终电容电压等于电源电动势，电流趋零。

### 从初电荷 $q_0$ 开始放电

撤去电源，将电容通过电阻闭合放电。若把流出原正极板的电流大小记为 $I_{\text{放}}$，应写

$$
I_{\text{放}}=-\frac{\mathrm dq}{\mathrm dt},\qquad
\frac qC-I_{\text{放}}R=0.
$$

所以

$$
\boxed{q(t)=q_0e^{-t/(RC)}},\qquad
\boxed{U_C(t)=\frac{q_0}{C}e^{-t/(RC)}},
$$

$$
\boxed{I_{\text{放}}(t)=\frac{q_0}{RC}e^{-t/(RC)}}.
$$

若仍使用“流入正极板”的有向电流 $I$，则放电时 $I=-I_{\text{放}}<0$。公式前的负号来自方向定义。








<figure class="physics-figure">
  <a href="/images/physics/ch11-rc-curves.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch11-rc-curves.svg" alt="归一化RC曲线，红线由0趋向1，蓝线由1趋向0；t等于τ时分别为0.632和0.368。" width="640" height="560" loading="lazy" decoding="async" /></a>
  <figcaption>图 11-7｜充电电压逐渐上升，电流逐渐衰减；放电电荷也沿蓝线衰减。</figcaption>
</figure>

### 时间常数与能量

$$
\boxed{\tau=RC}.
$$

$\tau$ 越大，变化越慢。经过一个 $\tau$，充电达到最终电压的约 $63.2\%$；放电剩约 $36.8\%$。经过 $5\tau$，差距降到约 $0.67\%$。理想指数过程到达最终值需要无限长时间。

恒定电源把未充电电容充到 $\mathcal E$，提供的能量为 $\mathcal E Q=C\mathcal E^2$；电容最后储能 $\tfrac12C\mathcal E^2$，另一半在电阻中变成热。电阻大小改变充电快慢，但在这个理想模型中不改变最终总发热量。

**做 RC 题先看三个时刻：** 初始电容电压是多少，最终电容电压是多少，中间用什么 $RC$ 决定变化速度。复杂一点的充放电也可写成

$$
U_C(t)=U_C(\infty)+[U_C(0)-U_C(\infty)]e^{-t/\tau},
$$

其中 $\tau=R_{\text{等效}}C$，$R_{\text{等效}}$ 是从电容两端看进去、将独立理想电压源短路后得到的等效电阻。

## 7. 本章检查清单

- 看截面总电流用 $I$；看某一点电流的大小和方向用 $\mathbf j$。
- 串联保持的是 $I$，面积变化时 $j$ 可以变化。
- $\mathbf j=\gamma\mathbf E$ 是局部材料关系；$I=U/R$ 是整段电路关系。
- 焦耳热密度的单位是 $\mathrm{W/m^3}$，场能密度的单位是 $\mathrm{J/m^3}$。
- 电动势描述电源转换能量的能力；端电压还受内阻和电流影响。
- 列回路方程先选绕行方向；解出负电流，只需反转实际方向。
- 充电时 $I=\mathrm dq/\mathrm dt$；以流出正极板为正的放电电流为 $-\mathrm dq/\mathrm dt$。

**教材依据：** 吴泽华、陈治中、黄正东《大学物理（中册）》，浙江大学出版社，第 3 版，第 11 章 §11.1～§11.5。题目按原书编号简述；页码均为书上印刷页码，PDF 页序加 10。
