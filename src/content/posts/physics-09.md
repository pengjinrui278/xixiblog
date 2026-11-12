---
title: "第9章：真空中的静电场——从电荷、场强到电势"
description: "从零理解电场强度、电通量、高斯定理、电势和电偶极子，配简明推导、选择题辨析及教材典型习题解答。"
pubDate: 2026-11-12
tags: [大学物理, 电磁学, 学习笔记]
series:
  name: 大学物理电磁学笔记
  order: 2
---

本章对应教材 §9.1—§9.8，印刷页 3—51（PDF 第 13—61 页）。学习主线是：**电荷产生电场；场强描述怎样受力；电势描述怎样做功。** 文中加粗字母表示矢量，普通字母表示大小或带符号的分量。习题保留教材编号，题意用简述形式呈现。

## 1. 电荷和库仑定律：先分清谁对谁施力

### 1.1 电荷的四条基本性质

对应 §9.1，书 p.3—5。

- **正、负两种电荷**：同号相斥，异号相吸。普通物体带电，通常是电子转移造成正负电荷不平衡。
- **电荷守恒**：孤立系统中，正负电荷的代数和不变。摩擦起电是转移电荷，不是凭空产生净电荷。
- **电荷量子化**：通常可独立观察到的带电体满足 $q=ne$，$n$ 为整数，$e\approx1.60\times10^{-19}\,\mathrm C$。宏观电荷量很大，计算时常将其视为连续分布。
- **电荷的运动不变性**：同一物体的总电荷量不因观察者选择不同惯性参考系而改变。

“点电荷”是一种近似：带电体的尺寸远小于所讨论距离时，可以忽略它的形状。小球不一定能当点电荷，关键是**相对距离**。

### 1.2 库仑力是矢量

对应 §9.2，书 p.5—8。在真空中，令 $\mathbf e_{12}$ 从电荷 $q_1$ 指向 $q_2$，则 $q_1$ 对 $q_2$ 的力为

$$
\boxed{\mathbf F_{2\leftarrow1}=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}^{2}}\mathbf e_{12}}
$$

其中 $\varepsilon_0\approx8.85\times10^{-12}\,\mathrm{F/m}$，$k_e=1/(4\pi\varepsilon_0)\approx9.0\times10^9\,\mathrm{N\,m^2/C^2}$。

电荷 $q_1,q_2$ 要带正负号：乘积为正，力沿 $\mathbf e_{12}$；乘积为负，力沿反方向。若只求力的**大小**，才写 $F=k_e\lvert q_1q_2\rvert/r^2$。

多个电荷同时作用时，先分别算力，再作**矢量相加**。其他电荷的加入会改变合力，但不会改变原先那一对固定点电荷之间的库仑力。

## 2. 电场强度：每单位正电荷受到多大的力

对应 §9.3，书 p.8—18。

$$
\boxed{\mathbf E=\frac{\mathbf F}{q_0}},\qquad \boxed{\mathbf F=q\mathbf E}
$$

试验电荷 $q_0$ 要足够小，避免明显改变原电荷分布。$\mathbf E$ 的方向是**正电荷**的受力方向；负电荷的受力方向与它相反。单位 $\mathrm{N/C}=\mathrm{V/m}$。

**教材思考题 9.3（p.45）：既然 $E=F/q_0$，场强是否与试验电荷成反比？**

不是。改变 $q_0$ 时，同一点的力 $\mathbf F=q_0\mathbf E$ 也同比改变。比值描述原有电场，不由试验电荷决定。定义式不能脱离其他量的变化，直接读成正比或反比关系。

### 2.1 点电荷、连续电荷分别怎样求场

若 $\mathbf e_r$ 从场源电荷指向观察点，

$$
\mathbf E=\frac{q}{4\pi\varepsilon_0r^2}\mathbf e_r,
\qquad
\mathbf E_{\text{总}}=\sum_i\mathbf E_i.
$$

连续带电体可以切成许多小电荷 $\mathrm dq$。每一小块都按点电荷处理，然后积分：

$$
\boxed{\mathbf E=\frac1{4\pi\varepsilon_0}\int\frac{\mathrm dq}{r^2}\mathbf e_r}
$$

