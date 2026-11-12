---
title: "导学：从高中物理走进电磁学"
description: "大学物理中册第9～14章阅读路线，以及矢量、点乘、叉乘、积分、方向和单位的入门工具。"
pubDate: 2026-11-12
tags: [大学物理, 电磁学, 学习笔记]
series:
  name: 大学物理电磁学笔记
  order: 1
---

这套笔记对应吴泽华、陈治中、黄正东编著《大学物理》中册（第三版，浙江大学出版社）的第9～14章。主线是：**电荷产生电场，电流产生磁场，物质会对场作出响应，变化的磁场又会产生电场。**

每章按教材小节讲解：先建立直观认识，再给出公式、适用条件和关键推导，最后用相应的课后题检验理解。题目采用题意简述，保留教材编号和必要条件；“思考题”和“习题”分开标注，解答紧跟题目。

图示中的 ⊙ 表示指向纸外，⊗ 表示指向纸内；字母沿用相邻正文的约定。点击图片可以放大，放大后可滑动查看细节。

## 一、目录与学习路线

| 阅读顺序 | 笔记 | 这一篇解决什么问题 | 教材印刷页码 |
| --- | --- | --- | --- |
| 1 | 本篇导学 | 看懂矢量、积分、符号和方向 | — |
| 2 | [第9章：真空中的静电场](/posts/physics-09/) | 怎样由电荷求电场、电势和功 | 3～51 |
| 3 | [第10章：静电场中的导体和电介质](/posts/physics-10/) | 导体怎样分配电荷，介质怎样极化，电场怎样储能 | 52～93 |
| 4 | [第11章：稳恒电流](/posts/physics-11/) | 电荷怎样持续流动，电源怎样供能 | 94～115 |
| 5 | [第12章：稳恒磁场](/posts/physics-12/) | 电流怎样产生磁场，磁场怎样作用于电流与粒子 | 116～176 |
| 6 | [第13章：磁场中的磁介质](/posts/physics-13/) | 顺磁、抗磁、铁磁有什么区别，如何计算介质中的场 | 177～202 |
| 7 | [第14章：电磁感应](/posts/physics-14/) | 磁通量变化怎样产生电动势，电感怎样储能 | 203～244 |
| 8 | [专题：电场与磁场的比较辨析](/posts/physics-comparison/) | 将六章中的相似公式和本质差异放在一起 | 跨章 |

页码均指书上印刷页码。配套扫描文件中，**PDF页面序号＝印刷页码＋10**。章末思考题和习题计入上表范围。教材标星的小节也有整理，可在掌握主线后阅读。

建议第一遍按章节顺序读；学完第13章后，回到专题比较六个场量；学完第14章后，再比较静电场与涡旋电场。

## 二、先看懂矢量：粗体有实际含义

温度、电势、能量只需一个带单位的数表示，是**标量**。力、速度、电场、磁场还需要方向，是**矢量**。

- $\mathbf E$ 表示电场强度矢量；$E=\lvert\mathbf E\rvert$ 表示它的大小，大小不带负号。
- $E_x$ 表示沿 $x$ 轴的分量，可以为负；$E_x=-3\,\mathrm{V/m}$ 表示 $x$ 方向的分量指向 $-x$ 方向。
- $\hat{\mathbf x}$ 是沿 $+x$ 方向、长度为1的单位矢量；$\mathbf E=-3\hat{\mathbf x}\,\mathrm{V/m}$ 同时给出了大小和方向。
- 同一公式里的 $q$ 通常是带正负号的电荷量。电子电量为 $q=-e$，其中 $e>0$。

例如 $\mathbf F=q\mathbf E$：正电荷受力与电场同向，负电荷受力与电场反向。若只求大小，则写成 $F=\lvert q\rvert E$。

### 1. 点乘：取同方向的那部分，结果是数

$$
\mathbf a\cdot\mathbf b=ab\cos\theta.
$$

$\theta$ 是两个矢量的夹角。同向为正，垂直为零，反向为负。例如功的微小变化量：

