---
title: "第13章：磁场中的磁介质——看懂 B、H、M 与顺磁、抗磁、铁磁"
description: "从微观磁矩理解三类磁介质，梳理磁化电流、介质中的两条基本定理、磁滞与边界条件，配教材典型题解。"
pubDate: 2026-11-12
tags: [大学物理, 电磁学, 学习笔记]
series:
  name: 大学物理电磁学笔记
  order: 6
---

本章对应教材第177～202页（PDF第187～212页）。先记住主线：**线圈电流建立磁场，材料内部的微观磁矩作出响应，这种响应又改变总磁场。** 本文的习题、思考题均取自本章课后题，题干作简述。

## 1. 磁介质：放进磁场后，材料会怎样响应？

**磁化**是材料在磁场作用下呈现磁性的过程；能被磁化的物质称为磁介质。总磁感应强度可按场源分解为

$$
\mathbf B=\mathbf B_0+\mathbf B',
$$

其中 $\mathbf B_0$ 是传导电流产生的磁场，$\mathbf B'$ 是材料磁化产生的附加磁场。两者是矢量相加，不能一律写成大小相加。

### 1.1 三类材料的选择题要点（§13.1、§13.2）

| 性质 | 顺磁质 | 抗磁质 | 铁磁质 |
|---|---|---|---|
| 磁化响应 | 微弱地顺着局部磁场 | 微弱地反着局部磁场 | 强烈磁化，并可能保留磁性 |
| 磁化率 $\chi_m$ | 正且很小 | 负且绝对值很小 | 往往很大，且受磁化状态和历史影响 |
| 相对磁导率 $\mu_r$ | 略大于1 | 略小于1 | 可远大于1，不能视为普遍常数 |
| 微观关键 | 固有磁矩的取向受到外场影响 | 外场引起反向附加磁矩 | 磁畴的扩展和转向 |
| 温度影响 | 常见情形下，温度升高使磁化率减小 | 普通抗磁质的磁化率对温度不敏感 | 超过居里温度，铁磁性消失，转为顺磁性 |
| 教材所举材料 | 铝、铂、钨、氧等 | 铜、银、铋、氦等 | 铁、钴、镍及部分合金、氧化物 |

“顺着/反着”说的是磁化响应方向。用材料是否使给定位置的 $B$ 增大来判断时，还要考虑形状；在教材的长螺线管、闭合细环等模型中，这种增大或减小最直观。

**容易遗漏的文字知识：**

- 所有物质都有抗磁响应。顺磁质中，固有磁矩的取向效应通常更强，所以整体表现为顺磁性。
- 顺磁质未加外场时，分子固有磁矩并未消失，只是热运动使方向杂乱，宏观矢量和近于零。
- 抗磁质的分子固有磁矩相互抵消；加外场后产生的附加磁矩总与外场相反。
- 均匀外场主要使磁矩转向；要比较材料整体被吸向哪里，应看**不均匀磁场**：顺磁、铁磁材料趋向强场区，抗磁材料趋向弱场区。
- 超导体有完全抗磁性，但它与普通抗磁材料的机制不同，不能把普通抗磁质理解为“磁场完全进不去”。




<figure class="physics-figure">
  <a href="/images/physics/ch13-response.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-response.svg" alt="在相同向右磁场强度H下，顺磁材料磁化强度M向右，抗磁材料M向左。" width="640" height="520" loading="lazy" decoding="async" /></a>
  <figcaption>图13-1　顺磁与抗磁的区别是磁化响应方向；普通材料的响应通常很弱。</figcaption>
</figure>

### 思考题13.2｜为什么一种顺磁，一种抗磁？（第199页）

**题意：** 解释顺磁质、抗磁质在外场中磁化的原因。

**解答：** 顺磁质原本就有固有分子磁矩。外场施加磁力矩，使它们更倾向沿场排列；热运动不断打乱排列，所以通常只出现微弱的净同向磁矩。抗磁质的固有分子磁矩为零，外场改变电子运动，产生反向附加磁矩，宏观磁化方向因此反向。不能将两者区别说成“一个有电子运动，一个没有”。

