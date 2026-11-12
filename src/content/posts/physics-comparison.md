---
title: "比较专题：把电场与磁场放在一起理解"
description: "贯通第9～14章：六个场量、两类积分、基本定理、极化与磁化、边界条件、偶极矩、储能和感应的比较辨析。"
pubDate: 2026-11-12
tags: [大学物理, 电磁学, 比较辨析, 学习笔记]
series:
  name: 大学物理电磁学笔记
  order: 8
---

电场和磁场的公式有许多相似之处。正确的类比能减少记忆量，关键是先说清楚：**正在比较场本身、物质的响应，还是为了计算引入的辅助量？**

本篇串联教材第9～14章。主要对应 §9.3～9.8、§10.3～10.6、§11.1～11.3、§12.1～12.6、§13.1～13.5、§14.2～14.5。文中页码均为教材印刷页码；按专题顺序复习，可结合[系列目录](/posts/physics-guide/)回到各章。

## 一、先建立正确的对应关系

| 要比较的角色 | 电学 | 磁学 | 一句话理解 |
| --- | --- | --- | --- |
| 直接进入基本受力公式的场 | 电场强度 $\mathbf E$ | 磁感应强度 $\mathbf B$ | 场怎样作用于电荷 |
| 物质的响应 | 电极化强度 $\mathbf P$ | 磁化强度 $\mathbf M$ | 单位体积的电偶极矩或磁矩 |
| 简化介质计算的辅助量 | 电位移 $\mathbf D$ | 磁场强度 $\mathbf H$ | 把束缚源吸收进定义 |
| 材料的线性响应参数 | 电极化率 $\chi_e$、介电常数 $\varepsilon$ | 磁化率 $\chi_m$、磁导率 $\mu$ | 材料怎样影响场 |

**名字相近的 $\mathbf E$ 与 $\mathbf H$，并不承担相同的受力角色。** 电力用 $\mathbf F_E=q\mathbf E$，磁力用 $\mathbf F_B=q\mathbf v\times\mathbf B$。$\mathbf D$ 的“位移”也不是某个电荷移动的距离，它的单位是 C/m²。

## 二、六个场量：定义、单位、关系

### 1. 场与物质响应分别是什么

$$
\mathbf P=\frac{\sum_i\mathbf p_{e,i}}{\Delta V},
\qquad
\mathbf M=\frac{\sum_i\mathbf p_{m,i}}{\Delta V}.
$$

这里 $\Delta V$ 是足够小、又包含大量分子的体积。$\mathbf p_e$ 是单个电偶极矩，$\mathbf p_m$ 是单个磁矩。两式都是**先按方向求和，再除以体积**。分子各自有偶极矩，宏观总和仍可能为零。

| 量 | 定义或计算入口 | 单位 |
| --- | --- | --- |
| $\mathbf E$ | $\mathbf F_E/q$，试验电荷不能显著改变原场 | V/m |
| $\mathbf B$ | 由磁力的大小和方向测定：$\mathbf F_B=q\mathbf v\times\mathbf B$ | T |
| $\mathbf P$ | 单位体积的总电偶极矩 | C/m² |
| $\mathbf M$ | 单位体积的总磁矩 | A/m |
| $\mathbf D$ | $\varepsilon_0\mathbf E+\mathbf P$ | C/m² |
| $\mathbf H$ | $\mathbf B/\mu_0-\mathbf M$ | A/m |

### 2. 最容易混淆的正负号

定义式是：

$$
\boxed{\mathbf D=\varepsilon_0\mathbf E+\mathbf P},
\qquad
\boxed{\mathbf H=\frac{\mathbf B}{\mu_0}-\mathbf M}.
$$

把直接进入受力公式的 $\mathbf E$ 和 $\mathbf B$ 写在左边，则成为：

$$
\mathbf E=\frac{\mathbf D-\mathbf P}{\varepsilon_0},
\qquad
\mathbf B=\mu_0(\mathbf H+\mathbf M).
$$

因此不能只换字母照抄。在线性、各向同性材料中，再加上材料关系：

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E,
\qquad
\mathbf M=\chi_m\mathbf H,
$$