$$
\mathrm dA=\mathbf F\cdot\mathrm d\mathbf l.
$$

力沿位移方向的分量才做功。点乘满足 $\mathbf a\cdot\mathbf b=\mathbf b\cdot\mathbf a$。

<figure class="physics-figure">
  <a href="/images/physics/guide-dot-product.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/guide-dot-product.svg" alt="矢量a斜向右上，b向右，垂足投影长度为a cos theta。" width="640" height="390" loading="lazy" decoding="async" /></a>
  <figcaption>图导-1　斜向矢量在水平方向的投影，决定点乘的大小与正负。</figcaption>
</figure>


### 2. 叉乘：结果有方向，交换顺序会变号

$$
\lvert\mathbf a\times\mathbf b\rvert=ab\sin\theta,
\qquad
\mathbf b\times\mathbf a=-\mathbf a\times\mathbf b.
$$

结果垂直于两矢量所在平面。右手四指由第一个矢量转向第二个矢量，拇指指向结果方向。取不超过 $180^\circ$ 的转角。例如：

$$
\hat{\mathbf x}\times\hat{\mathbf y}=\hat{\mathbf z},
\qquad
\hat{\mathbf y}\times\hat{\mathbf x}=-\hat{\mathbf z}.
$$

磁力 $\mathbf F_B=q\mathbf v\times\mathbf B$ 必须先确定 $\mathbf v\times\mathbf B$，再根据 $q$ 的正负决定是否反向。这里的 $\times$ 不是可以省掉的普通乘号。

**小检验（自编）**：正电荷向右运动，磁场垂直纸面向外，磁力向哪里？取右为 $+x$、上为 $+y$、纸外为 $+z$，有 $\hat{\mathbf x}\times\hat{\mathbf z}=-\hat{\mathbf y}$，所以向下。若是电子，则向上。

<figure class="physics-figure">
  <a href="/images/physics/guide-cross-product.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/guide-cross-product.svg" alt="磁场向纸外，速度向右；正电荷受力向下，负电荷受力向上。" width="640" height="450" loading="lazy" decoding="async" /></a>
  <figcaption>图导-2　相同速度和磁场下，正、负电荷的磁力方向相反。</figcaption>
</figure>


## 三、积分：把很多小部分正确地加起来

大学物理比高中物理多的一步，通常是把不能视为均匀的对象切成小段、小面或小体积。

### 1. 电荷分布：先把一小块电荷写出来

$$
\mathrm dq=\lambda\,\mathrm dl,
\qquad
\mathrm dq=\sigma\,\mathrm dS,
\qquad
\mathrm dq=\rho\,\mathrm dV.
$$

$\lambda$ 是单位长度电荷量，$\sigma$ 是单位面积电荷量，$\rho$ 是单位体积电荷量。它们不一定处处相同；若随位置变化，要放在积分号内。

例如长 $L$ 的均匀细线带电 $Q$，则 $\lambda=Q/L$，长度 $\mathrm dx$ 的小段带电 $\mathrm dq=(Q/L)\mathrm dx$。把小段贡献 $\mathrm d\mathbf E$ 按方向相加，得到总场 $\mathbf E=\int\mathrm d\mathbf E$。

### 2. 线积分与面积分分别在算什么

| 写法 | 在加什么 | 直观问题 |
| --- | --- | --- |
| $\int_a^b\mathbf E\cdot\mathrm d\mathbf l$ | 沿路径的电场分量×小段长度 | 单位正电荷沿这条路，电场做多少功 |
| $\int_S\mathbf E\cdot\mathrm d\mathbf S$ | 垂直于面的电场分量×小块面积 | 电场穿过这个面的净通量有多大 |
| $\int_V w\,\mathrm dV$ | 每小块空间的能量 | 这片空间共存了多少能量 |

面积矢量定义为 $\mathrm d\mathbf S=\hat{\mathbf n}\mathrm dS$，方向**垂直于面**。因此 $\mathbf E\cdot\mathrm d\mathbf S=E\cos\theta\,\mathrm dS$ 中的角度是电场与法线的夹角，不是与面的夹角。