## 2. 从一个电子，到磁化强度与磁化电流

### 2.1 微观磁矩：方向由电荷正负决定

磁矩描述一个小电流环的“磁性方向和强弱”。面积为 $S$、电流为 $I$ 的小环有

$$
\mathbf p_m=IS\mathbf n,
$$

$\mathbf n$ 按电流方向的右手规则确定。磁矩在场中受到的力矩为

$$
\boldsymbol\tau=\mathbf p_m\times\mathbf B.
$$

它倾向于把磁矩转向磁场，不能把叉乘换成点乘。

教材以电子圆轨道说明磁矩与角动量的联系。取 $e>0$ 表示电子电荷量的绝对值，电子质量为 $m_e$：

$$
I=\frac{ev}{2\pi r},\qquad
p_m=I\pi r^2=\frac{evr}{2},\qquad
L=m_evr,
$$

所以电子的轨道磁矩满足

$$
\boldsymbol\mu_{\mathrm{orb}}=-\frac{e}{2m_e}\mathbf L.
$$

**负号表示方向相反：** 电子运动方向与等效正电流方向相反。教材还给出自旋磁矩近似关系 $\boldsymbol\mu_s=-e\mathbf S/m_e$；自旋是电子的内禀性质，不应理解成小球在自转。玻尔磁子是常用磁矩尺度：$\mu_B=e\hbar/(2m_e)\approx9.27\times10^{-24}\,\mathrm{A\,m^2}$。

### 2.2 磁化强度 $\mathbf M$：单位体积的净磁矩

$$
\boxed{\mathbf M=\frac{\sum_i\mathbf p_{m,i}}{\Delta V}}
\qquad [M]=\mathrm{A/m}.
$$

$\Delta V$ 是足够小、又包含很多分子的体积。磁矩方向杂乱时，单个磁矩可以很大，但矢量和很小；方向趋于一致时，$M$ 增大。

### 2.3 磁化电流并不等于导线中的传导电流

可以把分子磁矩看作许多微小电流环。在**均匀磁化**的材料内部，相邻小环的电流互相抵消，表面留下等效环流，这就是表面磁化电流。它来自束缚电子的运动，不是自由电荷绕整个材料流动。

教材用 $j_m$ 表示表面磁化电流的线密度，单位是 $\mathrm{A/m}$，不是体电流密度的 $\mathrm{A/m^2}$。为避免混淆，这里记为 $\mathbf K_m$：

$$
\mathbf K_m=\mathbf M\times\mathbf n,
$$

$\mathbf n$ 是材料表面外法线。在沿轴向均匀磁化的圆柱侧面，$M=K_m$；不能把这个标量等式套到任意表面。非均匀磁化时，内部也可能出现等效磁化电流。

磁化强度的环流与穿过回路所围曲面的磁化电流满足

$$
\oint_L\mathbf M\cdot\mathrm d\boldsymbol\ell=I_{m,\mathrm{enc}}.
$$

这里的电流按正负相加，正方向与回路绕行方向遵循右手规则。

## 3. 介质中的基本规律：先找 H，再求 B 和 M

### 3.1 为什么引入 $\mathbf H$？（§13.3）

总磁场的安培环路定理含两类电流：

$$
\oint_L\mathbf B\cdot\mathrm d\boldsymbol\ell
=\mu_0\left(I_{f,\mathrm{enc}}+I_{m,\mathrm{enc}}\right).
$$

下标 $f$ 表示自由电流，即本章的传导电流。代入上一节磁化电流的关系并移项：

$$
\oint_L\left(\frac{\mathbf B}{\mu_0}-\mathbf M\right)
\cdot\mathrm d\boldsymbol\ell=I_{f,\mathrm{enc}}.
$$

定义**磁场强度**

$$
\boxed{\mathbf H=\frac{\mathbf B}{\mu_0}-\mathbf M},
\qquad
\boxed{\oint_L\mathbf H\cdot\mathrm d\boldsymbol\ell=I_{f,\mathrm{enc}}}.
$$