$$
\mathbf D=\varepsilon\mathbf E,
\quad\varepsilon=\varepsilon_0(1+\chi_e);
\qquad
\mathbf B=\mu\mathbf H,
\quad\mu=\mu_0(1+\chi_m).
$$

注意：$\mathbf P$ 的线性关系用介质中的**合电场** $\mathbf E$；$\mathbf M$ 的线性关系用 $\mathbf H$。真空中 $\mathbf P=\mathbf M=\mathbf0$，所以 $\mathbf D=\varepsilon_0\mathbf E$、$\mathbf B=\mu_0\mathbf H$，并不是 $\mathbf D=\mathbf E$、$\mathbf B=\mathbf H$。

铁磁质存在非线性和磁滞，不能把 $\chi_m$ 或 $\mu$ 当作与场强、历史无关的常量。各向异性材料中，响应方向也可能不与场平行。

## 三、通量与环流：一个看穿过，一个看绕行

$$
\Phi=\int_S\mathbf A\cdot\mathrm d\mathbf S,
\qquad
\Gamma=\oint_L\mathbf A\cdot\mathrm d\mathbf l.
$$

$\mathbf A$ 代表被研究的矢量场。通量累加**法向分量**，环流累加**切向分量**。两者都是标量，正负取决于所选方向。

<figure class="physics-figure">
  <a href="/images/physics/comparison-flux-circulation.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-flux-circulation.svg" alt="面积微元垂直于面，路径微元沿切线；图示比较通量与环流。" width="640" height="660" loading="lazy" decoding="async" /></a>
  <figcaption>图比-1　通量与环流的几何对象和取分量方式不同。</figcaption>
</figure>


| 积分 | 几何对象 | 角度、正方向 | 常见化简 |
| --- | --- | --- | --- |
| 通量 | 面；高斯定理用闭合面 | 与面法线夹角；闭合面向外为正 | 均匀场穿平面：$AS\cos\theta$ |
| 环流 | 闭合曲线 | 与路径切线夹角；先选绕行方向 | 等大切向场沿圆：$A\,2\pi r$ |

电场的高斯定理与磁场的高斯定理比较的是**闭合面通量**。静电环路定理与安培环路定理比较的是**闭合线环流**。不要因为它们都带小圆圈，就把面和线认成同一种积分。

## 四、四条基本定理一起看

以下磁场环路公式用于稳恒情形，$Q_f$ 表示面内自由电荷，$Q_b$ 表示面内束缚（极化）电荷；$I_f$ 表示穿过环路所围面的自由（传导）电流代数和，$I_b$ 表示磁化电流代数和。

| 性质 | 静电场 | 稳恒磁场 |
| --- | --- | --- |
| 基本场的高斯定理 | $\displaystyle\oiint_S\mathbf E\cdot\mathrm d\mathbf S=(Q_f+Q_b)/\varepsilon_0$ | $\displaystyle\oiint_S\mathbf B\cdot\mathrm d\mathbf S=0$ |
| 基本场的环路定理 | $\displaystyle\oint_L\mathbf E\cdot\mathrm d\mathbf l=0$ | $\displaystyle\oint_L\mathbf B\cdot\mathrm d\mathbf l=\mu_0(I_f+I_b)$ |
| 介质中更方便的形式 | $\displaystyle\oiint_S\mathbf D\cdot\mathrm d\mathbf S=Q_f$ | $\displaystyle\oint_L\mathbf H\cdot\mathrm d\mathbf l=I_f$ |
| 基本特征 | 有源、无旋 | 无源、有旋 |

“有源”指允许场线从电荷发出或终止，即封闭面净通量可以不为零；“无源”指没有磁单极源，磁感应线没有起点或终点。“无旋”指静电场绕闭合路径的积分为零；“有旋”指磁场可以具有非零环流，**不等于每一条环路的环流都非零**。

### 两个必须分开的判断

**积分只看包围的源，场值要看全部源。** 高斯面外的电荷对封闭面净通量贡献为零，但对面上各点 $\mathbf E$ 可以有贡献；环路外的电流对该环流的贡献为零，但对环路上各点 $\mathbf B$ 可以有贡献。

**定理成立，不代表总能用它直接求场。** 必须有足够对称性，才能把未知场量提出积分号。求电场常找球对称、柱对称、平面对称；求磁场常找长直导线、长螺线管、理想密绕环形线圈。