| 电荷分布 | 电荷密度 | 微小电荷 |
|---|---|---|
| 细线 | 线密度 $\lambda$，单位 $\mathrm{C/m}$ | $\mathrm dq=\lambda\,\mathrm dl$ |
| 薄面 | 面密度 $\sigma$，单位 $\mathrm{C/m^2}$ | $\mathrm dq=\sigma\,\mathrm dS$ |
| 体积 | 体密度 $\rho$，单位 $\mathrm{C/m^3}$ | $\mathrm dq=\rho\,\mathrm dV$ |

积分可理解为“把每一小块的贡献加起来”。方向变化时，先分解：$E_x=\int\mathrm dE_x$，再合成，不能把大小直接相加。

### 2.2 圆环与圆盘：对称性先消掉一半工作

半径 $R$、总电荷 $Q$ 的均匀带电圆环，以圆心为原点、轴为 $z$ 轴：

$$
\boxed{\mathbf E(z)=\frac{Qz}{4\pi\varepsilon_0(R^2+z^2)^{3/2}}\mathbf e_z}
$$




<figure class="physics-figure">
  <a href="/images/physics/ch09-ring-disk.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-ring-disk.svg" alt="圆环上两个对称正电荷元到轴上P点，横向场分量抵消，合场向右；下图为圆盘分环。" width="640" height="730" loading="lazy" decoding="async" /></a>
  <figcaption>图9-1　圆环轴线上的对称叠加，以及把圆盘分成同心圆环的方法。图示 Q&gt;0、z&gt;0。</figcaption>
</figure>

**短推导**：每个电荷元到轴上点的距离都是 $r=\sqrt{R^2+z^2}$。对称位置的横向分量相消，轴向分量相加：

$$
\mathrm dE_z=\frac{\mathrm dq}{4\pi\varepsilon_0r^2}\frac zr,
\qquad E_z=\frac{z}{4\pi\varepsilon_0r^3}\int\mathrm dq.
$$

因此圆心场强为零；远处 $\lvert z\rvert\gg R$ 时，圆环近似点电荷。注意分子中的 $z$ 保留了方向符号。

半径 $R$、面密度 $\sigma$ 的均匀圆盘，在 $z>0$ 一侧的轴线上：

$$
\boxed{\mathbf E(z)=\frac\sigma{2\varepsilon_0}\left(1-\frac z{\sqrt{z^2+R^2}}\right)\mathbf e_z}
$$

把圆盘切成同心圆环，取 $\mathrm dq=\sigma\,2\pi r\,\mathrm dr$，代入圆环公式积分即可。距盘很近且远离边缘时，近似无限平面；距盘很远时，近似总电荷为 $\sigma\pi R^2$ 的点电荷。

### 2.3 教材习题 9.5：有限直线电荷的两种观察位置

题意简述（p.47）：均匀带电细直线长 $L=15\,\mathrm{cm}$，$\lambda=5\times10^{-9}\,\mathrm{C/m}$。求延长线上距近端 $R=5\,\mathrm{cm}$ 的点，以及中垂线上距中点 $a=5\,\mathrm{cm}$ 的点的场强。




<figure class="physics-figure">
  <a href="/images/physics/ch09-ex09-05.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-ex09-05.svg" alt="正电细线延长线上P点场向右；中垂线上Q点对称分量抵消，合场向上。" width="640" height="620" loading="lazy" decoding="async" /></a>
  <figcaption>图9-2　习题9.5的两种几何位置。上图从近端量 R，下图从中点量 a。</figcaption>
</figure>

**延长线上的点**：所有电荷元的场同向。以观察点到电荷元的距离 $r$ 积分，

$$
E_P=k_e\lambda\int_R^{R+L}\frac{\mathrm dr}{r^2}
=k_e\lambda\left(\frac1R-\frac1{R+L}\right)
\approx6.75\times10^2\,\mathrm{N/C}.
$$

方向沿直线远离带电线段。

**中垂线上的点**：平行线段的分量相消，只剩垂直线段的分量。用 $x$ 表示电荷元到中点的有向距离，