$H$ 的单位是 $\mathrm{A/m}$，$B$ 的单位是 $\mathrm T$。**决定洛伦兹磁力的是 $\mathbf B$**；$\mathbf H$ 是把磁化电流从环流公式右端分离出去的辅助场量。名字里有“强度”，不代表它可以替换第12章的 $\mathbf B$。

### 3.2 三个量的关系及适用条件

一般的定义关系是

$$
\boxed{\mathbf B=\mu_0(\mathbf H+\mathbf M)}.
$$

对于**线性、各向同性**磁介质，才进一步有

$$
\mathbf M=\chi_m\mathbf H,\qquad
\mu_r=1+\chi_m,\qquad
\mu=\mu_0\mu_r,\qquad
\boxed{\mathbf B=\mu\mathbf H}.
$$

$\chi_m$、$\mu_r$ 无量纲；$\mu$ 的单位是 $\mathrm{H/m}$。各向同性意味着材料不偏爱某个空间方向，因此这些场量可以平行或反平行，磁导率可用标量表示。真空中 $\mathbf M=0$、$\mu_r=1$，但通常 $\mathbf B$ 与 $\mathbf H$ 都不为零。




<figure class="physics-figure">
  <a href="/images/physics/ch13-fields.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-fields.svg" alt="上方首尾相接的蓝色H与红色M箭头之和，等于下方紫色B除以真空磁导率的箭头。" width="640" height="470" loading="lazy" decoding="async" /></a>
  <figcaption>图13-2　B 与 H 的单位不同；将 B 除以 μ₀ 后，才能与 H、M 在同一尺度上作矢量相加。</figcaption>
</figure>

**解题顺序：** 利用对称性从传导电流求 $H$ → 用材料关系求 $B$ → 用 $M=B/\mu_0-H$ 求磁化程度。长螺线管和细螺绕环分别有

$$
H=nI,\qquad H\simeq\frac{NI}{\ell}.
$$

$n$ 为每米匝数，$N$ 为总匝数，$\ell$ 为环的平均磁路长度。环内更精确的表达式为 $H(r)=NI/(2\pi r)$。

### 习题13.1｜插入铁芯，哪些量改变？（第200页）

**题意：** 长直螺线管 $n=1000\,\mathrm{m^{-1}}$，空气中需要 $B_0=4.2\times10^{-4}\,\mathrm T$。求电流；保持电流不变，加入题设 $\mu_r=5000$ 的铁芯，求同一点的 $B$。




<figure class="physics-figure">
  <a href="/images/physics/ch13-solenoid.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-solenoid.svg" alt="上下两个相同长螺线管，空气芯与铁芯中H均向右且大小相同。" width="640" height="600" loading="lazy" decoding="async" /></a>
  <figcaption>图13-3　同样的匝密度和电流给出相同 H；加入铁芯后，材料磁化使 B 改变。</figcaption>
</figure>

**解：** 空气近似真空，

$$
I=\frac{B_0}{\mu_0n}
=\frac{4.2\times10^{-4}}{4\pi\times10^{-7}\times1000}
\approx0.334\,\mathrm A.
$$

在长螺线管近似下，相同 $nI$ 给出相同 $H$；按题设工作状态的磁导率，

$$
B=\mu_r B_0=2.10\,\mathrm T.
$$

**方法：** 线圈电流相同，不代表磁感应强度相同。铁芯的 $\mu_r$ 是题目给定工作状态下的值，不能把5000当作铁在所有状态下的固定常数。

### 习题13.4｜从磁通量反求 H、M 和磁导率（第201页）

**题意：** 环形铁芯平均周长 $\ell=0.30\,\mathrm m$，截面积 $S=1.0\times10^{-4}\,\mathrm{m^2}$，绕 $N=300$ 匝，电流 $I=0.032\,\mathrm A$，磁通量 $\Phi=2.0\times10^{-6}\,\mathrm{Wb}$。求 $H$、$M$、单位长度磁化电流及 $\mu_r$。