**辨析小题（自编）**：均匀电场通过一个不含电荷的球面，净通量为零；一个圆环未穿过净电流，磁环流为零。能分别推出 $\mathbf E=\mathbf0$ 和 $\mathbf B=\mathbf0$ 吗？

**答**：都不能。前者是穿入与穿出抵消；后者是切向贡献的积分抵消或处处没有切向分量，都不要求整个场为零。

<figure class="physics-figure">
  <a href="/images/physics/comparison-zero-flux.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-zero-flux.svg" alt="均匀电场从球面左侧穿入、右侧穿出，两侧通量抵消。" width="640" height="400" loading="lazy" decoding="async" /></a>
  <figcaption>图比-2　零净通量的反例：没有包围电荷的球面仍可处于非零匀强场中。</figcaption>
</figure>


## 五、为什么引入 D 和 H：把束缚源换一种记法

教材 p75～76、185～187 的推导可以并排压缩为三步。

### 电学：把极化电荷移到左边

极化强度与闭面内束缚电荷满足

$$
Q_b=-\oiint_S\mathbf P\cdot\mathrm d\mathbf S.
$$

代入电场高斯定理，再移项：

$$
\varepsilon_0\oiint_S\mathbf E\cdot\mathrm d\mathbf S
=Q_f-\oiint_S\mathbf P\cdot\mathrm d\mathbf S
\quad\Longrightarrow\quad
\oiint_S(\varepsilon_0\mathbf E+\mathbf P)\cdot\mathrm d\mathbf S=Q_f.
$$

括号里的量就是 $\mathbf D$。

### 磁学：把磁化电流移到左边

$$
I_b=\oint_L\mathbf M\cdot\mathrm d\mathbf l.
$$

代入安培环路定理：

$$
\oint_L\frac{\mathbf B}{\mu_0}\cdot\mathrm d\mathbf l
=I_f+\oint_L\mathbf M\cdot\mathrm d\mathbf l
\quad\Longrightarrow\quad
\oint_L\left(\frac{\mathbf B}{\mu_0}-\mathbf M\right)\cdot\mathrm d\mathbf l=I_f.
$$

括号里的量就是 $\mathbf H$。

**$\mathbf D$ 的通量只显含自由电荷，$\mathbf H$ 的环流只显含自由电流；这不意味着 $\mathbf D$、$\mathbf H$ 本身与介质无关。** 具体的场分布仍须满足材料关系和边界条件。特别是 $\mathbf B$ 无源，不能照搬成 $\mathbf H$ 的闭面通量总为零。

## 六、极化和磁化：微观图像相似在哪里

| 比较项 | 电介质极化 | 磁介质磁化 |
| --- | --- | --- |
| 已有偶极矩的排列 | 有极分子受力矩，平均取向偏向外电场 | 顺磁质的固有磁矩平均偏向外磁场 |
| 外场诱导的响应 | 正负电荷中心相对位移，形成或改变电偶极矩 | 诱导附加磁矩，普通抗磁响应与外场反向 |
| 热运动的作用 | 扰乱取向极化的有序排列 | 扰乱顺磁质固有磁矩的有序排列 |
| 宏观等效源 | 束缚电荷 | 束缚电流，即磁化电流 |
| 表面效应 | 孤立介质表面 $\sigma_b=\mathbf P\cdot\hat{\mathbf n}$ | 磁体表面 $\mathbf K_b=\mathbf M\times\hat{\mathbf n}$ |

$\hat{\mathbf n}$ 为材料表面向外单位法线，$\mathbf K_b$ 是单位横向长度上的表面电流，单位 A/m。最后一行一个是**点乘**，一个是**叉乘**：极化电荷来自电偶极子在表面的终止，磁化电流则沿着表面流动。两种材料交界时，要计算两侧响应的差，不能直接当成材料与真空的界面。

均匀极化介质的体内正负束缚电荷可相互抵消，只在边界剩下；均匀磁化介质的内部相邻分子电流可相互抵消，只在表面留下等效电流。非均匀极化或磁化时，内部也可能存在束缚源。