$$
E_Q=k_e\lambda\int_{-L/2}^{L/2}\frac{a\,\mathrm dx}{(a^2+x^2)^{3/2}}
=\frac{k_e\lambda L}{a\sqrt{a^2+(L/2)^2}}
\approx1.50\times10^3\,\mathrm{N/C}.
$$

方向从线段中点指向观察点。相同的垂直距离，不同的电荷几何分布，场强不会一样。

## 3. 电场线、电通量：方向图和“穿过量”

对应 §9.4，书 p.18—21。

电场线在每点的切线方向给出 $\mathbf E$ 的方向，线密处场强大。静电场线由正电荷出发、终止于负电荷，也可以延伸至无穷远；不在无电荷处突然中断，不相交，不闭合。

电场线是表示场的辅助图，不是空间里的实体，也不一定是粒子轨迹。粒子的速度方向受先前运动影响，只有加速度方向由合力决定。

为曲面选定单位法向量 $\mathbf n$，定义面积矢量 $\mathrm d\mathbf S=\mathbf n\,\mathrm dS$。电通量为

$$
\boxed{\Phi_E=\int_S\mathbf E\cdot\mathrm d\mathbf S
=\int_SE\cos\theta\,\mathrm dS}
$$

这是**点乘**，结果是带正负号的标量。$\theta$ 是场与**法线**的夹角，不是与平面的夹角。只有均匀电场穿过平面时，才能直接用 $\Phi_E=ES\cos\theta$。




<figure class="physics-figure">
  <a href="/images/physics/ch09-flux.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-flux.svg" alt="上图电场与面积外法线夹角theta；下图均匀电场穿入和穿出无电荷球面。" width="640" height="650" loading="lazy" decoding="async" /></a>
  <figcaption>图9-3　开放面先选法线；闭合面统一取外法线。下图均匀场穿过一个球面，进出通量相抵。</figcaption>
</figure>

闭合曲面的法线统一向外：穿出贡献为正，穿入为负。通量为零表示进出抵消，不能推出场强处处为零。

## 4. 高斯定理：先看包围多少电荷，再看能否求场

对应 §9.5，书 p.21—30。

$$
\boxed{\oiint_S\mathbf E\cdot\mathrm d\mathbf S=\frac{Q_{\text{内}}}{\varepsilon_0}}
$$

$Q_{\text{内}}$ 是闭合曲面内部所有电荷的**代数和**。左边的 $\mathbf E$ 却是内外全部电荷共同产生的总场。

**短推导的核心**：点电荷位于球心时，$E=k_eq/r^2$，乘球面积 $4\pi r^2$ 得 $q/\varepsilon_0$。换成任意包围该电荷的闭合面，穿出的总通量仍相同；面外电荷的场线有进有出，净贡献为零；再利用叠加原理得到一般形式。

定理对任意闭合面成立，但仅凭一个总通量，不能确定面上每点的场强。要把 $E$ 提出积分，需要球对称、轴对称、平面对称等条件。

**教材思考题 9.8（p.45）：球面包住一对等量异号电荷，净通量为零，能否推出 $E=0$？**

不能。偶极子电场在球面各处的大小和方向不同，$E\cos\theta$ 不是常数，不能写成 $E\cos\theta\,4\pi R^2$。错在提取非常数，不在高斯定理。

### 4.1 三种高频对称模型

以下 $\mathbf e_r$ 向外，$\sigma,\lambda,Q$ 均保留符号；球面边界用两侧极限理解。

| 电荷分布 | 高斯面 | 场强 |
|---|---|---|
| 半径 $R$ 的均匀带电球壳 | 同心球面 | 内部 $\mathbf E=0$；外部 $\mathbf E=Q\mathbf e_r/(4\pi\varepsilon_0r^2)$ |
| 半径 $R$ 的均匀带电实心球 | 同心球面 | 内部 $\mathbf E=Qr\mathbf e_r/(4\pi\varepsilon_0R^3)$；外部同点电荷 |
| 无限长均匀直线电荷 | 同轴圆柱面 | $\mathbf E=\lambda\mathbf e_r/(2\pi\varepsilon_0r)$ |
| 无限长、半径 $R$ 的均匀圆柱面电荷 | 同轴圆柱面 | 内部为零；外部同总线密度 $\lambda$ 的直线电荷 |
| 无限大均匀带电平面 | 穿过平面的薄柱面 | 两侧 $\mathbf E=\sigma\mathbf n_{\text{各侧}}/(2\varepsilon_0)$ |