<figure class="physics-figure">
  <a href="/images/physics/ch13-toroid.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-toroid.svg" alt="绕线环形铁芯的俯视图，蓝色箭头顺时针沿环向，标出绕组匝数N和铁芯截面S。" width="640" height="530" loading="lazy" decoding="async" /></a>
  <figcaption>图13-4　环路沿铁芯中心绕一周；截面 S 与环向磁场垂直，磁通近似为 BS。</figcaption>
</figure>

**解：** 用细环、截面磁场近似均匀的模型：

$$
B=\frac\Phi S=0.020\,\mathrm T,\qquad
H=\frac{NI}{\ell}=32\,\mathrm{A/m},
$$

$$
M=\frac B{\mu_0}-H
\approx1.588\times10^4\,\mathrm{A/m}.
$$

磁化方向沿环向，边界上等效表面磁化电流的线密度为 $K_m=M$；其方向由 $\mathbf M\times\mathbf n$ 确定。

$$
\mu_r=\frac B{\mu_0H}\approx497.
$$

先算磁通对应的 $B$，再利用环路求 $H$，两条路线各司其职。

### 3.3 磁场的高斯定理仍然成立

$$
\boxed{\oiint_S\mathbf B\cdot\mathrm d\mathbf S=0}.
$$

无论有无磁介质，闭合曲面的磁通量总和都为零。进入多少就出来多少；不等于每一点的 $B$ 都为零，也不等于任意开放曲面的磁通量为零。不能随意把式中的 $\mathbf B$ 改成 $\mathbf H$。

### 思考题13.4｜“环流只含传导电流”究竟说明什么？（第199页）

**题意与解答：**

1. “闭合曲线内没有传导电流，曲线上各点 $H$ 必为零。”**错。** 只能推出环流为零；例如在均匀非零 $\mathbf H$ 中取一个小回路，环流也为零。
2. “闭合曲线上各点 $H$ 都为零，则穿过所围曲面的传导电流代数和为零。”**对。** 直接代入环路定理，但仍可能有大小相等、方向相反的电流穿过。
3. “$\mathbf H$ 只与传导电流有关。”**错。** 环流的右端只有传导电流，不代表每一点的场只由它决定。材料形状、磁化状态和边界条件一般也会影响 $\mathbf H$。

## 4. 铁磁质：为什么“断电后仍有磁性”？（§13.4）

### 4.1 磁畴与自发磁化

铁磁体内部有许多**磁畴**。一个磁畴内，大量原子的磁矩在交换相互作用下趋于一致；这种有序状态不需要先施加外场，称为自发磁化。

未磁化铁块仍有磁畴，只是各畴方向不同，宏观上互相抵消。加外场后，方向有利的磁畴扩展，其他磁畴缩小；外场继续增强，磁矩进一步转向，最后磁化接近饱和。磁畴壁受杂质、内应力等阻碍，撤场时不能完全原路返回，因此出现剩磁和磁滞。

超过**居里温度**，热运动破坏这种有序排列，铁磁体转为顺磁质。剧烈机械振动也可能改变磁畴排列，使剩磁减弱。




<figure class="physics-figure">
  <a href="/images/physics/ch13-domains.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-domains.svg" alt="上下两个分区矩形表示铁磁体，未磁化时各区箭头方向不同，施加向右H后多数磁畴箭头向右。" width="640" height="600" loading="lazy" decoding="async" /></a>
  <figcaption>图13-5　未磁化时，各磁畴的磁矩相互抵消；磁化过程中，有利方向的磁畴扩展并转向。</figcaption>
</figure>

### 4.2 看懂 B–H 曲线

- **起始磁化曲线**：从宏观未磁化状态开始，逐渐增大 $H$ 时的 $B$–$H$ 曲线。
- **饱和磁化**：磁矩排列接近极限，$M$ 不再明显增加。此后 $B=\mu_0(H+M)$ 仍可随 $H$ 增加，不能说 $B$ 从此绝对不变。
- **剩磁 $B_r$**：从磁化状态撤去外场，使 $H=0$ 后仍保留的 $B$。
- **矫顽力 $H_c$**：使沿该磁滞支路的 $B$ 降为零所需的反向 $H$ 的大小。它虽叫“力”，单位却是 $\mathrm{A/m}$。
- **磁滞回线**：反复正反磁化形成的闭合曲线；同一个 $H$ 可以对应不同的 $B$，取决于此前经历。
- **磁滞损耗**：一次循环中转化成热的能量。按单位体积计算，等于 $B$–$H$ 回线围成的面积 $\lvert\oint H\,\mathrm dB\rvert$。