<figure class="physics-figure">
  <a href="/images/physics/comparison-bound-sources.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-bound-sources.svg" alt="均匀极化体左负右正；向右磁化的材料上表面电流向纸外、下表面向纸内。" width="640" height="650" loading="lazy" decoding="async" /></a>
  <figcaption>图比-3　同样是均匀响应，极化对应表面电荷，磁化对应表面电流。</figcaption>
</figure>


### 三种磁性与电介质的关键差别

| 性质 | 顺磁质 | 抗磁质 | 铁磁质 |
| --- | --- | --- | --- |
| 常见例子 | 铝、氧、锰 | 铜、银、铋、水 | 铁、钴、镍及某些合金 |
| 磁化率 | $\chi_m>0$，很小 | $\chi_m<0$，绝对值很小 | 强、非线性，不能用固定小常量描述 |
| $\mathbf M$ 相对 $\mathbf H$ | 同向 | 反向 | 随磁化状态和历史变化 |
| 相对磁导率 | 略大于1 | 略小于1 | 可远大于1且随状态变化 |
| 温度影响 | 通常升温使顺磁响应减弱 | 通常温度影响较小 | 越过居里温度，铁磁有序性消失，转为顺磁 |
| 撤去外场 | 普通情形宏观磁化消失 | 诱导磁化消失 | 可保留剩磁 |

普通顺磁质也有抗磁响应，只是顺磁效应占优势。“抗磁”不是没有磁性，而是净响应方向相反。没有外场时顺磁质宏观磁化为零，也不代表每个分子的固有磁矩为零。

铁磁质靠磁畴内的自发有序形成强响应；未磁化铁磁体仍有磁畴，只是各畴方向整体抵消。教材第10章的**铁电体**与第13章的**铁磁体**都有自发有序、滞回、剩余响应和居里温度等现象，但前者的有序量是电极化，后者是磁化。“铁电”这个名字不表示材料一定含铁（教材 p72～73、190～194）。

## 七、“加介质，场变强还是变弱”先问控制条件

### 平行板电容器：固定自由电荷，电场减弱

均匀线性电介质完全填满极板间，忽略边缘效应，极板自由电荷面密度 $\sigma_f$ 固定：

$$
D=\sigma_f,\qquad
E=\frac{D}{\varepsilon}=\frac{E_0}{\varepsilon_r}.
$$

但若电容器一直接电源，电压 $U$ 和间距 $d$ 固定，$E=U/d$ 不变，增大的是自由电荷量和 $D$。所以“放介质一定减小电场”缺少条件。

### 理想长螺线管：固定自由电流，磁场按磁导率改变

线圈每单位长度匝数为 $n$，电流 $I$ 固定，磁芯完全填充并保持理想长管对称性：

$$
H=nI,\qquad B=\mu nI=\mu_r B_0.
$$

顺磁质使 $B$ 略增，抗磁质使 $B$ 略减。铁磁芯可显著增大 $B$，但须按实际磁化曲线求值。

这两个常见模型分别是“先由自由电荷求 $D$”和“先由自由电流求 $H$”。任意形状、局部填充材料时，不能直接使用 $E=E_0/\varepsilon_r$ 或 $B=\mu_rB_0$。

## 八、边界条件：电场与磁场的对应关系会变

设界面单位法线 $\hat{\mathbf n}$ 从介质1指向介质2。下标 $n$、$t$ 分别表示法向、切向分量。

| 边界关系 | 电学（静电） | 磁学（稳恒） |
| --- | --- | --- |
| 由闭合面定理得到 | $D_{2n}-D_{1n}=\sigma_f$ | $B_{2n}-B_{1n}=0$ |
| 由环路定理得到 | $\mathbf E_{2t}=\mathbf E_{1t}$ | $\hat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf K_f$ |
| 无自由面源时 | $D_n$ 连续、$E_t$ 连续 | $B_n$ 连续、$H_t$ 连续 |

$\sigma_f$ 是自由面电荷密度；$\mathbf K_f$ 是自由面电流密度。这里的“连续”指分量跨界面不跳变，不代表两侧整个矢量完全相同。

推导的图像相同：用跨界面的薄小柱面消去侧面贡献，得到法向条件；用跨界面的扁小矩形回路消去短边贡献，得到切向条件。