例如无限直线：侧面场处处等大且垂直侧面，两底面通量为零，所以 $E\,2\pi rl=\lambda l/\varepsilon_0$。无限平面：两个底面都贡献通量，所以 $2ES=\sigma S/\varepsilon_0$。

两张带 $+\sigma$、$-\sigma$ 的无限平行平面叠加后，板间 $E=\sigma/\varepsilon_0$，由正板指向负板；板外为零。这里的“无限”在实际题中通常表示观察位置远离边缘。

### 4.2 教材习题 9.14：电荷密度不均匀，也能用高斯定理

题意简述（p.48）：半径 $R$ 的非金属球，电荷体密度 $\rho(r)=kr^2$，求球内、球外场强。这里 $k$ 是原题给定的密度系数，与库仑常量 $k_e$ 不同。




<figure class="physics-figure">
  <a href="/images/physics/ch09-ex09-14.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-ex09-14.svg" alt="非均匀带电球内部取球形高斯面，薄球壳为积分元；下方场强随r先三次增长再平方反比下降。" width="640" height="690" loading="lazy" decoding="async" /></a>
  <figcaption>图9-4　习题9.14的薄球壳分割及按正文公式绘制的场强曲线。r=R 处两段连续。</figcaption>
</figure>

电荷仍然球对称，所以取半径 $r$ 的同心球面。半径为 $s$、厚度 $\mathrm ds$ 的薄球壳，体积是 $4\pi s^2\mathrm ds$。

$$
Q_{\text{内}}(r)=\int_0^rks^2\,4\pi s^2\mathrm ds=\frac{4\pi kr^5}{5}.
$$

球内：$E_r4\pi r^2=Q_{\text{内}}/\varepsilon_0$；球外：包住全部电荷 $4\pi kR^5/5$。于是

$$
\boxed{\mathbf E(r)=
\begin{cases}
\dfrac{kr^3}{5\varepsilon_0}\mathbf e_r,&0<r<R,\\[4pt]
\dfrac{kR^5}{5\varepsilon_0r^2}\mathbf e_r,&r>R.
\end{cases}}
$$

球心场为零，表面两侧结果相同。**非均匀不等于不对称**：密度只随距球心的距离变化，仍可使用球对称高斯面。

## 5. 环路定理、电势与功：弄清负号的来处

对应 §9.6—§9.7，书 p.30—41。

静电力做功只与起点、终点有关，与绕行路径无关，称为保守力。因此绕闭合路一圈：

$$
\boxed{\oint_L\mathbf E\cdot\mathrm d\mathbf l=0}.
$$

高斯定理说静电场有电荷作为源，环路定理说静电场无旋、可以用电势描述。环路积分不是曲面积分，$\mathrm d\mathbf l$ 指沿路的位移元。

### 5.1 电势、电势能、电势差是三个量

电势 $U$ 描述场所在位置，电势能 $W_p=qU$ 描述电荷与场的相互作用。零电势位置可以选择，但各点必须使用同一个参考。

$$
\boxed{U_A-U_B=\int_A^B\mathbf E\cdot\mathrm d\mathbf l}
$$

$$
\boxed{A_{A\to B}=q(U_A-U_B)=-\Delta W_p},
\qquad \Delta W_p=q(U_B-U_A).
$$

沿电场移动，电势降低。正电荷电势能降低，负电荷电势能升高。若仅电场力做功，动能增加量就是电场力所做的功。

若取参考点 $P_0$ 电势为零，则 $U(P)=\int_P^{P_0}\mathbf E\cdot\mathrm d\mathbf l$。有限范围内的电荷分布常取无穷远为零；无限直线、无限平面电荷不能机械地这样选，因为积分可能发散。

### 5.2 电势用代数和，场强用矢量和

取无穷远为零时：