因此铁磁质不能普遍用一个固定 $\mu$ 描述。指定工作点时可用 $\mu=B/H$；小范围变化对应的斜率 $\mathrm dB/\mathrm dH$ 又是另一个量。




<figure class="physics-figure">
  <a href="/images/physics/ch13-hysteresis.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-hysteresis.svg" alt="BH磁滞回线，标出正负剩磁与矫顽力；上支箭头向左，下支箭头向右。" width="640" height="570" loading="lazy" decoding="async" /></a>
  <figcaption>图13-6　从正向磁化状态减小 H，沿红色上支向左；反向磁化后再增大 H，沿蓝色下支向右。</figcaption>
</figure>

### 4.3 软磁、硬磁、矩磁材料

| 材料 | 关键性质 | 典型用途 |
|---|---|---|
| 软磁 | 易磁化，也易退磁；矫顽力小，回线窄，磁滞损耗小 | 电磁铁、变压器、电机铁芯 |
| 硬磁 | 矫顽力大，剩磁不易被消除 | 永久磁铁 |
| 矩磁 | 回线近似矩形，两个稳定剩磁状态清楚 | 用正、反磁化状态记录二进制信息 |

“软、硬”指磁性能，不是机械硬度。高频铁芯还要求电阻率较高，以抑制第14章的涡流损耗；只考虑磁导率不够。

### 思考题13.7｜永久磁铁与电磁铁怎样选材料？（第200页）

**题意：** 教材给出两条不同的磁滞回线，判断哪种更适合永久磁铁、哪种更适合电磁铁。

**解答：** 永久磁铁优先选择矫顽力大、剩磁稳定的硬磁材料；电磁铁需要通电磁化、断电易退磁，选择矫顽力小的软磁材料。判断图时先比较回线与 $H$ 轴交点的远近，而不是只看最高点的 $B$。

### 习题13.7｜消除剩磁需要多大电流？（第201页）

**题意：** 磁棒的矫顽力为 $4.0\times10^3\,\mathrm{A/m}$，放入长 $0.12\,\mathrm m$、绕60匝的长直螺线管，至少通多大电流才能使其沿反向磁化支路的 $B$ 降到零？

**解：** 磁场方向必须与原磁化方向相反。由 $H=NI/\ell$，

$$
I_{\min}=\frac{H_c\ell}{N}
=\frac{4.0\times10^3\times0.12}{60}=8.0\,\mathrm A.
$$

这是“加着反向场时使 $B=0$”的门槛。若希望撤场后剩磁也很小，可用幅度逐渐减小的交变磁场退磁，不能把一次达到矫顽力等同于完成所有退磁过程。

## 5. 边界条件与磁屏蔽（§13.5）

“法向”垂直于分界面，“切向”平行于分界面。跨界面取一个很薄的小柱面，由磁场高斯定理可得

$$
\boxed{B_{1n}=B_{2n}}.
$$

再取跨界面的窄矩形回路；**界面上没有自由面电流**时，安培环路定理给出

$$
\boxed{H_{1t}=H_{2t}}.
$$

有自由面电流时，切向 $H$ 可以发生跃变。若 $\mathbf n$ 从介质1指向介质2，完整写法为

$$
\mathbf n\times(\mathbf H_2-\mathbf H_1)=\mathbf K_f.
$$

注意连续的是 **$B$ 的法向分量、$H$ 的切向分量**，不是 $B$、$H$ 的所有分量。

对于两种线性各向同性介质，且没有自由面电流，令 $\theta_1,\theta_2$ 都是磁感应线与**法线**的夹角：