<figure class="physics-figure">
  <a href="/images/physics/comparison-boundary.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-boundary.svg" alt="薄柱面跨越介质界面，上下法线相反；扁矩形的上下长边绕行方向相反。" width="640" height="600" loading="lazy" decoding="async" /></a>
  <figcaption>图比-4　电学与磁学的边界关系，都可从这两种跨界面的小几何体出发。</figcaption>
</figure>


**就边界公式而言，对应的是 $D_n\leftrightarrow B_n$、$E_t\leftrightarrow H_t$。** 这与受力角色的 $\mathbf E\leftrightarrow\mathbf B$ 并不矛盾：类比依赖正在比较的性质。

### 场线“折射”的公式不能反背

两侧为线性各向同性介质，界面无相应自由面源，$\theta_1,\theta_2$ 均取与**法线**的夹角，则

$$
\frac{\tan\theta_1}{\tan\theta_2}
=\frac{\varepsilon_1}{\varepsilon_2}
\quad\text{（电场线、电位移线）},
$$

$$
\frac{\tan\theta_1}{\tan\theta_2}
=\frac{\mu_1}{\mu_2}
\quad\text{（磁感应线）}.
$$

例如电学中 $E_{1t}=E_{2t}$、$\varepsilon_1E_{1n}=\varepsilon_2E_{2n}$，把 $\tan\theta=E_t/E_n$ 代入便得到第一式。两条都是场线在材料界面的方向改变，不是光线折射定律（教材 p79～81、197～199）。

### 静电屏蔽与磁屏蔽

静电平衡的导体内部 $\mathbf E=0$，空腔内没有电荷时可屏蔽外部静电场。普通高磁导率外壳则让磁通更多经过壳体，使腔内磁场减弱，**并不普遍等于严格为零**。其工作依据分别是自由电荷重排和磁通分布改变，不能把导体静电平衡条件套到普通磁体上。

## 九、求场公式：共同靠叠加，方向规则不同

真空中，微小电荷和稳恒电流元的场为

$$
\mathrm d\mathbf E=\frac{1}{4\pi\varepsilon_0}\frac{\mathrm dq}{r^2}\hat{\mathbf r},
\qquad
\mathrm d\mathbf B=\frac{\mu_0}{4\pi}\frac{I\,\mathrm d\mathbf l\times\hat{\mathbf r}}{r^2}.
$$

$\hat{\mathbf r}$ 从源元指向场点。电场贡献沿这条连线，正负由电荷决定；磁场贡献垂直于电流元与连线所在平面，按叉乘定向。分别积分得到总场，不能先把各项大小直接相加。

两条长直源的结果都按 $1/r$ 变化，却有不同方向：

$$
\mathbf E=\frac{\lambda}{2\pi\varepsilon_0r}\hat{\mathbf r}
\quad\text{（无限长均匀带电线）},
\qquad
\mathbf B=\frac{\mu_0I}{2\pi r}\hat{\boldsymbol\varphi}
\quad\text{（无限长直电流）}.
$$

前者沿径向，适合圆柱高斯面；后者绕导线，适合圆周积分路径。$\hat{\boldsymbol\varphi}$ 是与所定电流方向满足右手关系的环向单位矢量。

<figure class="physics-figure">
  <a href="/images/physics/comparison-line-sources.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-line-sources.svg" alt="正长直线电荷的电场沿径向向外；向纸外的长直电流产生逆时针环绕磁场。" width="640" height="420" loading="lazy" decoding="async" /></a>
  <figcaption>图比-5　同样是长直源，场的方向不同，所选积分对象也不同。</figcaption>
</figure>


## 十、力、做功与偶极矩

### 单个电荷：磁场改变运动方向，电场可以改变速率

$$
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B).
$$

$$
\mathbf F_B\cdot\mathbf v
=q(\mathbf v\times\mathbf B)\cdot\mathbf v=0.
$$

磁力总与粒子的瞬时速度垂直，所以单独作用时不改变动能；电力一般可以做功。在静电场中，正电荷沿电场方向移动，电势降低，电场做正功；若无其他力做功，动能增加。负电荷要把电荷符号一起考虑。

载流导线受到的安培力 $\mathrm d\mathbf F=I\,\mathrm d\mathbf l\times\mathbf B$ 却可以使导线运动并输出机械功。这里研究的是导体整体，电源、内部约束和感应电场共同参与能量传递，并非“单粒子磁力不做功”失效。