积分号上的小圆圈表示“闭合”：$\oint_L$ 沿一圈闭合路径，$\oiint_S$ 对整个封闭曲面。路径是一条线，曲面是一张面，二者不能混用。封闭曲面取向外法线为正；开曲面先选法线，再用右手定则配套规定边界绕行方向。

<figure class="physics-figure">
  <a href="/images/physics/comparison-flux-circulation.svg" target="_blank" rel="noopener" title="打开大图"><img src="/images/physics/comparison-flux-circulation.svg" alt="上图显示场与面法线的夹角；下图显示圆路径上沿切线的场与线元。" width="640" height="660" loading="lazy" decoding="async" /></a>
  <figcaption>图导-3　一个对面求和，一个沿线求和；先看清微元的方向。</figcaption>
</figure>


### 3. 什么时候可以把场提出积分号

要同时检查**大小是否恒定**、**夹角是否已知**。均匀电场垂直平面时，通量才直接成为 $ES$；沿圆周处处等大的切向磁场，环流才成为 $B\,2\pi r$。仅仅“画了一个圆”不会让真实的场自动对称。

## 四、微分、导数和负号

$\mathrm dU/\mathrm dx$ 表示电势沿 $x$ 方向变化得多快。关系

$$
E_x=-\frac{\mathrm dU}{\mathrm dx}
$$

表示电场指向电势下降的方向。若电势还随 $y,z$ 变化，就写偏导数 $E_x=-\partial U/\partial x$：只沿 $x$ 变化，其他坐标暂时不动。

$\mathrm d\Phi/\mathrm dt$ 是磁通量的变化率。磁通量很大但不变，变化率仍为零；磁通量某时刻为零但正穿过零点，变化率可以不为零。

负号常有两类含义：一个是**相对于规定方向为反向**，另一个是**某个量随另一个量增加而减小**。解题先规定方向，再代入带符号的量，最后用物理图像检查。

## 五、常用量、单位和符号冲突

| 量 | 符号 | SI单位 |
| --- | --- | --- |
| 电荷、电流 | $q,I$ | C、A |
| 电势、电势差、电动势 | $U,U_a-U_b,\mathcal E$ | V |
| 电场强度 | $\mathbf E$ | N/C＝V/m |
| 电极化强度、电位移 | $\mathbf P,\mathbf D$ | C/m² |
| 磁感应强度、磁通量 | $\mathbf B,\Phi_B$ | T、Wb |
| 磁化强度、磁场强度 | $\mathbf M,\mathbf H$ | A/m |
| 电容、自感、互感 | $C,L,M$ | F、H、H |
| 能量、能量密度 | $W,w$ | J、J/m³ |

粗体 $\mathbf M$ 是磁化强度，普通斜体 $M$ 可以是互感；力矩写成 $\boldsymbol\tau$ 时，是为了和磁化强度区分。电势沿用教材的 $U$，电势能写 $W$。字母相同不等于物理量相同，要结合定义和单位。

计算常用近似值：

$$
\varepsilon_0\approx8.85\times10^{-12}\,\mathrm{F/m},\quad
\mu_0\approx4\pi\times10^{-7}\,\mathrm{H/m},\quad
e\approx1.60\times10^{-19}\,\mathrm C.
$$

做题可按“画图定方向→找场源与对称性→选定律→写带符号的表达式→代数值和单位”五步走。遇到介质，再补问一句：哪些电荷或电流是自由的，哪些是极化或磁化产生的？

## 六、怎么用这套笔记复习

第一轮看直观解释，能说出每个物理量在描述什么。第二轮遮住解答做精选题，特别检查公式的条件、方向和积分范围。第三轮读比较专题，用一句话回答“为什么这两个公式看起来相似，却不能互换”。

每章中，文字判断和计算同样重要。例如“有磁畴是否一定有宏观磁性”“环路内净电流为零是否代表磁场为零”，都不能只靠记公式判断。理解公式背后的对象和条件，选择题与计算题才能连起来。