$$
\frac{\tan\theta_1}{\tan\theta_2}=\frac{\mu_1}{\mu_2}.
$$

推导只需两步：$\tan\theta=B_t/B_n$；再代入 $B_{1n}=B_{2n}$ 和 $B_{1t}/\mu_1=B_{2t}/\mu_2$。




<figure class="physics-figure">
  <a href="/images/physics/ch13-boundary.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-boundary.svg" alt="磁感应线由下方低磁导率介质斜向上进入高磁导率介质后更加偏离竖直法线，标出入射角与折射角。" width="640" height="520" loading="lazy" decoding="async" /></a>
  <figcaption>图13-7　进入磁导率较大的介质，磁感应线偏离法线；注意 θ 从法线量起。</figcaption>
</figure>

高磁导率软磁材料做成外壳，可让磁通更多地经过壳体，削弱腔内磁场，这就是**磁屏蔽**。普通软磁壳内的磁场通常只是减弱，并不严格等于零；它与静电平衡导体的屏蔽机制不同。

### 习题13.3｜铁环开一道气隙，为什么不能直接套 B=μNI/ℓ？（第201页）

**题意：** 铁环平均磁路总长 $0.61\,\mathrm m$，其中空气隙长 $g=0.01\,\mathrm m$，线圈 $N=1000$ 匝、$I=1.5\,\mathrm A$。气隙中 $B=0.18\,\mathrm T$，忽略气隙磁力线发散，求铁的磁导率。




<figure class="physics-figure">
  <a href="/images/physics/ch13-gap.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/ch13-gap.svg" alt="带右侧气隙的环形铁芯，蓝色磁场沿磁路顺时针跨越气隙，标出0.60米铁芯磁路和0.01米气隙。" width="640" height="570" loading="lazy" decoding="async" /></a>
  <figcaption>图13-8　忽略漏磁与发散时，铁芯和气隙中的 B 相同；H 因磁导率不同而不同，必须分段积分。</figcaption>
</figure>

**解：** 铁中磁路长 $\ell_{\mathrm{Fe}}=0.60\,\mathrm m$。截面相同且不计漏磁时，法向 $B$ 连续，所以铁中与气隙的 $B$ 都是 $0.18\,\mathrm T$。然而两个区域的 $H$ 不相同：

$$
H_g=\frac B{\mu_0},\qquad
H_{\mathrm{Fe}}=\frac B\mu.
$$

沿整个磁路积分：

$$
H_{\mathrm{Fe}}\ell_{\mathrm{Fe}}+H_gg=NI.
$$

于是

$$
H_{\mathrm{Fe}}=
\frac{1500-(0.18/\mu_0)\times0.01}{0.60}
\approx112.7\,\mathrm{A/m},
$$

$$
\boxed{\mu=\frac{0.18}{112.7}\approx1.60\times10^{-3}\,\mathrm{H/m}},
\qquad \mu_r\approx1.27\times10^3.
$$

很短的空气隙也消耗了大部分 $NI$：因为相同 $B$ 下，空气的 $H$ 远大于铁中的 $H$。这是磁路题最值得记住的物理图景。

## 6. 一页回看

1. 判断材料：看 $\chi_m$ 的符号、磁畴、温度、剩磁与磁滞，别只背“增强/减弱”。
2. 解场问题：先由传导电流与对称性求 $H$，再用材料关系求 $B$、$M$。
3. $\mathbf B=\mu_0(\mathbf H+\mathbf M)$ 是定义关系；$\mathbf B=\mu\mathbf H$ 需要材料条件。
4. $\oint\mathbf H\cdot\mathrm d\boldsymbol\ell=0$ 不推出 $\mathbf H=0$；$\oiint\mathbf B\cdot\mathrm d\mathbf S=0$ 不推出 $\mathbf B=0$。
5. 边界牢记 $B_n$ 连续、无自由面电流时 $H_t$ 连续；有气隙就分段计算。

与第10章的 $\mathbf E,\mathbf D,\mathbf P$、电边界条件和静电屏蔽的逐项对照，见本系列[电场与磁场比较专题](/posts/physics-comparison/)。