### 两种偶极子：力矩和稳定方向高度相似

| 比较项 | 电偶极子 | 磁偶极子（小线圈） |
| --- | --- | --- |
| 偶极矩 | $\mathbf p_e=q\boldsymbol\ell$，$q>0$，$\boldsymbol\ell$ 由负电荷指向正电荷 | $\mathbf p_m=NIS\hat{\mathbf n}$，法线按电流右手定则 |
| 单位 | C·m | A·m² |
| 匀强外场中的合力 | 零 | 零 |
| 力矩 | $\boldsymbol\tau=\mathbf p_e\times\mathbf E$ | $\boldsymbol\tau=\mathbf p_m\times\mathbf B$ |
| 固定偶极矩在给定外场中的取向势能 | $W=-\mathbf p_e\cdot\mathbf E$ | $W=-\mathbf p_m\cdot\mathbf B$ |
| 稳定取向 | $\mathbf p_e$ 与 $\mathbf E$ 同向 | $\mathbf p_m$ 与 $\mathbf B$ 同向 |

零力矩有两种取向：同向和反向。前者能量最低，稳定；后者能量最高，不稳定。非均匀场中，偶极子还可受到合力。

远离局域偶极子时，电偶极场和小电流环磁场都按 $1/r^3$ 衰减，场线外观相似；但电偶极子有真实的正负电荷两端，磁偶极子没有可拆出的孤立磁荷，磁感应线还要贯通磁体内部（教材 §9.3、§9.7、§12.2、§12.4）。

## 十一、电势、电动势与涡旋电场

### 电势差描述静电场的两点差别

$$
U_a-U_b=\int_a^b\mathbf E_{\mathrm s}\cdot\mathrm d\mathbf l,
\qquad
\mathbf E_{\mathrm s}=-\nabla U.
$$

$\nabla U$ 是“电势在空间上升最快的方向及其变化率”，负号表明电场朝电势下降方向。静电力做功只看起终点，不看路线。

### 电动势描述驱动单位正电荷的能量来源

电源电动势用非静电力的功定义。感应电动势可能由导体运动产生，也可能由变化磁场产生。它的单位虽与电势差相同，但物理定义不同。

| 性质 | 静电场 | 涡旋（感生）电场 |
| --- | --- | --- |
| 起因 | 静止电荷 | 变化的磁场 |
| 对电荷的力 | $q\mathbf E_{\mathrm s}$ | $q\mathbf E_{\mathrm i}$ |
| 闭合路径积分 | 零 | 一般不为零 |
| 做功是否与路径有关 | 无关 | 有关 |
| 是否可单用电势描述整个场 | 可以 | 不可以 |
| 是否需要导体存在 | 不需要 | 不需要 |

对固定回路，法拉第定律为

$$
\oint_L\mathbf E_{\mathrm i}\cdot\mathrm d\mathbf l
=-\frac{\mathrm d}{\mathrm dt}\int_S\mathbf B\cdot\mathrm d\mathbf S.
$$

$L$ 的正向与 $S$ 的法线必须满足右手关系。负号表示感应作用阻碍**磁通量的变化**：原磁通增加时反抗增加，原磁通减少时反抗减少，不能简化成“感应磁场永远与原磁场反向”。

稳恒电流中的电场也可以是无旋的，但有电流的普通电阻导体内部需要 $\mathbf E\ne\mathbf0$ 来维持漂移；静电平衡导体内部则为零。两者不要混淆（教材 p98～99、215～218）。

## 十二、电容与电感、RC与RL：储能和暂态的一组对应

| 比较项 | 电容器 | 线性电感线圈 |
| --- | --- | --- |
| 比例关系 | $Q=CU$ | $\Psi=LI$，$\Psi$ 为磁通链 |
| 储能 | $W_e=Q^2/(2C)=CU^2/2$ | $W_m=LI^2/2$ |
| 储能所在 | 电场 | 磁场 |
| 建立能量所需微元功 | $\mathrm dW_e=U\,\mathrm dQ$ | $\mathrm dW_m=LI\,\mathrm dI$ |
| 常规有限激励下不能突变的量 | 电容电压 | 电感电流 |
| 与电阻配合的时间常量 | $\tau=RC$ | $\tau=L/R$ |
| 理想元件直流稳态表现 | 电容支路相当于断路 | 理想电感相当于导线；实际线圈电阻仍存在 |

