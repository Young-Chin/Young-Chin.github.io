---
title: '[Survey] A Survey about the Watermark Removal'
date: 2024-04-28
permalink: /posts/2024/04/watermark/
tags:
  - Watermark Removal
  - Paper Collections
---

**总结：** 调研了目前可尝试的一些水印去除方案，主要分为专属水印去除模型和基于扩散模型inpainting的水印去除。前者主要集中在水印的检测、提取和图像复原的pipeline上面，后者主要集中在图像的条件生成上（图生图），即不关心水印提取，只关心水印的定位和能否较好的重绘mask(水印)区域。从调研结果来看，目前开源和复现的专门用于水印去除的模型主要还是以22年以前的模型为主，近一两年的专属模型提出较少。而基于扩散模型Inpainting的生成式方法提出较多，但其需要手动选定水印区域或结合水印检测定位模块组合使用。且各自模型在水印去除的场景下，效果和速度不一。

---

**名称：** [A self-supervised CNN for image watermark removal](https://arxiv.org/pdf/2303.15435)

**地址：** [GitHub - hellloxiaotian/SSNet: A self-supervised network for image denoising and watermark removal (Neural Networks 2024)](https://github.com/hellloxiaotian/SSNet)——去噪+去水印

[GitHub - hellloxiaotian/SWCNN: A self-supervised CNN for image watermark removal (IEEE Transactions on Circuits and Systems for Video 2024)](https://github.com/hellloxiaotian/SWCNN)——去水印

[GitHub - hellloxiaotian/PSLNet: Perceptive self-supervised learning network for noisy image watermark removal （IEEE Transactions on Circuits and Systems for Video 2024）](https://github.com/hellloxiaotian/PSLNet)——噪声情况下的水印去除

**作者：** 西工大

**摘要：** 在图像水印去除中，流行的方法以监督的方式依赖于给定的参考非水印图像。然而，参考非水印图像在现实世界中很难获得。与此同时，当被数字设备捕获时，它们经常受到噪音的影响。为了解决这些问题，在本文中，我们提出了一个用于图像去噪和水印去除（SSNet）的自我监督网络。SSNet以自我监督的学习方式使用并行网络来消除噪音和水印。具体来说，每个子网络包含两个子块。根据噪声对噪声，上层子网络使用第一个子块来消除噪声。然后，根据水印的分布，上层子网络中的第二个子块用于删除水印。为了防止重要信息的丢失，较低的子网络用于以自我监督的学习方式同时学习噪音和水印。此外，两个子网络通过关注进行交互，以提取更互补的突出信息。拟议的方法不依赖配对图像来学习盲去异和水印去除模型，这对实际应用非常有意义。此外，它比公共数据集中流行的图像水印去除方法更有效。

**Tips：** 有“噪声下去水印“、“去噪+去水印”，“去水印” 三个版本；故发了三篇文章。

![Refer to caption](https://arxiv.org/html/2403.05807v1/x1.png)

**样例：** ![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-24-14-52-13-image.png?msec=1715218329911) 

![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-24-14-51-50-image.png?msec=1715218329911)

---

**名称：** Watermark-Removal

**地址：** [GitHub - zuruoke/watermark-removal: a machine learning image inpainting task that instinctively removes watermarks from image indistinguishable from the ground truth image](https://github.com/zuruoke/watermark-removal)

**作者：** Chimzuruoke Okafor

**摘要：** 一个开源项目，使用基于机器学习的图像彩绘方法从图像中删除水印。

**Tips：** 只针对已获得水印mask的情况，再进行去除，可考虑集合水印定位模块；另外，采用tensor flow编写。

---

**名称：** [DENet: Disentangled Embedding Network for Visible Watermark Removal](https://ojs.aaai.org/index.php/AAAI/article/view/25337/25109)

**地址：** [GitHub - lianchengmingjue/DENet: This is an official pytorch implementation for &quot;DENet: Disentangled Embedding Network for Visible Watermark Removal&quot; (AAAI23).](https://github.com/lianchengmingjue/DENet)

**作者：** 南方科技大学

**摘要：**

在图像中添加可见水印是媒体常见的版权保护方法。与此同时，关于去除水印的公共研究可以作为一种对抗性技术，以帮助水印的进一步发展。现有的水印去除方法主要采用多任务学习网络，可以同时定位水印并恢复背景。然而，这些方法将任务视为图像到图像的重建问题，它们只在最终输出后施加监督，使高级语义功能在不同任务之间共享。为此，受两阶段粗细化网络的启发，我们提出了一种新颖的对比学习机制，以解开图像和水印的高级嵌入语义信息，推动各自的网络分支更加定向。具体来说，拟议的机制用于水印图像分解，其目的是在高级嵌入空间中解耦干净的图像和水印提示。这可以保证恢复图像的学习表示享受更多特定于任务的线索。此外，我们引入了一个基于自注意力机制的增强模块，该模块促进了网络捕获不同区域之间语义信息的能力，从而进一步改进了对比学习机制。为了验证我们建议方法的有效性，对不同的具有挑战性的基准进行了广泛的实验。实验评估表明，我们的方法可以实现最先进的性能，并产生高质量的图像。

![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-24-15-14-33-image.png?msec=1715218329908)

**样例：**

![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-24-15-17-04-image.png?msec=1715218329915)

**名称：** [Removing Interference and Recovering Content Imaginatively for Visible
Watermark Removal](https://arxiv.org/pdf/2312.14383.pdf)

**地址：** 未开源

**Tips：** AAAI2023

**摘要：**

可见水印虽然有助于保护图像版权，但经常会扭曲底层内容，使场景解释和图像编辑等任务变得复杂。可见水印去除的目的是消除水印的干扰，恢复背景内容。然而，现有的方法通常在单个分支内实现水印分量去除和背景恢复任务，导致预测中残留水印并忽略水印严重模糊背景的情况。为了解决这些局限性，本研究引入了“想象地消除干扰和恢复内容”（RIRCI）框架。 RIRCI体现了一个两阶段的方法：初始阶段集中于识别和分离水印成分，而后续阶段则集中于背景内容恢复。为了实现细致的背景恢复，我们提出的模型采用了双路径网络，能够充分探索半透明水印下的内在背景信息和未受影响区域的外围上下文信息。此外，全局和局部上下文交互模块建立在多层感知器和双向特征转换的基础上，用于背景恢复阶段的综合表示建模。我们的方法的有效性在两个大型数据集上得到了实证验证，我们的研究结果表明比现有的水印去除技术有显着的增强。

![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-25-20-52-27-image.png?msec=1715218329910)

**样例：**

![](file:///Users/admin/Library/Application%20Support/marktext/images/2024-04-25-20-55-01-image.png?msec=1715218329926)

---

**以下是22年以前较为传统的模型**

---

名称：[[2012.07007] Split then Refine: Stacked Attention-guided ResUNets for Blind Single Image Visible Watermark Removal](https://arxiv.org/abs/2012.07007)

地址：[GitHub - vinthony/deep-blind-watermark-removal: [AAAI 2021] Split then Refine: Stacked Attention-guided ResUNets for Blind Single Image Visible Watermark Removal](https://github.com/vinthony/deep-blind-watermark-removal.git)

作者： 澳门大学 潘志文 组；

Tips：AAAI 2021

摘要：

数字水印是保护媒体版权的常用技术。同时，为了增加水印的鲁棒性，攻击技术，如去除水印，也引起了社区的关注。以前的水印去除方法需要从用户那里获取水印位置或训练多任务网络不分青红皂白地恢复背景。然而，当共同学习时，网络在水印检测方面比恢复纹理更好。受这一观察结果的启发，为了盲目地消除可见的水印，我们提出了一个新的两阶段框架，带有堆叠的注意力引导的ResUNets，以模拟检测、删除和细化的过程。在第一阶段，我们设计了一个名为SplitNet的多任务网络。它总共学习了三个子任务的基本功能，而特定任务的功能则分别使用多个通道关注。然后，通过预测的掩模和粗糙的恢复图像，我们设计了RefineNet，以掩码引导的空间注意力来平滑水印区域。除了网络结构外，拟议的算法还结合了多个感知损失，以提高视觉和数值质量。我们在各种设置下广泛评估了四个不同数据集的算法，实验表明，我们的方法远远优于其他最先进的方法。

自测效果：

泛化效果还是较差，对于色彩差异不明显的水印无法完整定位，甚至无法定位。

| ![图片1](file:///Users/admin/Documents/GitHub/deep-blind-watermark-removal/image/000000.jpg?msec=1715218329865) | ![图片2](file:///Users/admin/Documents/GitHub/deep-blind-watermark-removal/results/immask0.png?msec=1715218329883) | ![图片3](file:///Users/admin/Documents/GitHub/deep-blind-watermark-removal/results/imwatermark0.png?msec=1715218329847) | ![图片4](file:///Users/admin/Documents/GitHub/deep-blind-watermark-removal/results/imrefine0.png?msec=1715218329895) |
| --- | --- | --- | --- |
| 原图  | 水印Mask | 提取水印 | 复原结果 |

---

名称：[WDNet: Watermark-Decomposition Network for Visible Watermark Removal](https://arxiv.org/pdf/2012.07616.pdf)

地址：[GitHub - MRUIL/WDNet](https://github.com/MRUIL/WDNet.git)

作者： 杭州电子科技大学

Tips：WACV2021

摘要：

可见水印广泛用于图像中以保护版权所有权。分析水印去除有助于以对抗性方式强化抗攻击技术。当前的去除方法通常利用图像到图像的转换技术。然而，水印的大小、形状、颜色和透明度的不确定性为这些方法设置了巨大的障碍。为了解决这个问题，我们将传统的水印图像分解结合到一个两阶段生成器中，称为水印分解网络（WDNet），其中第一阶段预测整个水印图像的粗略分解，第二阶段专门集中于水印区域以细化去除结果。分解公式使 WDNet 能够将水印从图像中分离出来，而不是简单地删除它们。我们进一步表明，这些分离的水印可以作为构建更大的训练数据集并进一步提高水印去除效果。此外，我们构建了一个名为 CLWD 的大型数据集，其中主要包含彩色水印，以填补彩色水印去除数据集的真空。对公共灰度数据集 LVW 和 CLWD 的大量实验一致表明，所提出的 WDNet 在准确性和效率方面均优于最先进的方法。

---

名称：[[1904.02756] Blind Visual Motif Removal from a Single Image](https://arxiv.org/abs/1904.02756)

地址：[GitHub - amirhertz/visual_motif_removal](https://github.com/amirhertz/visual_motif_removal.git)

作者： Tel Aviv University

Tips：2019

摘要：

在网络上共享的许多图像包括叠加对象或视觉图案，如文本、符号或图纸，为图像添加描述或装饰。例如，指定图像拍摄位置的装饰性文本会反复出现在各种不同的图像中。通常，重复出现的视觉主题在语义上相似，但在位置、风格和内容（例如文本位置、字体和字母）上有所不同。这项工作提出了一种基于深度学习的技术，用于盲目移除此类物体。在盲环境中，图案的位置和确切几何形状是未知的。我们的方法同时估计哪些像素包含视觉主题，并合成底层的潜在图像。它适用于单个输入图像，无需任何用户帮助指定图案的位置，实现盲目去除不透明和半透明视觉图案的最新结果。

---

名称：[Visible Watermark Removal via Self-calibrated Localization and Background Refinement](https://arxiv.org/pdf/2108.03581.pdf)

地址：[GitHub - bcmi/SLBR-Visible-Watermark-Removal](https://github.com/bcmi/SLBR-Visible-Watermark-Removal.git)

作者： 上海交通大学 BCMI实验室

Tips：ACM MM2021

摘要：

在图像上叠加可见水印为应对版权问题提供了有力的武器。水印去除技术可以以对抗性方式增强可见水印的鲁棒性，引起了越来越多的研究兴趣。现代水印去除方法同时执行水印定位和背景恢复，这可以被视为多任务学习问题。然而，现有的方法存在检测到的水印不完整和恢复背景的纹理质量下降的问题。因此，我们设计了一个两阶段多任务网络来解决上述问题。粗略阶段由水印分支和背景分支组成，其中水印分支对粗略估计的掩模进行自校准，并将校准后的掩模传递到背景分支以重建水印区域。在细化阶段，我们集成多级特征来提高水印区域的纹理质量。对两个数据集的大量实验证明了我们提出的方法的有效性。

---

名称：[On the Effectiveness of Visible Watermarks](http://openaccess.thecvf.com/content_cvpr_2017/papers/Dekel_On_the_Effectiveness_CVPR_2017_paper.pdf)

地址：[GitHub - Sukhdip-Sandhu/Automatic-Watermark-Removal: Python computer vision project that aims to automatically remove the watermarks of stock images. The algorithm is designed off of those of Google researchers](https://github.com/Sukhdip-Sandhu/Automatic-Watermark-Removal)

[GitHub - Sukhdip-Sandhu/Automatic-Watermark-Removal: Python computer vision project that aims to automatically remove the watermarks of stock images. The algorithm is designed off of those of Google researchers](https://github.com/Sukhdip-Sandhu/Automatic-Watermark-Removal)

作者： Google Research

Tips：未开源，但有一些复现代码如上

摘要：

可见水印是一种广泛使用的技术，用于标记和保护网络上数百万张图像的版权，但它存在固有的安全缺陷——水印通常以一致的方式添加到许多图像中。我们证明，这种一致性可以自动估计水印并以高精度恢复原始图像。具体来说，我们提出了一种通用的多图像抠图算法，该算法将带水印的图像集合作为输入，并自动估计“前景”（水印）、其 alpha 遮罩和“背景”（原始）图像。由于这种攻击依赖于图像集合中水印的一致性，因此我们探索并评估了水印嵌入中各种类型的不一致如何影响它，这些不一致可能会用于使水印更加安全。我们在网络上提供的库存图像上演示了该算法，并对合成水印数据提供了广泛的定量分析。本文的一个关键要点是，可见水印的设计不仅应该能够稳健地防止从单个图像中删除，而且还应该更能抵抗从图像集合中大规模删除。

### 基于扩散模型的图像擦除/复原

---

**名称：** [LaMa/LaMa Cleaner]([[2109.07161] Resolution-robust Large Mask Inpainting with Fourier Convolutions](https://arxiv.org/abs/2109.07161))

**地址：** [GitHub - playgroundai/lama-cleaner: Fork of https://github.com/Sanster/lama-cleaner](https://github.com/playgroundai/lama-cleaner)

**作者：** 三星研究中心

**Tips：** LaMa CLeaner是基于Lama的擦除修复集成工具

---

**名称：**[# MAT: Mask-Aware Transformer for Large Hole Image Inpainting ]([[2203.15270] MAT: Mask-Aware Transformer for Large Hole Image Inpainting](https://arxiv.org/abs/2203.15270))

**地址：** [fenglinglwb/large-hole-image-inpainting – Run with an API on Replicate](https://replicate.com/fenglinglwb/large-hole-image-inpainting)

**Tips：** CVPR2022 Best Paper

---

**名称：** [Incremental Transformer Structure Enhanced Image Inpainting with Masking Positional Encoding]([[2203.00867] Incremental Transformer Structure Enhanced Image Inpainting with Masking Positional Encoding](https://arxiv.org/abs/2203.00867))

**地址：** [GitHub - DQiaole/ZITS_inpainting: [CVPR 2022] Incremental Transformer Structure Enhanced Image Inpainting with Masking Positional Encoding](https://github.com/DQiaole/ZITS_inpainting)

**作者：** 复旦大学

**Tips：** 与以前的方法相比，更好的整体结构修复效果。有最新版本ZITS++，收录在TPAMI2023

---

**名称：** [MI-GAN: A Simple Baseline for Image Inpainting on Mobile Devices](https://openaccess.thecvf.com/content/ICCV2023/papers/Sargsyan_MI-GAN_A_Simple_Baseline_for_Image_Inpainting_on_Mobile_Devices_ICCV_2023_paper.pdf)

**地址：**[ GitHub - Picsart-AI-Research/MI-GAN: [ICCV 2023] MI-GAN: A Simple Baseline for Image Inpainting on Mobile Devices](https://github.com/Picsart-AI-Research/MI-GAN)

**Tips：** MI-GAN可以在复杂的场景图像和面部图像上产生合理的结果。MI-GAN实现了低FID，同时比最近的SOTA方法参数量小一个数量级，速度也快一个数量级。