$$
\boxed{U=\sum_i\frac{q_i}{4\pi\varepsilon_0r_i}},\qquad
\boxed{U=\frac1{4\pi\varepsilon_0}\int\frac{\mathrm dq}{r}}.
$$

正电荷给正电势，负电荷给负电势。各项保留符号相加，不分解方向。

| 模型 | 电势（无穷远为零） |
|---|---|
| 半径 $R$、电荷 $Q$ 的圆环轴线上 | $U(z)=Q/[4\pi\varepsilon_0\sqrt{R^2+z^2}]$ |
| 均匀球壳内部 $r\le R$ | $U=Q/(4\pi\varepsilon_0R)$ |
| 均匀球壳外部 $r\ge R$ | $U=Q/(4\pi\varepsilon_0r)$ |

无限长直线电荷若以距轴 $r_0$ 处为零，则

$$
U(r)=\frac\lambda{2\pi\varepsilon_0}\ln\frac{r_0}{r}.
$$

### 5.3 教材习题 9.24：场强为零，电势仍可很大

题意简述（p.50）：正方形四个顶点各有 $q=2.0\times10^{-9}\,\mathrm C$，每个顶点距中心 $r=5.0\,\mathrm{cm}$。求中心电势，以及把 $q_0=1.0\times10^{-9}\,\mathrm C$ 从无穷远移到中心时电场力的功和电势能变化。




<figure class="physics-figure">
  <a href="/images/physics/ch09-ex09-24.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-ex09-24.svg" alt="正方形四角各有正电荷，中心四个对角线方向电场相抵，中心电势为正。" width="640" height="470" loading="lazy" decoding="async" /></a>
  <figcaption>图9-5　习题9.24。中心处四个电场矢量两两抵消，四个正电势贡献仍然相加。</figcaption>
</figure>

由对称性，中心的场强相互抵消为零；电势是标量，四项相加：

$$
U_O=4k_e\frac qr\approx1.44\times10^3\,\mathrm V.
$$

$$
A_{\infty\to O}=q_0(0-U_O)\approx-1.44\times10^{-6}\,\mathrm J,
\qquad \Delta W_p\approx+1.44\times10^{-6}\,\mathrm J.
$$

“终点处不受力”不代表一路上电场没有做功。

### 5.4 教材习题 9.28：球壳内部的电势不是零

题意简述（p.50）：两个同心均匀球壳半径为 $0.10\,\mathrm m$、$0.30\,\mathrm m$，分别带正电荷 $Q_1=10^{-8}\,\mathrm C$、$Q_2=1.5\times10^{-8}\,\mathrm C$。求 $r_a=0.20\,\mathrm m$、$r_b=0.50\,\mathrm m$ 处电势。




<figure class="physics-figure">
  <a href="/images/physics/ch09-ex09-28.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-ex09-28.svg" alt="内壳半径0.1米、外壳半径0.3米，a距中心0.2米，b距中心0.5米。" width="640" height="490" loading="lazy" decoding="async" /></a>
  <figcaption>图9-6　习题9.28的球壳截面，半径按同一比例绘制。a 在两壳之间，b 在两壳外。</figcaption>
</figure>

$a$ 在小球壳外、大球壳内；大球壳贡献的是常量 $k_eQ_2/0.30$：

$$
U_a=k_e\left(\frac{Q_1}{0.20}+\frac{Q_2}{0.30}\right)\approx900\,\mathrm V.
$$

$b$ 在两个球壳外：

$$
U_b=k_e\frac{Q_1+Q_2}{0.50}\approx450\,\mathrm V.
$$

每一个球壳都要先判断观察点在它内部还是外部，再分别计算。

## 6. 电场与电势的关系：场强看“坡度”

对应 §9.8，书 p.41—45。若把电势想成高度，场强指向下降最快的方向，大小对应下降的陡峭程度。

$$
\boxed{\mathrm dU=-\mathbf E\cdot\mathrm d\mathbf l},\qquad
\boxed{\mathbf E=-\nabla U}
$$

不熟悉 $\nabla$ 时，先记分量式：

$$
E_x=-\frac{\partial U}{\partial x},\quad
E_y=-\frac{\partial U}{\partial y},\quad
E_z=-\frac{\partial U}{\partial z}.
$$