两个最短的能量推导为

$$
W_e=\int_0^Q\frac{q}{C}\,\mathrm dq=\frac{Q^2}{2C},
\qquad
W_m=\int_0^I Li\,\mathrm di=\frac12LI^2.
$$

其中 $C,L$ 固定。时间常量越大，变化越慢；在简单串联电路中，增大 $R$ 会让 RC 过程变慢，却让 RL 过程变快，因为两者的时间常量中 $R$ 的位置相反。

**初值为零、接恒压源 $\mathcal E$ 时**：

$$
U_C(t)=\mathcal E(1-e^{-t/(RC)}),
\qquad
I_L(t)=\frac{\mathcal E}{R}(1-e^{-tR/L}).
$$

移去电源后，若电容或电感仍分别与电阻构成闭合放电回路，电容电压和电感电流分别按 $e^{-t/(RC)}$、$e^{-tR/L}$ 衰减。对照教材 §11.5 与 §14.4，看清一个跟踪电压，一个跟踪电流。

<figure class="physics-figure">
  <a href="/images/physics/comparison-transients.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-transients.svg" alt="建立曲线从0升到1，t等于时间常量时达到0.632；衰减曲线从1趋近0。" width="640" height="450" loading="lazy" decoding="async" /></a>
  <figcaption>图比-6　用各自的时间常量归一化，RC 电压与 RL 电流具有相同的指数变化形式。</figcaption>
</figure>


## 十三、场能量密度与控制条件

线性、无滞回的介质中，单位体积场能量为

$$
\boxed{w_e=\frac12\mathbf E\cdot\mathbf D},
\qquad
\boxed{w_m=\frac12\mathbf B\cdot\mathbf H}.
$$

各向同性时进一步化为

$$
w_e=\frac12\varepsilon E^2=\frac{D^2}{2\varepsilon},
\qquad
w_m=\frac{B^2}{2\mu}=\frac12\mu H^2.
$$

单位都是 J/m³，总能量为 $W=\int_Vw\,\mathrm dV$，要积分覆盖储能场所在的空间。电磁能量都可以定域在场中。

为何有时增大介电常数使能量增加，有时却使能量减少？固定 $E$ 看 $\varepsilon E^2/2$，固定 $D$ 看 $D^2/(2\varepsilon)$；条件不同，结论不同。同样，固定 $H$ 与固定 $B$ 时增大 $\mu$，也会得出不同趋势。

连着电源改变电容器或线圈参数时，电源也交换能量，不能把“场能量减少”直接等同于“外力做负功”。含磁滞的铁磁体还会损耗能量，不能对整个磁化过程直接套用 $BH/2$（对应教材 p83～86、231～235）。

## 十四、电场与磁场的统一：换参考系会改变划分

教材 §12.6 用载流导线附近的电荷说明：在一个参考系里看到的电荷静止，在另一个参考系里可能运动；相应的电场和磁场也会发生变换。对同一物理过程，有的参考系中电力和磁力的分担方式会不同，但对可观测运动的描述应当相容。

所以“电荷只产生电场、电流只产生磁场”只是静态入门模型的简写。运动电荷一般具有电场和磁场；第14章又说明，变化的磁场能够激发电场。两者是同一电磁场在给定参考系中的不同组成。

## 十五、最后用六句话检查有没有串台

1. **受力认 $\mathbf E,\mathbf B$，物质响应认 $\mathbf P,\mathbf M$，介质辅助量认 $\mathbf D,\mathbf H$。**
2. **通量看法向、环流看切向；积分为零不等于场处处为零。**
3. **$\mathbf D$ 的通量只显自由电荷，$\mathbf H$ 的稳恒环流只显自由电流，但场分布仍受介质影响。**
4. **电介质边界常记 $D_n,E_t$，磁介质边界常记 $B_n,H_t$，先检查自由面源。**
5. **静电场无旋，涡旋电场一般有非零环流；电势差与电动势同单位、不同定义。**
6. **比较能量、加介质的效果和暂态时，先说清哪个量保持不变。**