偏导数就是“只改变这个坐标，其他坐标先不动，看电势如何变化”。若只沿一条轴变化，就用普通导数 $E_x=-\mathrm dU/\mathrm dx$。

**短推导**：位移很短时，电场做功 $\mathrm dA=q\mathbf E\cdot\mathrm d\mathbf l$；又因 $\mathrm dA=-q\,\mathrm dU$，两式相等并约去 $q$。




<figure class="physics-figure">
  <a href="/images/physics/ch09-potential.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-potential.svg" alt="四个等间距的竖直等势面截线依次30、20、10、0伏，电场水平向右并与等势面垂直。" width="640" height="370" loading="lazy" decoding="async" /></a>
  <figcaption>图9-7　均匀电场的等势面。等距离对应相同电势差，电场由高电势指向低电势。</figcaption>
</figure>

等势面上 $\mathrm dU=0$，所以非零电场垂直等势面。比较相邻等势面的疏密时，要使它们的电势差相同：间距越小，场强越大。

**教材思考题 9.13（p.46）的四个判断：**

1. 场强大，电势一定高？**不一定**。陡坡可以位于低处，平地可以位于高处。
2. 某点场强为零，电势一定为零？**不一定**。带电球壳内部就是反例。
3. 某点电势为零，场强一定为零？**不一定**。等量异号电荷的中点电势为零，场强同向叠加。
4. 一整个空间区域电势相等，场强处处相等？**是，而且都为零**，因为所有方向的电势变化率均为零。只说某一个等势面，则仅能推出切向场为零。

## 7. 电偶极子：为下一章极化做准备

教材例 9.2、9.6、9.10、9.12 分别讨论其场、电势、受力与力矩。两个相距很近的等量异号电荷组成电偶极子，定义

$$
\boxed{\mathbf p_e=q\mathbf l},\qquad \mathbf l\text{ 从负电荷指向正电荷}.
$$

在距偶极子很远的地方 $r\gg l$，

$$
U=\frac{\mathbf p_e\cdot\mathbf e_r}{4\pi\varepsilon_0r^2},\qquad
\mathbf E=\frac{3(\mathbf p_e\cdot\mathbf e_r)\mathbf e_r-\mathbf p_e}{4\pi\varepsilon_0r^3}.
$$

场按 $1/r^3$ 衰减，比点电荷的 $1/r^2$ 更快；电势中的点乘决定正负。在中垂面上 $U=0$，但 $\mathbf E=-\mathbf p_e/(4\pi\varepsilon_0r^3)$，仍不为零。




<figure class="physics-figure">
  <a href="/images/physics/ch09-dipole.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch09-dipole.svg" alt="负电荷在左下、正电荷在右上，外电场向右，正电荷受力右、负电荷受力左，力矩向纸内。" width="640" height="470" loading="lazy" decoding="async" /></a>
  <figcaption>图9-8　倾斜电偶极子在匀强场中的力与力矩。叉乘给出的力矩朝纸内，对应顺时针转动。</figcaption>
</figure>

放入**均匀**外电场时，两端受力等大反向，合力为零，但一般有力矩：

$$
\boxed{\boldsymbol\tau=\mathbf p_e\times\mathbf E},\qquad
\boxed{W_p=-\mathbf p_e\cdot\mathbf E=-p_eE\cos\theta}.
$$

力矩用**叉乘**，能量用**点乘**。力矩让电偶极矩转向电场方向；同向能量最低、稳定，反向能量最高、不稳定。非均匀场中，两端受力不再等大，偶极子还可能整体移动。

## 8. 做题时怎样选择工具

已知电荷分布，先判断对称性：高度对称时用高斯定理；普通线、面分布用电荷元积分。求电势通常比求场强简单，能先求 $U$ 再求导时，可少做矢量分解。求功直接用 $q(U_A-U_B)$，不必沿实际曲线积分。

最后检查三个问题：方向是否写明；$Q_{\text{内}}$ 是否真的只算高斯面内；零电势参考是否一致。本章公式与磁场公式的逐项对照，见系列的[电场与磁场比较专题](/posts/physics-comparison)。
